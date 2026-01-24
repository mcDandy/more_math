from ast import If
import torch
import math
import torch.nn.functional as F
from .MathExprVisitor import MathExprVisitor
from ..helper_functions import generate_dim_variables


class UnifiedMathVisitor(MathExprVisitor):
    def __init__(self, variables, shape=None, device=None, functions=None):
        self.variables = variables
        self.spatial_variables = variables.copy()
        self.shape = shape if shape is not None else (1,)
        if device is None:
            self.device = next((v.device for v in variables.values() if isinstance(v, torch.Tensor)), torch.device("cpu"))
        else:
            self.device = device
        self.functions = functions if functions is not None else {}

    def _is_tensor(self, val):
        return isinstance(val, torch.Tensor)

    def _is_list(self, val):
        return isinstance(val, (list, tuple))

    def _promote_to_tensor(self, val,brodcast=False):
        if self._is_tensor(val):
            return val.contiguous()
        if self._is_list(val):
            return torch.tensor(val, device=self.device)
        if brodcast:
            t = list(self.shape)
            t[0]=1
            return torch.full(t,val,device=self.device)
        return torch.tensor(val, device=self.device)

    def _bin_op(self, a, b, torch_op, scalar_op):
        """
        Generic binary operation handler.
        """
        # one of them is a list and one is tensor
        if self._is_tensor(a) and self._is_list(b):
             if(a.shape[0]==len(b)):
                c = torch.split(a,1)
                return torch.cat([self._bin_op(x, y, torch_op, scalar_op) for x,y in zip(a,c)],dim=0)
             return torch.cat([self._bin_op(a, x, torch_op, scalar_op) for x in b], dim=0)
        if self._is_list(a) and self._is_tensor(b):
            if(b.shape[0]==len(a)):
                c = torch.split(a,1)
                return torch.cat([self._bin_op(x, y, torch_op, scalar_op) for x,y in zip(c,b)],dim=0)
            return torch.cat([self._bin_op(x, b, torch_op, scalar_op) for x in a], dim=0)

        if self._is_list(a) and not self._is_tensor(b):
            if self._is_list(b):
                if len(a) != len(b):
                    raise ValueError("List length mismatch")
                return [self._bin_op(x, y, torch_op, scalar_op) for x, y in zip(a, b)]
            return [self._bin_op(x, b, torch_op, scalar_op) for x in a]

        if not self._is_tensor(a) and self._is_list(b):
            return [self._bin_op(a, x, torch_op, scalar_op) for x in b]

        if self._is_tensor(a) or self._is_tensor(b):
            if torch_op:
                return torch_op(a, b).contiguous()
            return scalar_op(a, b)

        return scalar_op(a, b)

    def _unary_op(self, a, torch_op, scalar_op):
        if self._is_list(a):
            return [self._unary_op(x, torch_op, scalar_op) for x in a]
        if self._is_tensor(a):
            return torch_op(a).contiguous() if torch_op else scalar_op(a)
        return scalar_op(a)

    def _reduction_op(self, val, torch_op, list_op):
        if self._is_tensor(val):
            return torch_op(val)
        if self._is_list(val):
            return list_op(val)
        return val

    # ========================
    # Visitors
    # ========================

    def visitNumberExp(self, ctx):
        val_str = ctx.getText()
        if "." in val_str or "e" in val_str:
            return float(val_str)
        return int(val_str)

    def visitConstantExp(self, ctx):
        name = ctx.getText().lower()
        if name == "pi":
            return math.pi
        if name == "e":
            return math.e
        raise ValueError(f"Unknown constant: {name}")

    def visitVariableExp(self, ctx):
        name = ctx.getText()
        if name not in self.variables:
            raise ValueError(f"Variable '{name}' not found")
        return self.variables[name]

    def visitListExp(self, ctx):
        return [self.visit(e) for e in ctx.expr()]

    def visitParenExp(self, ctx):
        return self.visit(ctx.expr())

    def visitUnaryPlus(self, ctx):
        return self._unary_op(self.visit(ctx.unaryExpr()), lambda x: x, lambda x: +x)

    def visitUnaryMinus(self, ctx):
        return self._unary_op(self.visit(ctx.unaryExpr()), torch.neg, lambda x: -x)

    def visitToIndex(self, ctx):
        return self.visit(ctx.indexExpr())

    def visitIndexExp(self, ctx):
        val = self.visit(ctx.indexExpr())
        index_args = [self.visit(e) for e in ctx.expr()]

        flat_indices = []
        for idx in index_args:
            if self._is_list(idx):
                flat_indices.extend(idx)
            elif self._is_tensor(idx):
                flat_indices.extend(idx.flatten().tolist())
            else:
                flat_indices.append(idx)

        if self._is_tensor(val):
            flat_indices = [i + val.shape[0] if i < 0 else i for i in flat_indices]
            idx_tensor = torch.tensor(flat_indices, device=self.device, dtype=torch.long)
            return torch.index_select(val, 0, idx_tensor)

        elif self._is_list(val):
            flat_indices = [i + len(val) if i < 0 else i for i in flat_indices]
            res = [val[int(i)] for i in flat_indices]
            if len(index_args) == 1 and not (self._is_list(index_args[0]) or self._is_tensor(index_args[0])):
                return res[0]
            return res
        else:
            raise ValueError("Indexing only supported on tensors and lists.")

    def visitToAtom(self, ctx):
        return self.visit(ctx.atom())

    # Binary Ops
    def visitAddExp(self, ctx):
        return self._bin_op(self.visit(ctx.addExpr()), self.visit(ctx.mulExpr()), torch.add, lambda a, b: a + b)

    def visitSubExp(self, ctx):
        return self._bin_op(self.visit(ctx.addExpr()), self.visit(ctx.mulExpr()), torch.sub, lambda a, b: a - b)

    def visitMulExp(self, ctx):
        return self._bin_op(self.visit(ctx.mulExpr()), self.visit(ctx.powExpr()), torch.mul, lambda a, b: a * b)

    def visitDivExp(self, ctx):
        return self._bin_op(self.visit(ctx.mulExpr()), self.visit(ctx.powExpr()), torch.div, lambda a, b: a / b)

    def visitModExp(self, ctx):
        return self._bin_op(self.visit(ctx.mulExpr()), self.visit(ctx.powExpr()), torch.fmod, lambda a, b: a % b)

    def visitPowExp(self, ctx):
        return self._bin_op(self.visit(ctx.unaryExpr()), self.visit(ctx.powExpr()), torch.pow, math.pow)

    def _bool_op(self, a, b, torch_op, scalar_op):
        return self._bin_op(a, b, torch_op, scalar_op)

    def visitNeExp(self, ctx):
        return self._bool_op(self.visit(ctx.compExpr()), self.visit(ctx.addExpr()), torch.ne, lambda a, b: float(a != b))

    def visitEqExp(self, ctx):
        return self._bool_op(self.visit(ctx.compExpr()), self.visit(ctx.addExpr()), torch.eq, lambda a, b: float(a == b))

    def visitGtExp(self, ctx):
        return self._bool_op(self.visit(ctx.compExpr()), self.visit(ctx.addExpr()), torch.gt, lambda a, b: float(a > b))

    def visitLtExp(self, ctx):
        return self._bool_op(self.visit(ctx.compExpr()), self.visit(ctx.addExpr()), torch.lt, lambda a, b: float(a < b))

    def visitGeExp(self, ctx):
        return self._bool_op(self.visit(ctx.compExpr()), self.visit(ctx.addExpr()), torch.ge, lambda a, b: float(a >= b))

    def visitLeExp(self, ctx):
        return self._bool_op(self.visit(ctx.compExpr()), self.visit(ctx.addExpr()), torch.le, lambda a, b: float(a <= b))

    # Functions


    def visitSinFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.sin, math.sin)

    def visitCosFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.cos, math.cos)

    def visitTanFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.tan, math.tan)

    def visitAsinFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.asin, math.asin)

    def visitAcosFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.acos, math.acos)

    def visitAtanFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.atan, math.atan)

    def visitSinhFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.sinh, math.sinh)

    def visitCoshFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.cosh, math.cosh)

    def visitTanhFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.tanh, math.tanh)

    def visitAsinhFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.asinh, math.asinh)

    def visitAcoshFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.acosh, math.acosh)

    def visitAtanhFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.atanh, math.atanh)

    def visitAbsFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.abs, abs)

    def visitAbsExp(self, ctx):
        val = self.visit(ctx.expr())
        if self._is_list(val):
            return torch.linalg.norm(self._promote_to_tensor(val))
        if self._is_tensor(val):
            return torch.linalg.norm(val)
        return abs(val)

    def visitSqrtFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.sqrt, math.sqrt)

    def visitLnFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.log, math.log)

    def visitLogFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.log10, math.log10)

    def visitExpFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.exp, math.exp)

    def visitFloorFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.floor, math.floor)

    def visitCeilFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.ceil, math.ceil)

    def visitRoundFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.round, round)

    def visitSignFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.sign, lambda x: (1.0 if x > 0 else (-1.0 if x < 0 else 0.0)))

    def visitFractFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), lambda x: x - torch.floor(x), lambda x: x - math.floor(x))

    def visitGammaFunc(self, ctx):
        torch_gamma = getattr(torch.special, "gamma", None)
        if torch_gamma is None:
            torch_gamma = lambda x: torch.exp(torch.lgamma(x))
        return self._unary_op(self.visit(ctx.expr()), torch_gamma, math.gamma)

    def visitSigmoidFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.sigmoid, lambda x: 1.0 / (1.0 + math.exp(-x)))

    def visitReluFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.relu, lambda x: max(0.0, x))

    def visitSoftplusFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), F.softplus, lambda x: math.log(1.0 + math.exp(x)))

    def visitGeluFunc(self, ctx):
        return self._unary_op(
            self.visit(ctx.expr()), F.gelu, lambda x: 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * math.pow(x, 3))))
        )

    def visitAnglFunc(self, ctx):
        return self._unary_op(self.visit(ctx.expr()), torch.angle, lambda x: math.atan2(0, x) if x < 0 else 0)

    def visitPrintFunc(self, ctx):
        val = self.visit(ctx.expr())
        print(f"{val}")
        return val

    def visitTNormFunc(self, ctx):
        val = self.visit(ctx.expr())
        if self._is_tensor(val):
            return F.normalize(val, p=2, dim=-1)
        return 1.0 if val != 0 else 0.0

    def visitSNormFunc(self, ctx):
        val = self.visit(ctx.expr())
        if self._is_tensor(val):
            return torch.linalg.norm(val)
        return abs(val)

    # Two-argument functions
    def visitPowFunc(self, ctx):
        return self._bin_op(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), torch.pow, math.pow)

    def visitAtan2Func(self, ctx):
        return self._bin_op(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), torch.atan2, math.atan2)

    def visitTMinFunc(self, ctx):
        return self._bin_op(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), torch.minimum, min)

    def visitTMaxFunc(self, ctx):
        return self._bin_op(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), torch.maximum, max)

    def visitStepFunc(self, ctx):
        # step(x, edge) = 1 if x >= edge else 0
        return self._bin_op(
            self.visit(ctx.expr(0)),
            self.visit(ctx.expr(1)),
            lambda x, edge: torch.where(x >= edge, 1.0, 0.0),
            lambda x, edge: 1.0 if x >= edge else 0.0,
        )

    def visitTopkFunc(self, ctx):
        val = self.visit(ctx.expr(0))
        k = self.visit(ctx.expr(1))

        if self._is_tensor(k):
            k_val = int(k.flatten()[0].item())
        else:
            k_val = int(k)

        if self._is_tensor(val):
            size = val.shape[-1]
            k_val = max(1, min(k_val, size))
            score_val = val.abs() if torch.is_complex(val) else val

            _, indices = torch.topk(score_val, k=k_val, dim=-1)
            indices = indices.contiguous()
            mask = torch.zeros_like(score_val, dtype=torch.bool)
            mask.scatter_(dim=-1, index=indices, value=True)

            result = torch.where(mask, val, torch.zeros_like(val))
            return result.contiguous()

        if self._is_list(val):
            k_val = max(0, min(k_val, len(val)))
            try:
                return sorted(val, reverse=True)[:k_val]
            except:
                return val[:k_val]

        return val

    def visitBotkFunc(self, ctx):
        val = self.visit(ctx.expr(0))
        k = self.visit(ctx.expr(1))

        if self._is_tensor(k):
            k_val = int(k.flatten()[0].item())
        else:
            k_val = int(k)

        if self._is_tensor(val):
            size = val.shape[-1]
            k_val = max(1, min(k_val, size))
            score_val = val.abs() if torch.is_complex(val) else val

            _, indices = torch.topk(score_val, k=k_val, dim=-1, largest=False)
            indices = indices.contiguous()
            mask = torch.zeros_like(score_val, dtype=torch.bool)
            mask.scatter_(dim=-1, index=indices, value=True)

            result = torch.where(mask, val, torch.zeros_like(val))
            return result.contiguous()

        if self._is_list(val):
            k_val = max(0, min(k_val, len(val)))
            try:
                return sorted(val)[:k_val]
            except:
                return val[:k_val]

        return val

    def visitPinvFunc(self, ctx):
        """Permutation inverse: if input[i] = j, output[j] = i."""
        val = self.visit(ctx.expr())

        if self._is_list(val):
            n = len(val)
            result = [0] * n
            for i, v in enumerate(val):
                idx = int(v)
                if 0 <= idx < n:
                    result[idx] = i
            return result

        if self._is_tensor(val):
            val_list = val.flatten().tolist()
            n = len(val_list)
            result = [0] * n
            for i, v in enumerate(val_list):
                idx = int(v)
                if 0 <= idx < n:
                    result[idx] = i
            return torch.tensor(result, device=val.device, dtype=val.dtype).reshape(val.shape)

        return val

    # Three-argument functions
    def visitClampFunc(self, ctx):
        val = self.visit(ctx.expr(0))
        min_v = self.visit(ctx.expr(1))
        max_v = self.visit(ctx.expr(2))
        if any(self._is_tensor(x) for x in [val, min_v, max_v]):
            return torch.clamp(self._promote_to_tensor(val), self._promote_to_tensor(min_v), self._promote_to_tensor(max_v))
        if self._is_list(val):
            return [max(min(x, max_v), min_v) for x in val]  # TODO: what if min_v or max_v is list
        return max(min(val, max_v), min_v)

    def visitLerpFunc(self, ctx):
        a = self.visit(ctx.expr(0))
        b = self.visit(ctx.expr(1))
        w = self.visit(ctx.expr(2))
        if any(self._is_tensor(x) for x in [a, b, w]):
            # Lerp: a + w*(b-a)
            return torch.lerp(self._promote_to_tensor(a), self._promote_to_tensor(b), self._promote_to_tensor(w))
        return a*(1-w)+b*w

    def visitSmoothstepFunc(self, ctx):
        x = self.visit(ctx.expr(0))
        edge0 = self.visit(ctx.expr(1))
        edge1 = self.visit(ctx.expr(2))

        # t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
        # return t * t * (3.0 - 2.0 * t)

        if any(self._is_tensor(v) for v in [x, edge0, edge1]):
            x_t, e0_t, e1_t = self._promote_to_tensor(x), self._promote_to_tensor(edge0), self._promote_to_tensor(edge1)
            t = torch.clamp((x_t - e0_t) / (e1_t - e0_t), 0.0, 1.0)
            return t * t * (3.0 - 2.0 * t)

        t = max(0.0, min(1.0, (x - edge0) / (edge1 - edge0)))
        return t * t * (3.0 - 2.0 * t)

    def visitRangeFunc(self, ctx):
        return list(torch.arange(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.expr(2))))

    # Helpers for visiting generic exprs
    def visitFunc1Exp(self, ctx):
        return self.visitChildren(ctx)

    def visitFunc2Exp(self, ctx):
        return self.visitChildren(ctx)

    def visitFuncNExp(self, ctx):
        return self.visitChildren(ctx)

    def visitAtomExp(self, ctx):
        return self.visitChildren(ctx)

    def visitExpr(self, ctx):
        return self.visitChildren(ctx)

    def visitSMinFunc(self, ctx):
        vals = [self.visit(e) for e in ctx.expr()]

        if all(not self._is_tensor(x) and not self._is_list(x) for x in vals):
            return min(vals)

        promoted = [self._promote_to_tensor(x) for x in vals]
        if len(promoted) == 1:
            return torch.min(promoted[0])
        return torch.min(torch.stack(torch.broadcast_tensors(*promoted))).item()

    def visitSMaxFunc(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        if len(args) == 1:
            # Check if list or scalar
            if not self._is_tensor(args[0]) and not self._is_list(args[0]):
                return args[0]
            if self._is_list(args[0]):
                return max(args[0])  # max of list
            return torch.max(args[0]).item()  # Global max of single tensor

        # Multiple args
        if all(not self._is_tensor(x) and not self._is_list(x) for x in args):
            return max(args)

        promoted = [self._promote_to_tensor(x) for x in args]
        if len(promoted) == 1:
            return torch.max(promoted[0])
        return torch.max(torch.stack(torch.broadcast_tensors(*promoted)))

    def _fold_nd(self, tsr, spatial_dims):
        original_shape = tsr.shape
        added_dims = 0
        target_rank = spatial_dims + 2
        while tsr.ndim < target_rank:
            tsr = tsr.unsqueeze(1)
            added_dims += 1
        folded = False
        if tsr.ndim > target_rank:
            fold_count = tsr.ndim - target_rank
            new_batch = 1
            for i in range(fold_count + 1):
                new_batch *= tsr.shape[i]
            tsr = tsr.reshape(new_batch, *tsr.shape[fold_count + 1 :])
            folded = True
        else:
            folded = added_dims > 0
        return tsr, original_shape, added_dims, folded

    def _unfold_nd(self, tsr, original_shape, added_dims, folded):
        spatial_dims = tsr.ndim - 2
        if folded and added_dims == 0:
            target_fold_rank = len(original_shape) - (spatial_dims + 1)
            fold_dims = original_shape[:target_fold_rank]
            tsr = tsr.reshape(*fold_dims, *tsr.shape[1:])
        for _ in range(added_dims):
            if tsr.ndim > len(original_shape) and tsr.shape[1] == 1:
                tsr = tsr.squeeze(1)
        return tsr

    def visitPermuteFunc(self, ctx):
        tsr = self._promote_to_tensor(self.visit(ctx.expr(0)))
        dims = self.visit(ctx.expr(1))
        if isinstance(dims, torch.Tensor):
            dims = dims.flatten().long().tolist()
        return tsr.permute(*dims)

    def visitReshapeFunc(self, ctx):
        tsr = self._promote_to_tensor(self.visit(ctx.expr(0)))
        new_shape = self.visit(ctx.expr(1))
        if isinstance(new_shape, torch.Tensor):
            new_shape = new_shape.flatten().long().tolist()
        return tsr.reshape(*new_shape)

    def visitPrintShapeFunc(self, ctx):
        tsr = self.visit(ctx.expr())
        if hasattr(tsr, "shape"):
            print(tsr.shape)
        else:
            print(f"Scalar/List: {tsr}")
        return tsr

    def visitSfftFunc(self, ctx):
        old_vars = self.variables
        self.variables = self.spatial_variables.copy()
        try:
            val = self._promote_to_tensor(self.visit(ctx.expr()))
            dims = tuple(range(val.ndim))
            return torch.fft.fftn(val, dim=dims)
        finally:
            self.variables = old_vars

    def visitSifftFunc(self, ctx):
        old_vars = self.variables
        self.variables = self.variables.copy()
        device = self.device

        shape_to_use = self.shape if self.shape else (1, 1, 1, 1)

        ndim = len(shape_to_use)
        dim_names = ["x", "y", "z", "w", "v", "u"]

        k_components = []
        for i in range(ndim):
            dim_idx = ndim - 1 - i
            size_d = shape_to_use[dim_idx]
            values = torch.arange(size_d, dtype=torch.float32, device=device)
            view_shape = [1] * ndim
            view_shape[dim_idx] = size_d
            values = values.view(*view_shape).expand(*shape_to_use)

            if i < len(dim_names):
                var_name = f"K{dim_names[i]}"
                self.variables[var_name] = values
                self.variables[f"F{dim_names[i]}"] = float(size_d)

            self.variables[f"K_dim{dim_idx}"] = values
            self.variables[f"F_dim{dim_idx}"] = float(size_d)
            k_components.append(values)

        k_sq_sum = torch.zeros(shape_to_use, device=device)
        for k_val in k_components:
            k_sq_sum = k_sq_sum + k_val**2

        self.variables["K"] = torch.sqrt(k_sq_sum)
        self.variables["frequency"] = self.variables["K"]

        if "Kx" in self.variables:
            self.variables["frequency_count"] = self.variables.get("Fx", 1.0)

        self.variables = self.variables | generate_dim_variables(k_sq_sum)

        try:
            val = self._promote_to_tensor(self.visit(ctx.expr()))
            dims = tuple(range(val.ndim))
            return torch.fft.ifftn(val, dim=dims).real
        finally:
            self.variables = old_vars

    def visitSwapFunc(self, ctx):
        tsr = self._promote_to_tensor(self.visit(ctx.expr(0)))
        dim_t = self.visit(ctx.expr(1))
        idx1_t = self.visit(ctx.expr(2))
        idx2_t = self.visit(ctx.expr(3))

        dim = int(dim_t.flatten()[0].item()) if isinstance(dim_t, torch.Tensor) else int(dim_t)
        i = int(idx1_t.flatten()[0].item()) if isinstance(idx1_t, torch.Tensor) else int(idx1_t)
        j = int(idx2_t.flatten()[0].item()) if isinstance(idx2_t, torch.Tensor) else int(idx2_t)

        while dim < 0:
            dim += tsr.ndim
        while i < 0:
            i += tsr.shape[dim]
        while j < 0:
            j += tsr.shape[dim]

        indices = torch.arange(tsr.shape[dim], device=tsr.device)
        val_i = indices[i].clone()
        indices[i] = indices[j]
        indices[j] = val_i

        return torch.index_select(tsr, dim, indices)

    def _normalize_coord(self, coord, size):
        if size > 1:
            return (coord / (size - 1)) * 2.0 - 1.0
        return torch.zeros_like(coord)

    def visitSumFunc(self, ctx):
        return self._reduction_op(self.visit(ctx.expr()), torch.sum, sum)

    def visitMeanFunc(self, ctx):
        return self._reduction_op(
            self.visit(ctx.expr()), lambda x: torch.mean(x.float()), lambda x: sum(x) / len(x) if x else 0.0
        )

    def visitStdFunc(self, ctx):
        def list_std(val):
            if len(val) < 2:
                return 0.0
            mean = sum(val) / len(val)
            variance = sum((x - mean) ** 2 for x in val) / (len(val) - 1)
            return math.sqrt(variance)

        return self._reduction_op(self.visit(ctx.expr()), lambda x: torch.std(x.float()), list_std)

    def visitVarFunc(self, ctx):
        def list_var(val):
            if len(val) < 2:
                return 0.0
            mean = sum(val) / len(val)
            return sum((x - mean) ** 2 for x in val) / (len(val) - 1)

        return self._reduction_op(self.visit(ctx.expr()), lambda x: torch.var(x.float()), list_var)

    def _manual_quantile(self, val, q):
        """Fallback implementation using sort for when torch.quantile fails on large tensors."""
        val_flat = val.flatten().float()
        sorted_val, _ = torch.sort(val_flat)
        n = len(sorted_val)
        if n == 0:
            return torch.zeros_like(q) if self._is_tensor(q) else 0.0

        # indices = q * (n - 1)
        indices = q * (n - 1)
        low = torch.floor(indices).long()
        high = torch.ceil(indices).long()
        frac = (indices - low).float()

        # Ensure bounds
        low = torch.clamp(low, 0, n - 1)
        high = torch.clamp(high, 0, n - 1)

        res = sorted_val[low] + (sorted_val[high] - sorted_val[low]) * frac
        return res

    def _quartile_helper(self, val, q):

        if self._is_tensor(q) and not self._is_tensor(val):
            val = self._promote_to_tensor(val)

        if self._is_tensor(val):
            if not self._is_tensor(q):
                q = torch.tensor(q, device=self.device).float()

            try:
                if q.ndim > 1:
                    q_flat = q.flatten()
                    res = torch.quantile(val.float(), q_flat)
                    return res.reshape(q.shape)

                return torch.quantile(val.float(), q)
            except RuntimeError as e:
                # Fallback for "input tensor is too large" or other quantile-specific issues
                if "quantile" in str(e).lower() or "too large" in str(e).lower():
                    if q.ndim > 1:
                        q_flat = q.flatten()
                        res = self._manual_quantile(val, q_flat)
                        return res.reshape(q.shape)
                    return self._manual_quantile(val, q)
                raise e

        if self._is_list(val):
            if not val:
                return 0.0
            sorted_data = sorted(val)
            n = len(val)
            pos = (n - 1) * q
            whole = int(pos)
            frac = pos - whole
            if whole + 1 < n:
                return sorted_data[whole] + (sorted_data[whole + 1] - sorted_data[whole]) * frac
            else:
                return sorted_data[whole]
        return val

    def visitQuartileFunc(self, ctx):
        val = self.visit(ctx.expr(0))
        k = self.visit(ctx.expr(1))

        if self._is_tensor(k):
             # q = k * 0.25. Ensure k is treated as int-like (1,2,3)?
             # Old code did int().
             return self._quartile_helper(val, (k.int().float() * 0.25))
        if self._is_list(k):
            return [self._quartile_helper(val, int(x) * 0.25) for x in k]

        k_val = int(k)
        q = min(1.0, max(0.0, k_val * 0.25))
        return self._quartile_helper(val, q)

    def visitPercentileFunc(self, ctx):
        val = self.visit(ctx.expr(0))
        p_raw = self.visit(ctx.expr(1))

        if self._is_tensor(p_raw):
            # p is 0-100. q = p / 100
            return self._quartile_helper(val, p_raw.float() / 100.0)
        if self._is_list(p_raw):
            return [self._quartile_helper(val, float(x) / 100.0) for x in p_raw]

        p = float(p_raw)
        q = max(0.0, min(1.0, p / 100.0))
        return self._quartile_helper(val, q)

    def visitQuantileFunc(self, ctx):
        val = self.visit(ctx.expr(0))
        q_raw = self.visit(ctx.expr(1))

        if self._is_tensor(q_raw):
            return self._quartile_helper(val, q_raw.float())
        if self._is_list(q_raw):
            return [self._quartile_helper(val, float(x)) for x in q_raw]

        q = float(q_raw)
        q = max(0.0, min(1.0, q))
        return self._quartile_helper(val, q)

    def visitDotFunc(self, ctx):
        a = self._promote_to_tensor(self.visit(ctx.expr(0)))
        b = self._promote_to_tensor(self.visit(ctx.expr(1)))
        return torch.dot(a.flatten(), b.flatten())

    def visitMomentFunc(self,ctx):
        x = self._promote_to_tensor(self.visit(ctx.expr(0)))
        a = self.visit(ctx.expr(1))
        k = self.visit(ctx.expr(2))

        return torch.sum(self._bin_op(self._bin_op(x,a,torch.sub,lambda x, a: x - a),k,torch.pow,pow)).item()/x.numel()

    def visitSortFunc(self, ctx):
        val = self._promote_to_tensor(self.visit(ctx.expr()))
        sorted_val, _ = torch.sort(val)
        return sorted_val

    def visitCossimFunc(self, ctx):
        a = self._promote_to_tensor(self.visit(ctx.expr(0))).float()
        b = self._promote_to_tensor(self.visit(ctx.expr(1))).float()
        return F.cosine_similarity(a, b, dim=-1)

    def visitFlipFunc(self, ctx):
        val = self._promote_to_tensor(self.visit(ctx.expr(0)))
        dims = self.visit(ctx.expr(1))

        if self._is_list(dims):
            dims_tuple = tuple(int(x) for x in dims)
        elif self._is_tensor(dims):
            dims_tuple = tuple(dims.long().flatten().tolist())
        else:
            dims_tuple = (int(dims),)

        return torch.flip(val, dims_tuple)

    def visitCovFunc(self, ctx):
        x = self._promote_to_tensor(self.visit(ctx.expr(0))).float()
        y = self._promote_to_tensor(self.visit(ctx.expr(1))).float()

        x_flat = x.flatten()
        y_flat = y.flatten()

        if x_flat.numel() != y_flat.numel():
            raise ValueError("x and y must have the same number of elements")

        n = x_flat.numel()
        if n < 2:
            return torch.tensor(0.0, device=self.device)

        x_mean = torch.mean(x_flat)
        y_mean = torch.mean(y_flat)

        sum_sq_diff = torch.sum((x_flat - x_mean) * (y_flat - y_mean)).item()
        return sum_sq_diff / (n - 1)

    def visitMapFunc(self, ctx):
        tensor = self._promote_to_tensor(self.visit(ctx.expr(0)))
        coords = [self._promote_to_tensor(self.visit(ctx.expr(i))) for i in range(1, len(ctx.expr()))]
        num_coords = len(coords)

        if num_coords == 0:
            return tensor
        if num_coords > 3:
            raise ValueError("map() supports max 3 mapping functions.")

        spatial_in_shape = tensor.shape[-num_coords:]
        leading_shape = tensor.shape[:-num_coords]

        batch_size = 1
        for s in leading_shape:
            batch_size *= s

        input_view = tensor.reshape(batch_size, 1, *spatial_in_shape)
        norm_coords_list = []
        for i in range(num_coords):
            dim_size = spatial_in_shape[i]
            norm = self._normalize_coord(coords[i], dim_size)
            norm_coords_list.append(norm)

        grid = torch.stack(norm_coords_list[::-1], dim=-1)
        grid_spatial_shape = grid.shape[:-1]

        try:
            grid_view = grid.reshape(batch_size, *grid_spatial_shape[-(num_coords):], num_coords)
        except RuntimeError:
            grid_view = grid.expand(batch_size, *([-1] * len(grid_spatial_shape)), -1)
            grid_view = grid_view.reshape(batch_size, *grid_view.shape[-(num_coords + 1) : -1], num_coords)

        if num_coords == 1:
            input_final = input_view.reshape(batch_size, 1, 1, -1)
            gv = grid_view
            while gv.ndim < 3:
                gv = gv.unsqueeze(1)
            y_zeros = torch.zeros_like(gv[..., :1])
            grid_final = torch.cat([gv, y_zeros], dim=-1).unsqueeze(1)  # [B, 1, 1, 2]
            output = F.grid_sample(input_final, grid_final, align_corners=True)
        elif num_coords == 2:
            grid_final = grid_view.reshape(batch_size, *grid_view.shape[-3:-1], 2)
            output = F.grid_sample(input_view, grid_final, align_corners=True)
        else:
            grid_final = grid_view.reshape(batch_size, *grid_view.shape[-4:-1], 3)
            output = F.grid_sample(input_view, grid_final, align_corners=True)
        actual_spatial = grid_view.shape[1:-1]
        final_shape = list(leading_shape) + list(actual_spatial)
        return output.reshape(final_shape)

    def _parse_conv_args(self, ctx):
        input_raw = self.visit(ctx.expr(0))
        tensor = self._promote_to_tensor(input_raw)
        num_args = len(ctx.expr())
        if num_args < 3:
            raise ValueError("conv() requires at least 3 arguments")

        kernel_arg_idx = num_args - 1

        spatial_dims_count = num_args - 2
        if spatial_dims_count not in [1, 2, 3]:
            raise ValueError(f"conv() supports 1D, 2D, or 3D. Found {spatial_dims_count}")

        kernel_sizes = []
        for i in range(1, 1 + spatial_dims_count):
            val = self.visit(ctx.expr(i))
            if isinstance(val, torch.Tensor):
                val = int(val.flatten()[0].item())
            kernel_sizes.append(val)

        # Prepare context for kernel
        coords = [torch.arange(s, device=self.device).float() - (s // 2) for s in kernel_sizes]
        grid = torch.meshgrid(*coords, indexing="ij")

        dim_names = ["x", "y", "z"]
        old_vars = self.variables
        self.variables = self.variables.copy()
        for i in range(spatial_dims_count):
            self.variables[f"k{dim_names[i].lower()}"] = grid[i]
            self.variables[f"k{dim_names[i].upper()}"] = grid[i]

        kernel_var_names = ["kW", "kH", "kD"]
        kernel_var_full = ["kernel_width", "kernel_height", "kernel_depth"]
        for i in range(spatial_dims_count):
            size_val = float(kernel_sizes[i])
            self.variables[kernel_var_names[i]] = size_val
            self.variables[kernel_var_full[i]] = size_val

        original_shape = self.shape
        self.shape = tuple(kernel_sizes)

        try:
            kernel_val = self._promote_to_tensor(self.visit(ctx.expr(kernel_arg_idx)))
        finally:
            self.shape = original_shape
            self.variables = old_vars

        return tensor, kernel_val, kernel_sizes, spatial_dims_count

    def _apply_conv_internal(self, conv_input, kernel_val, kernel_sizes, spatial_dims_count):
        """
        Executes the convolution with asymmetric padding support for even kernels.
        Input: [Batch, Channel, Spatial...]
        Kernel: [Spatial...] (to be promoted/repeated)
        kernel_sizes: [W, H, D]
        """
        in_channels = conv_input.size(1)

        pads = []
        for k in kernel_sizes:
            p_total = k - 1
            p_low = k // 2
            p_high = p_total - p_low
            pads.extend([p_low, p_high])

        padded_input = torch.nn.functional.pad(conv_input, tuple(pads), mode="constant", value=0)

        actual_kernel_sizes = kernel_sizes[::-1]

        if kernel_val.numel() == 1:
            kernel_val = kernel_val.expand(tuple(actual_kernel_sizes))
        elif kernel_val.ndim != spatial_dims_count:
            kernel_val = kernel_val.reshape(tuple(actual_kernel_sizes))

        final_kernel = kernel_val.unsqueeze(0).unsqueeze(0)
        final_kernel = final_kernel.to(conv_input.dtype)
        final_kernel = final_kernel.repeat(in_channels, 1, *([1] * spatial_dims_count))

        conv_fn = F.conv1d if spatial_dims_count == 1 else (F.conv2d if spatial_dims_count == 2 else F.conv3d)

        result = conv_fn(padded_input, final_kernel, padding=0, groups=in_channels)
        return result

    def visitEzConvFunc(self, ctx):
        tensor, kernel_val, kernel_sizes, spatial_dims_count = self._parse_conv_args(ctx)
        input_ndim = tensor.ndim

        is_channels_first = False
        if tensor.ndim == spatial_dims_count + 2:
            c_front = tensor.shape[1]
            c_back = tensor.shape[-1]
            if c_front <= 4 and c_front < c_back:
                is_channels_first = True
            elif c_back <= 4 and c_back < c_front:
                is_channels_first = False
            else:
                is_channels_first = c_back > 4

        if is_channels_first:
            if spatial_dims_count == 1 and tensor.ndim == 3:
                tensor = tensor.permute(0, 2, 1)
            elif spatial_dims_count == 2 and tensor.ndim == 4:
                tensor = tensor.permute(0, 2, 3, 1)
            elif spatial_dims_count == 3:
                if tensor.ndim == 4:
                    tensor = tensor.unsqueeze(-1)
                elif tensor.ndim == 5:
                    tensor = tensor.permute(0, 2, 3, 4, 1)

        if tensor.ndim == spatial_dims_count + 1:
            tensor = tensor.unsqueeze(-1)  # Add C=1
        elif tensor.ndim == spatial_dims_count:
            tensor = tensor.unsqueeze(0).unsqueeze(-1)  # Add B=1, C=1

        in_channels = tensor.size(-1)
        batch_end_idx = tensor.ndim - 1 - spatial_dims_count
        batch_shape = tensor.shape[:batch_end_idx]
        spatial_shape = tensor.shape[batch_end_idx:-1]
        channels_shape = (tensor.shape[-1],)

        total_batch = 1
        for s in batch_shape:
            total_batch *= s
        flat_input = tensor.reshape(total_batch, *spatial_shape, in_channels)

        permute_order = [0, spatial_dims_count + 1] + list(range(1, spatial_dims_count + 1))
        conv_input = flat_input.permute(*permute_order)

        result = self._apply_conv_internal(conv_input, kernel_val, kernel_sizes, spatial_dims_count)

        result_permute = [0] + list(range(2, 2 + spatial_dims_count)) + [1]
        out_flat = result.permute(*result_permute)

        final_shape = batch_shape + spatial_shape + channels_shape
        out = out_flat.reshape(final_shape)

        if is_channels_first:
            if spatial_dims_count == 1 and out.ndim == 3:
                out = out.permute(0, 2, 1)
            elif spatial_dims_count == 2 and out.ndim == 4:
                out = out.permute(0, 3, 1, 2)
            elif spatial_dims_count == 3:
                if out.ndim == 5 and out.shape[-1] == 1 and input_ndim == 4:
                    out = out.squeeze(-1)
                elif out.ndim == 5:
                    out = out.permute(0, 4, 1, 2, 3)

        return out

    def visitConvFunc(self, ctx):
        tensor, kernel_val, kernel_sizes, spatial_dims_count = self._parse_conv_args(ctx)

        # Expect (Batch..., Channel, Spatial...)
        # spatial_dims_count = 1, 2, or 3
        # Must have at least Channel + Spatial dims
        min_dims = spatial_dims_count + 1
        if tensor.ndim < min_dims:
             raise ValueError(f"convolution() input requires at least Channels + Spatial dimensions. Got shape {tensor.shape} for {spatial_dims_count}D conv.")

        spatial_shape = tensor.shape[-spatial_dims_count:]
        in_channels = tensor.shape[-(spatial_dims_count + 1)]
        batch_shape = tensor.shape[:-(spatial_dims_count + 1)]

        total_batch = 1
        for s in batch_shape:
            total_batch *= s

        conv_input = tensor.reshape(total_batch, in_channels, *spatial_shape)

        result = self._apply_conv_internal(conv_input, kernel_val, kernel_sizes, spatial_dims_count)

        return result.reshape(*batch_shape, in_channels, *spatial_shape)

    def visitAppendFunc(self, ctx):
        a = self.visit(ctx.expr(0))
        b = self.visit(ctx.expr(1))
        if(self._is_tensor(a) and a.numel()==1):
            a = a.Item()
        if(self._is_tensor(b) and b.numel()==1):
            b = b.Item()
        if self._is_tensor(a) or self._is_tensor(b):
            a = self._promote_to_tensor(a,True)
            b = self._promote_to_tensor(b,True)
            if a.ndim == 0: a = a.unsqueeze(0)
            if b.ndim == 0: b = b.unsqueeze(0)
            return torch.cat((a, b), dim=0)
        if not self._is_list(a): a = [a]
        if not self._is_list(b): b = [b]
        return a + b

    def visitStart(self, ctx):
        # Visit all statements (function definitions)
        if ctx.funcDef():
            for i in range(len(ctx.funcDef())):
                self.visit(ctx.funcDef(i))

        if ctx.varDef():
            for i in range(len(ctx.varDef())):
                self.visit(ctx.varDef(i))

        return self.visit(ctx.expr())

    def visitVarDef(self, ctx):
        var_name = ctx.VARIABLE().getText()
        var_value = self.visit(ctx.expr())
        self.variables[var_name] = var_value
        return {var_name: var_value}


    def visitFunctionDef(self, ctx):
        func_name = ctx.VARIABLE().getText()
        params = []
        if ctx.paramList():
            params = [node.getText() for node in ctx.paramList().VARIABLE()]

        self.functions[func_name] = {
            "params": params,
            "body": ctx.expr()
        }
        return None

    def visitCallExp(self, ctx):
        func_name = ctx.VARIABLE().getText()

        # Check if it is a user-defined function
        if func_name in self.functions:
            func_def = self.functions[func_name]
            params = func_def["params"]

            # Evaluate arguments
            args = []
            if ctx.exprList():
                args = [self.visit(e) for e in ctx.exprList().expr()]

            if len(args) != len(params):
                raise ValueError(f"Function '{func_name}' expects {len(params)} arguments, got {len(args)}")

            # Create a new scope for function execution
            new_vars = self.variables.copy()
            for param, arg in zip(params, args):
                new_vars[param] = arg

            # Create a new visitor to execute the function body in the new scope - easier than managing stack of variables and call stack
            visitor = UnifiedMathVisitor(new_vars, self.shape, self.device, self.functions)
            return visitor.visit(func_def["body"])

        raise ValueError(f"Unknown function: {func_name}")

    def visitNoiseFunc(self,ctx):
        seed = int(self.visit(ctx.expr()))
        generator = torch.Generator(device=self.device).manual_seed(seed)
        return torch.randn(self.shape, generator=generator, device=self.device)

    def visitRandFunc(self, ctx):
        seed = int(self.visit(ctx.expr()))
        generator = torch.Generator(device=self.device).manual_seed(seed)
        return torch.rand(self.shape, generator=generator, device=self.device)

    def visitExponentialFunc(self, ctx):
        seed = int(self.visit(ctx.expr(0)))
        lambd = float(self.visit(ctx.expr(1)))
        generator = torch.Generator(device=self.device).manual_seed(seed)
        return torch.empty(self.shape, device=self.device).exponential_(lambd, generator=generator)

    def visitCauchyFunc(self, ctx):
        seed = int(self.visit(ctx.expr(0)))
        median = float(self.visit(ctx.expr(1)))
        sigma = float(self.visit(ctx.expr(2)))
        generator = torch.Generator(device=self.device).manual_seed(seed)
        return torch.empty(self.shape, device=self.device).cauchy_(median, sigma, generator=generator)

    def visitLogNormalFunc(self, ctx):
        seed = int(self.visit(ctx.expr(0)))
        mean = float(self.visit(ctx.expr(1)))
        std = float(self.visit(ctx.expr(2)))
        generator = torch.Generator(device=self.device).manual_seed(seed)
        return torch.empty(self.shape, device=self.device).log_normal_(mean, std, generator=generator)

    def visitBernoulliFunc(self, ctx):
        seed = int(self.visit(ctx.expr(0)))
        p = self.visit(ctx.expr(1))
        generator = torch.Generator(device=self.device).manual_seed(seed)
        if self._is_tensor(p):
            return torch.bernoulli(p, generator=generator).to(device=self.device)
        return torch.bernoulli(torch.full(self.shape, p, device=self.device), generator=generator)

    def visitPoissonFunc(self, ctx):
        seed = int(self.visit(ctx.expr(0)))
        lam = self.visit(ctx.expr(1))
        generator = torch.Generator(device=self.device).manual_seed(seed)
        if self._is_tensor(lam):
            return torch.poisson(lam, generator=generator).to(device=self.device)
        return torch.poisson(torch.full(self.shape, lam, device=self.device), generator=generator)