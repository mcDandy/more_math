import time
import torch
import math
import inspect
import torch.nn.functional as F
from .MathExprVisitor import MathExprVisitor
from ..helper_functions import generate_dim_variables


class ReturnSignal:
    __slots__ = ("value",)
    def __init__(self, value):
        self.value = value

class BreakSignal:
    pass

class ContinueSignal:
    pass

class UnifiedMathVisitor(MathExprVisitor):
    def __init__(self, variables, shape=None, device=None, functions=None, depth=0, state_storage=None):

        self.variables = variables
        self.spatial_variables = variables.copy()
        self.shape = shape if shape is not None else (1,)
        if device is None:
            self.device = next((v.device for v in variables.values() if isinstance(v, torch.Tensor)), torch.device("cpu"))
        else:
            self.device = device
        self.functions = functions if functions is not None else {}
        self.depth = depth
        self._scope_stack = []
        self._state_storage = state_storage if state_storage is not None else {}

    def visit(self, tree):
        if tree is None:
            return None

        gen = tree.accept(self)
        if not inspect.isgenerator(gen):
            return gen

        stack = [gen]
        last_result = None

        while stack:
            try:
                # If we're bubbling a signal, we need to check if the parent can handle it.
                if isinstance(last_result, (ReturnSignal, BreakSignal, ContinueSignal)):
                    parent_gen = stack[-1]
                    func_name = parent_gen.gi_code.co_name

                    is_handler = False
                    if isinstance(last_result, (BreakSignal, ContinueSignal)):
                        if func_name in ("visitWhileStmt", "visitForStmt"):
                            is_handler = True
                    elif isinstance(last_result, ReturnSignal):
                        if func_name in ("visitCallExp", "visitStart"):
                            is_handler = True

                    if not is_handler:
                        stack.pop().close()
                        continue

                res = stack[-1].send(last_result)

                if hasattr(res, 'accept'):
                    next_gen = res.accept(self)
                    if inspect.isgenerator(next_gen):
                        stack.append(next_gen)
                        last_result = None
                    else:
                        last_result = next_gen
                else:
                    last_result = res

            except StopIteration as e:
                stack.pop()
                last_result = e.value

        if isinstance(last_result, ReturnSignal):
            return last_result.value
        return last_result
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
        if self._is_tensor(a) and a.numel() == 1:
            a = float(a.flatten()[0].item())
        if self._is_tensor(b) and b.numel() == 1:
            b = float(b.flatten()[0].item())

        # one of them is a list and one is tensor
        if self._is_tensor(a) and self._is_list(b):
             if(a.shape[0]==len(b)):
                A = torch.split(a,1)
                return torch.cat([self._bin_op(x, y, torch_op, scalar_op) for x,y in zip(A,b)],dim=0)
             return torch.cat([self._bin_op(a, x, torch_op, scalar_op) for x in b], dim=0)
        if self._is_list(a) and self._is_tensor(b):
            if(b.shape[0]==len(a)):
                B = torch.split(b,1)
                return torch.cat([self._bin_op(x, y, torch_op, scalar_op) for x,y in zip(a,B)],dim=0)
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
        if self._is_tensor(a) and a.numel() == 1:
            a = float(a.flatten()[0].item())

        if self._is_list(a):
            return [self._unary_op(x, torch_op, scalar_op) for x in a]
        if self._is_tensor(a):
            return torch_op(a).contiguous() if torch_op else scalar_op(a)
        return scalar_op(a)

    def _reduction_op(self, val, torch_op, list_op):
        # If it's a scalar tensor, return Python float to avoid 0-dim tensor propagation
        if self._is_tensor(val):
            if val.numel() == 1:
                return float(val.flatten()[0].item())
            return torch_op(val)
        if self._is_list(val):
            return list_op(val)
        return val

    # ========================
    # Visitors
    # ========================

    def visitNumberExp(self, ctx):
        return float(ctx.NUMBER().getText())

    def visitConstantExp(self, ctx):
        val = ctx.CONSTANT().getText().lower()
        if val == "pi":
            return math.pi
        if val == "e":
            return math.e
        return 0.0

    def visitVariableExp(self, ctx):
        var_name = ctx.VARIABLE().getText()
        if var_name == "depth":
            return float(self.depth)
        if var_name in self.variables:
            res = self.variables[var_name]
            return res
        raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Variable '{var_name}' not found")

    def visitListExp(self, ctx):
        res = []
        for e in ctx.expr():
            res.append((yield e))
        return res

    def visitParenExp(self, ctx):
        return (yield ctx.expr())

    def visitNoneExp(self, ctx):
        return None

    def visitUnaryPlus(self, ctx):
        return self._unary_op((yield ctx.unaryExpr()), lambda x: x, lambda x: +x)

    def visitUnaryMinus(self, ctx):
        return self._unary_op((yield ctx.unaryExpr()), torch.neg, lambda x: -x)

    def visitToIndex(self, ctx):
        return (yield ctx.indexExpr())

    def visitIndexExp(self, ctx):
        val = (yield ctx.indexExpr())
        index_args = []
        for e in ctx.expr():
            index_args.append((yield e))

        if self._is_tensor(val):

            if len(index_args) == 1 and (self._is_list(index_args[0]) or self._is_tensor(index_args[0])):
                idx = index_args[0]
                if self._is_tensor(idx): idx = idx.flatten().tolist()
                flat_indices = [int(i + val.shape[0] if i < 0 else i) for i in idx]
                idx_tensor = torch.tensor(flat_indices, device=self.device, dtype=torch.long)
                return torch.index_select(val, 0, idx_tensor).contiguous()

            # Tuple indexing
            torch_indices = []
            for idx in index_args:
                if self._is_list(idx):
                    torch_indices.append(torch.tensor(idx, device=self.device, dtype=torch.long))
                elif self._is_tensor(idx):
                    torch_indices.append(idx.long())
                else:
                    torch_indices.append(int(idx))

            res = val[tuple(torch_indices)]
            if isinstance(res, torch.Tensor):
                if res.numel() == 1 and res.ndim == 0:
                    return float(res.item())
                return res.contiguous()
            return float(res)

        elif self._is_list(val):
            # Nested list indexing or selection
            if len(index_args) > 1:
                curr = val
                for idx in index_args:
                    curr = curr[int(idx + len(curr) if idx < 0 else idx)]
                return curr

            idx = index_args[0]
            if self._is_list(idx) or self._is_tensor(idx):
                if self._is_tensor(idx): idx = idx.flatten().tolist()
                return [val[int(i + len(val) if i < 0 else i)] for i in idx]
            else:
                return val[int(idx + len(val) if idx < 0 else idx)]
        else:
            raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Indexing only supported on tensors and lists.")

    def visitToAtom(self, ctx):
        return (yield ctx.atom())

    def visitTernaryExp(self, ctx):
        condition = yield ctx.compExpr()

        if self._is_tensor(condition):
            true_val = yield ctx.expr(0)
            false_val = yield ctx.expr(1)
            true_t = self._promote_to_tensor(true_val)
            false_t = self._promote_to_tensor(false_val)

            if true_t.dtype != false_t.dtype:
                true_t = true_t.float()
                false_t = false_t.float()

            cond_t = torch.isclose(condition.float(), torch.tensor(0.0, device=self.device)) == False
            return torch.where(cond_t, true_t, false_t).contiguous()

        if self._is_list(condition):
            res = []
            cache_true = None
            cache_false = None
            for i, c in enumerate(condition):
                if c:
                    if cache_true is None:
                        cache_true = yield ctx.expr(0)
                    res.append(cache_true)
                else:
                    if cache_false is None:
                        cache_false = yield ctx.expr(1)
                    res.append(cache_false)
            return res

        if condition:
            return (yield ctx.expr(0))
        else:
            return (yield ctx.expr(1))

    # Binary Ops
    def visitAddExp(self, ctx):
        a = yield ctx.addExpr()
        b = yield ctx.mulExpr()
        return self._bin_op(a, b, torch.add, lambda a, b: a + b)

    def visitSubExp(self, ctx):
        a = yield ctx.addExpr()
        b = yield ctx.mulExpr()
        return self._bin_op(a, b, torch.sub, lambda a, b: a - b)

    def visitMulExp(self, ctx):
        a = yield ctx.mulExpr()
        b = yield ctx.powExpr()
        return self._bin_op(a, b, torch.mul, lambda a, b: a * b)

    def visitDivExp(self, ctx):
        a = yield ctx.mulExpr()
        b = yield ctx.powExpr()
        return self._bin_op(a, b, torch.div, lambda a, b: a / b)

    def visitModExp(self, ctx):
        a = yield ctx.mulExpr()
        b = yield ctx.powExpr()
        return self._bin_op(a, b, torch.remainder, lambda a, b: a % b)

    def visitPowExp(self, ctx):
        a = yield ctx.unaryExpr()
        b = yield ctx.powExpr()
        return self._bin_op(a, b, torch.pow, lambda a, b: a ** b)

    def _bool_op(self, a, b, torch_op, scalar_op):
        return self._bin_op(a, b, torch_op, scalar_op)

    def visitNeExp(self, ctx):
        a = yield ctx.compExpr()
        b = yield ctx.addExpr()
        return self._bool_op(a, b, torch.ne, lambda a, b: a != b)

    def visitEqExp(self, ctx):
        a = yield ctx.compExpr()
        b = yield ctx.addExpr()
        return self._bool_op(a, b, torch.eq, lambda a, b: a == b)

    def visitGtExp(self, ctx):
        a = yield ctx.compExpr()
        b = yield ctx.addExpr()
        return self._bool_op(a, b, torch.gt, lambda a, b: a > b)

    def visitLtExp(self, ctx):
        a = yield ctx.compExpr()
        b = yield ctx.addExpr()
        return self._bool_op(a, b, torch.lt, lambda a, b: a < b)

    def visitGeExp(self, ctx):
        a = yield ctx.compExpr()
        b = yield ctx.addExpr()
        return self._bool_op(a, b, torch.ge, lambda a, b: a >= b)

    def visitLeExp(self, ctx):
        a = yield ctx.compExpr()
        b = yield ctx.addExpr()
        return self._bool_op(a, b, torch.le, lambda a, b: a <= b)

    def visitToAdd(self, ctx):
        return (yield ctx.addExpr())

    def visitToMul(self, ctx):
        return (yield ctx.mulExpr())

    def visitToPow(self, ctx):
        return (yield ctx.powExpr())

    def visitToUnary(self, ctx):
        return (yield ctx.unaryExpr())

    # Functions
    def visitTimestampFunc(self, ctx):
        return time.time();

    def visitSinFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.sin, math.sin)

    def visitCosFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.cos, math.cos)

    def visitTanFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.tan, math.tan)

    def visitAsinFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.asin, math.asin)

    def visitAcosFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.acos, math.acos)

    def visitAtanFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.atan, math.atan)

    def visitSinhFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.sinh, math.sinh)

    def visitCoshFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.cosh, math.cosh)

    def visitTanhFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.tanh, math.tanh)

    def visitAsinhFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.asinh, math.asinh)

    def visitAcoshFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.acosh, math.acosh)

    def visitAtanhFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.atanh, math.atanh)

    def visitAbsFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.abs, abs)

    def visitAbsExp(self, ctx):
        val = (yield ctx.expr())
        if self._is_list(val):
            return torch.linalg.norm(self._promote_to_tensor(val))
        if self._is_tensor(val):
            return torch.linalg.norm(val)
        return abs(val)

    def visitSqrtFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.sqrt, math.sqrt)

    def visitLnFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.log, math.log)

    def visitLogFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.log10, math.log10)

    def visitExpFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.exp, math.exp)

    def visitFloorFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.floor, math.floor)

    def visitCeilFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.ceil, math.ceil)

    def visitRoundFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.round, round)

    def visitSignFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.sign, lambda x: (1.0 if x > 0 else (-1.0 if x < 0 else 0.0)))

    def visitFractFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), lambda x: x - torch.floor(x), lambda x: x - math.floor(x))

    def visitGammaFunc(self, ctx):
        torch_gamma = getattr(torch.special, "gamma", None)
        if torch_gamma is None:
            torch_gamma = lambda x: torch.exp(torch.lgamma(x))
        return self._unary_op((yield ctx.expr()), torch_gamma, math.gamma)

    def visitSigmoidFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.sigmoid, lambda x: 1.0 / (1.0 + math.exp(-x)))

    def visitReluFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.relu, lambda x: max(0.0, x))

    def visitSoftplusFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), F.softplus, lambda x: math.log(1.0 + math.exp(x)))

    def visitGeluFunc(self, ctx):
        return self._unary_op(
            (yield ctx.expr()), F.gelu, lambda x: 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * math.pow(x, 3))))
        )

    def visitAnglFunc(self, ctx):
        return self._unary_op((yield ctx.expr()), torch.angle, lambda x: math.atan2(0, x) if x < 0 else 0)

    def visitPrintFunc(self, ctx):
        val = (yield ctx.expr())
        print(f"{val}")
        return val

    def visitTNormFunc(self, ctx):
        val = (yield ctx.expr())
        if self._is_tensor(val):
            return F.normalize(val, p=2, dim=-1)
        return 1.0 if val != 0 else 0.0

    def visitSNormFunc(self, ctx):
        val = (yield ctx.expr())
        if self._is_tensor(val):
            return torch.linalg.norm(val)
        return abs(val)

    # Two-argument functions
    def visitPowFunc(self, ctx):
        return self._bin_op((yield ctx.expr(0)), (yield ctx.expr(1)), torch.pow, math.pow)

    def visitAtan2Func(self, ctx):
        return self._bin_op((yield ctx.expr(0)), (yield ctx.expr(1)), torch.atan2, math.atan2)

    def visitTMinFunc(self, ctx):
        return self._bin_op((yield ctx.expr(0)), (yield ctx.expr(1)), torch.minimum, min)

    def visitTMaxFunc(self, ctx):
        return self._bin_op((yield ctx.expr(0)), (yield ctx.expr(1)), torch.maximum, max)

    def visitStepFunc(self, ctx):
        # step(x, edge) = 1 if x >= edge else 0
        return self._bin_op(
            (yield ctx.expr(0)),
            (yield ctx.expr(1)),
            lambda x, edge: torch.where(x >= edge, 1.0, 0.0),
            lambda x, edge: 1.0 if x >= edge else 0.0,
        )

    def visitTopkFunc(self, ctx):
        val = (yield ctx.expr(0))
        k = (yield ctx.expr(1))

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
        val = (yield ctx.expr(0))
        k = (yield ctx.expr(1))

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
        val = (yield ctx.expr())

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

    def visitGetValueFunc(self, ctx):
        var = yield ctx.expr(0)
        pos_list = yield ctx.expr(1)

        if not self._is_tensor(var):
             raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: get_value expects a tensor as first argument")

        if not self._is_list(pos_list) and not self._is_tensor(pos_list):
            pos_list = [pos_list]

        if self._is_tensor(pos_list):
             pos_list = pos_list.tolist()

        if len(pos_list) != var.ndim:
             raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Position list length {len(pos_list)} does not match tensor dimensions {var.ndim}")

        shape = var.shape
        c_strides = [1] * var.ndim
        if var.ndim > 0:
            for i in range(var.ndim - 2, -1, -1):
                c_strides[i] = c_strides[i+1] * shape[i+1]

        offset = 0
        for i, p in enumerate(pos_list):
            idx = int(p)
            if idx < 0 or idx >= shape[i]:
                 raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Index {idx} out of bounds for dimension {i} with size {shape[i]}")
            offset += idx * c_strides[i]

        return var.contiguous().flatten()[offset]

    def visitBatchShuffleFunc(self, ctx):
        tsr_val = yield ctx.expr(0)
        idx_val = yield ctx.expr(1)

        tsr = self._promote_to_tensor(tsr_val)

        if self._is_tensor(idx_val):
            indices = idx_val.long()
        elif self._is_list(idx_val):
            indices = torch.tensor([int(float(x)) for x in idx_val], dtype=torch.long, device=tsr.device)
        else:
            indices = torch.tensor([int(float(idx_val))], dtype=torch.long, device=tsr.device)

        # Check bounds
        max_idx = tsr.size(0)
        if torch.any(indices < 0) or torch.any(indices >= max_idx):
             raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Batch index out of bounds (0-{max_idx-1})")

        return tsr[indices]

    # Three-argument functions
    def visitClampFunc(self, ctx):
        val = (yield ctx.expr(0))
        min_v = (yield ctx.expr(1))
        max_v = (yield ctx.expr(2))
        if any(self._is_tensor(x) for x in [val, min_v, max_v]):
            return torch.clamp(self._promote_to_tensor(val), self._promote_to_tensor(min_v), self._promote_to_tensor(max_v))
        if self._is_list(val):
            return [max(min(x, max_v), min_v) for x in val]  # TODO: what if min_v or max_v is list
        return max(min(val, max_v), min_v)

    def visitLerpFunc(self, ctx):
        a = (yield ctx.expr(0))
        b = (yield ctx.expr(1))
        w = (yield ctx.expr(2))

        if self._is_list(w):
             return [self._lerp_helper(a[i] if self._is_list(a) else a,
                                      b[i] if self._is_list(b) else b,
                                      t) for i, t in enumerate(w)]

        return self._lerp_helper(a, b, w)

    def _lerp_helper(self, a, b, w):
        if any(self._is_tensor(x) for x in [a, b, w]) or any(self._is_list(x) for x in [a, b, w]):
             return torch.lerp(self._promote_to_tensor(a), self._promote_to_tensor(b), self._promote_to_tensor(w))
        return a*(1-w)+b*w

    def visitSmoothstepFunc(self, ctx):
        x = (yield ctx.expr(0))
        edge0 = (yield ctx.expr(1))
        edge1 = (yield ctx.expr(2))

        # t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
        # return t * t * (3.0 - 2.0 * t)

        if any(self._is_tensor(v) for v in [x, edge0, edge1]):
            x_t, e0_t, e1_t = self._promote_to_tensor(x), self._promote_to_tensor(edge0), self._promote_to_tensor(edge1)
            t = torch.clamp((x_t - e0_t) / (e1_t - e0_t), 0.0, 1.0)
            return t * t * (3.0 - 2.0 * t)

        t = max(0.0, min(1.0, (x - edge0) / (edge1 - edge0)))
        return t * t * (3.0 - 2.0 * t)

    def visitRangeFunc(self, ctx):
        s = (yield ctx.expr(0))
        e = (yield ctx.expr(1))
        st = (yield ctx.expr(2))
        arr = torch.arange(s, e, st, device=self.device, dtype=torch.float32)
        return [float(x) for x in arr.tolist()]

    def visitSmootherstepFunc(self, ctx):
        x = (yield ctx.expr(0))
        edge0 = (yield ctx.expr(1))
        edge1 = (yield ctx.expr(2))

        def smoother(t):
            return 6*t**5 - 15*t**4 + 10*t**3

        if any(self._is_tensor(v) for v in [x, edge0, edge1]):
            x_t, e0_t, e1_t = self._promote_to_tensor(x), self._promote_to_tensor(edge0), self._promote_to_tensor(edge1)
            t = torch.clamp((x_t - e0_t) / (e1_t - e0_t), 0.0, 1.0)
            return smoother(t)

        t = max(0.0, min(1.0, (x - edge0) / (edge1 - edge0)))
        return smoother(t)

    def visitCropFunc(self, ctx):
        inp = yield ctx.expr(0)
        pos_list = yield ctx.expr(1)
        size_list = yield ctx.expr(2)

        inp = self._promote_to_tensor(inp)

        def to_int_list(x):
             if self._is_list(x): return [int(v) for v in x]
             if self._is_tensor(x): return x.int().tolist()
             return [int(x)]

        p_l = to_int_list(pos_list)
        s_l = to_int_list(size_list)

        if len(p_l) != inp.ndim or len(s_l) != inp.ndim:
             # Basic safety fallback if dims don't match, though robust logic might handle slices properly if we truncate?
             # Let's enforce or just take first N?
             # For robustness, we'll assume user provides correct dims or we raise error?
             # Given "lists described in get_value" implies stricter checking.
             if len(p_l) != inp.ndim: raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: crop: position dim {len(p_l)} != input dim {inp.ndim}")
             if len(s_l) != inp.ndim: raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: crop: size dim {len(s_l)} != input dim {inp.ndim}")

        out_tensor = torch.zeros(tuple(s_l), dtype=inp.dtype, device=inp.device)

        slices_in = []
        slices_out = []

        valid_intersection = True

        for i in range(inp.ndim):
            start = p_l[i]
            length = s_l[i]
            end = start + length

            in_start = max(0, start)
            in_end = min(inp.shape[i], end)

            if in_start >= in_end:
                 valid_intersection = False
                 break

            slices_in.append(slice(in_start, in_end))

            out_start = in_start - start
            out_len = in_end - in_start
            slices_out.append(slice(out_start, out_start + out_len))

        if valid_intersection:
            out_tensor[tuple(slices_out)] = inp[tuple(slices_in)]

        return out_tensor

    def visitCubicEaseFunc(self, ctx):
        a, b, t = (yield ctx.expr(0)), (yield ctx.expr(1)), (yield ctx.expr(2))
        def cubic(v):
             return torch.where(v < 0.5, 4 * v**3, 1 - torch.pow(-2 * v + 2, 3) / 2) if self._is_tensor(v) else \
                    (4 * v**3 if v < 0.5 else 1 - math.pow(-2 * v + 2, 3) / 2)
        return self._lerp_helper(a, b, cubic(t))

    def visitSineEaseFunc(self, ctx):
        a, b, t = (yield ctx.expr(0)), (yield ctx.expr(1)), (yield ctx.expr(2))
        def sine(v):
             return -(torch.cos(math.pi * v) - 1) / 2 if self._is_tensor(v) else -(math.cos(math.pi * v) - 1) / 2
        return self._lerp_helper(a, b, sine(t))

    def visitElasticEaseFunc(self, ctx):
        a, b, t = (yield ctx.expr(0)), (yield ctx.expr(1)), (yield ctx.expr(2))
        # Specific elastic formula (simplified InOut)
        def elastic(v):
             c4 = (2 * math.pi) / 3
             if self._is_tensor(v):
                 return torch.where(v <= 0, 0, torch.where(v >= 1, 1,
                        torch.where(v < 0.5, -(torch.pow(2, 20 * v - 10) * torch.sin((20 * v - 11.125) * c4)) / 2,
                                     (torch.pow(2, -20 * v + 10) * torch.sin((20 * v - 11.125) * c4)) / 2 + 1)))
             if v <= 0: return 0
             if v >= 1: return 1
             if v < 0.5: return -(math.pow(2, 20 * v - 10) * math.sin((20 * v - 11.125) * c4)) / 2
             return (math.pow(2, -20 * v + 10) * math.sin((20 * v - 11.125) * c4)) / 2 + 1
        return self._lerp_helper(a, b, elastic(t))

    # Helpers for visiting generic exprs
    def visitFunc1Exp(self, ctx):
        res = yield ctx.getChild(0)
        return res

    def visitFunc2Exp(self, ctx):
        res = yield ctx.getChild(0)
        return res

    def visitFuncNExp(self, ctx):
        res = yield ctx.getChild(0)
        return res

    def visitAtomExp(self, ctx):
        res = yield ctx.getChild(0)
        return res

    def visitExpr(self, ctx):
        res = yield ctx.getChild(0)
        return res

    def visitSMinFunc(self, ctx):
        vals = []
        for e in ctx.expr():
            vals.append((yield e))

        if all(not self._is_tensor(x) and not self._is_list(x) for x in vals):
            return min(vals)

        promoted = [self._promote_to_tensor(x) for x in vals]
        if len(promoted) == 1:
            return torch.min(promoted[0])
        return torch.min(torch.stack(torch.broadcast_tensors(*promoted))).item()

    def visitSMaxFunc(self, ctx):
        args = []
        for e in ctx.expr():
            args.append((yield e))
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
        tsr = self._promote_to_tensor((yield ctx.expr(0)))
        dims = (yield ctx.expr(1))
        if isinstance(dims, torch.Tensor):
            dims = dims.flatten().long().tolist()
        return tsr.permute(*dims)

    def visitReshapeFunc(self, ctx):
        tsr = self._promote_to_tensor((yield ctx.expr(0)))
        new_shape = (yield ctx.expr(1))
        if isinstance(new_shape, torch.Tensor):
            new_shape = new_shape.flatten().long().tolist()
        return tsr.reshape(*new_shape)

    def visitPrintShapeFunc(self, ctx):
        tsr = (yield ctx.expr())
        if hasattr(tsr, "shape"):
            print(tsr.shape)
        else:
            print(f"Scalar/List: {tsr}")
        return tsr

    def visitSfftFunc(self, ctx):
        old_vars = self.variables
        self.variables = self.spatial_variables.copy()
        try:
            val = self._promote_to_tensor((yield ctx.expr()))
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
            val = self._promote_to_tensor((yield ctx.expr()))
            dims = tuple(range(val.ndim))
            return torch.fft.ifftn(val, dim=dims).real
        finally:
            self.variables = old_vars

    def visitSwapFunc(self, ctx):
        tsr = self._promote_to_tensor((yield ctx.expr(0)))
        dim_t = (yield ctx.expr(1))
        idx1_t = (yield ctx.expr(2))
        idx2_t = (yield ctx.expr(3))

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
        return self._reduction_op((yield ctx.expr()), torch.sum, sum)

    def visitCountFunc(self, ctx):
        val = yield ctx.expr()
        if self._is_list(val):
            return float(len(val))
        if self._is_tensor(val):
            if val.ndim == 0:
                return 1.0
            return float(val.size(0))
        return 1.0

    def visitMeanFunc(self, ctx):
        return self._reduction_op(
            (yield ctx.expr()), lambda x: torch.mean(x.float()), lambda x: sum(x) / len(x) if x else 0.0
        )

    def visitStdFunc(self, ctx):
        def list_std(val):
            if len(val) < 2:
                return 0.0
            mean = sum(val) / len(val)
            variance = sum((x - mean) ** 2 for x in val) / (len(val) - 1)
            return math.sqrt(variance)

        return self._reduction_op((yield ctx.expr()), lambda x: torch.std(x.float()), list_std)

    def visitVarFunc(self, ctx):
        def list_var(val):
            if len(val) < 2:
                return 0.0
            mean = sum(val) / len(val)
            return sum((x - mean) ** 2 for x in val) / (len(val) - 1)

        return self._reduction_op((yield ctx.expr()), lambda x: torch.var(x.float()), list_var)

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
        val = (yield ctx.expr(0))
        k = (yield ctx.expr(1))

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
        val = (yield ctx.expr(0))
        p_raw = (yield ctx.expr(1))

        if self._is_tensor(p_raw):
            # p is 0-100. q = p / 100
            # p is 0-100. q = p / 100
            return self._quartile_helper(val, p_raw.float() / 100.0)
        if self._is_list(p_raw):
            return [self._quartile_helper(val, float(x) / 100.0) for x in p_raw]

        p = float(p_raw)
        q = max(0.0, min(1.0, p / 100.0))
        return self._quartile_helper(val, q)

    def visitQuantileFunc(self, ctx):
        val = (yield ctx.expr(0))
        q_raw = (yield ctx.expr(1))

        if self._is_tensor(q_raw):
            return self._quartile_helper(val, q_raw.float())
        if self._is_list(q_raw):
            return [self._quartile_helper(val, float(x)) for x in q_raw]

        q = float(q_raw)
        q = max(0.0, min(1.0, q))
        return self._quartile_helper(val, q)

    def visitDotFunc(self, ctx):
        a = self._promote_to_tensor((yield ctx.expr(0)))
        b = self._promote_to_tensor((yield ctx.expr(1)))
        return torch.dot(a.flatten(), b.flatten())

    def visitMomentFunc(self,ctx):
        x = self._promote_to_tensor((yield ctx.expr(0)))
        a = (yield ctx.expr(1))
        k = (yield ctx.expr(2))

        return torch.sum(self._bin_op(self._bin_op(x,a,torch.sub,lambda x, a: x - a),k,torch.pow,pow)).item()/x.numel()

    def visitSortFunc(self, ctx):
        val = self._promote_to_tensor((yield ctx.expr()))
        sorted_val, _ = torch.sort(val)
        return sorted_val

    def visitCossimFunc(self, ctx):
        a = self._promote_to_tensor((yield ctx.expr(0))).float()
        b = self._promote_to_tensor((yield ctx.expr(1))).float()
        return F.cosine_similarity(a, b, dim=-1)

    def visitFlipFunc(self, ctx):
        val = self._promote_to_tensor((yield ctx.expr(0)))
        dims = (yield ctx.expr(1))

        if self._is_list(dims):
            dims_tuple = tuple(int(x) for x in dims)
        elif self._is_tensor(dims):
            dims_tuple = tuple(dims.long().flatten().tolist())
        else:
            dims_tuple = (int(dims),)

        return torch.flip(val, dims_tuple)

    def visitCovFunc(self, ctx):
        x = self._promote_to_tensor((yield ctx.expr(0))).float()
        y = self._promote_to_tensor((yield ctx.expr(1))).float()

        x_flat = x.flatten()
        y_flat = y.flatten()

        if x_flat.numel() != y_flat.numel():
            raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: x and y must have the same number of elements")

        n = x_flat.numel()
        if n < 2:
            return torch.tensor(0.0, device=self.device)

        x_mean = torch.mean(x_flat)
        y_mean = torch.mean(y_flat)

        sum_sq_diff = torch.sum((x_flat - x_mean) * (y_flat - y_mean)).item()
        return sum_sq_diff / (n - 1)

    def visitMapFunc(self, ctx):
        tensor = self._promote_to_tensor((yield ctx.expr(0)))
        coords = []
        for i in range(1, len(ctx.expr())):
            coords.append(self._promote_to_tensor((yield ctx.expr(i))))
        num_coords = len(coords)

        if num_coords == 0:
            return tensor
        if num_coords > 3:
            raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: map() supports max 3 mapping functions.")

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
        input_raw = (yield ctx.expr(0))
        tensor = self._promote_to_tensor(input_raw)
        num_args = len(ctx.expr())
        if num_args < 3:
            raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: conv() requires at least 3 arguments")

        kernel_arg_idx = num_args - 1

        spatial_dims_count = num_args - 2
        if spatial_dims_count not in [1, 2, 3]:
            raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: conv() supports 1D, 2D, or 3D. Found {spatial_dims_count}")

        kernel_sizes = []
        for i in range(1, 1 + spatial_dims_count):
            val = (yield ctx.expr(i))
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
            kernel_val = self._promote_to_tensor((yield ctx.expr(kernel_arg_idx)))
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
        tensor, kernel_val, kernel_sizes, spatial_dims_count = (yield from self._parse_conv_args(ctx))
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
        tensor, kernel_val, kernel_sizes, spatial_dims_count = (yield from self._parse_conv_args(ctx))

        # Expect (Batch..., Channel, Spatial...)
        # spatial_dims_count = 1, 2, or 3
        # Must have at least Channel + Spatial dims
        min_dims = spatial_dims_count + 1
        if tensor.ndim < min_dims:
             raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: convolution() input requires at least Channels + Spatial dimensions. Got shape {tensor.shape} for {spatial_dims_count}D conv.")

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
        a = (yield ctx.expr(0))
        b = (yield ctx.expr(1))

        if a is None:
            return b
        if b is None:
            return a

        if self._is_tensor(a) and a.numel() == 1:
            a = a.item()
        if self._is_tensor(b) and b.numel() == 1:
            b = b.item()

        if self._is_tensor(a) or self._is_tensor(b):
            if self._is_tensor(a) and not self._is_tensor(b):
                b_tensor = torch.tensor(b, device=self.device, dtype=a.dtype)
                if a.ndim > 0:
                    target_shape = [1] + list(a.shape[1:])
                    b = b_tensor.expand(target_shape).contiguous()
                else:
                    b = b_tensor
            elif not self._is_tensor(a) and self._is_tensor(b):
                a_tensor = torch.tensor(a, device=self.device, dtype=b.dtype)
                if b.ndim > 0:
                    target_shape = [1] + list(b.shape[1:])
                    a = a_tensor.expand(target_shape).contiguous()
                else:
                    a = a_tensor
            else:
                a = self._promote_to_tensor(a)
                b = self._promote_to_tensor(b)

            # Ensure at least 1D for cat
            if a.ndim == 0:
                a = a.unsqueeze(0)
            if b.ndim == 0:
                b = b.unsqueeze(0)

            return torch.cat((a, b), dim=0)

        if not self._is_list(a):
            a = [a]
        if not self._is_list(b):
            b = [b]
        return a + b

    def visitStart(self, ctx):
        from antlr4.tree.Tree import TerminalNode
        count = ctx.getChildCount()
        last_res = None

        for i in range(count):
            child = ctx.getChild(i)
            if isinstance(child, TerminalNode):
                continue

            res = yield child
            if res is not None:
                last_res = res

        return last_res

    def visitExprStatement(self, ctx):
        res = yield ctx.expr()
        return res

    def visitVarDefStmt(self, ctx):
        res = yield ctx.varDef()
        return res

    def visitBlockStatement(self, ctx):
        res = yield ctx.block()
        return res

    def visitBlock(self, ctx):
        vars_before = set(self.variables.keys())
        try:
            val = None
            for stmt in ctx.stmt():
                val = yield stmt
            return val
        finally:
            for v in set(self.variables.keys()) - vars_before:
                del self.variables[v]

    def visitIfStatement(self, ctx):
        return (yield ctx.ifStmt())

    def visitIfStmt(self, ctx):
        cond = yield ctx.expr()

        def truthy(x):
            if isinstance(x, torch.Tensor):
                return torch.any(x != 0).item()
            if isinstance(x, (list, tuple)):
                return any(x)
            return bool(x)

        if truthy(cond):
            return (yield ctx.stmt(0))
        elif ctx.stmt(1):
            return (yield ctx.stmt(1))
        return None

    def visitWhileStmt(self, ctx):
        while True:
            cond = yield ctx.expr()
            is_true = (
                torch.any(cond != 0).item() if isinstance(cond, torch.Tensor)
                else any(cond) if isinstance(cond, (list, tuple))
                else bool(cond)
            )

            if not is_true:
                break

            res = yield ctx.stmt()

            if isinstance(res, ReturnSignal):
                return res
            if isinstance(res, BreakSignal):
                break
            if isinstance(res, ContinueSignal):
                continue
        return None

    def visitForStmt(self, ctx):
        var_name = ctx.VARIABLE().getText()
        iterable = yield ctx.expr()

        iterator = []
        if self._is_tensor(iterable):
            if iterable.ndim == 0:
                iterator = [iterable]
            else:
                iterator = iterable
        elif self._is_list(iterable):
            iterator = iterable
        else:
            iterator = [iterable]

        for val in iterator:
            self.variables[var_name] = val
            res = yield ctx.stmt()

            if isinstance(res, BreakSignal):
                break
            if isinstance(res, ContinueSignal):
                continue
        return None

    def visitBreakStmt(self, ctx):
        return BreakSignal()

    def visitContinueStmt(self, ctx):
        return ContinueSignal()

    def visitReturnStatement(self, ctx):
        res = yield ctx.returnStmt()
        return res

    def visitReturnStmt(self, ctx):
        val = (yield ctx.expr()) if ctx.expr() else None
        return ReturnSignal(val)

    def visitVarDef(self, ctx):
        var_name = ctx.VARIABLE().getText()
        expr_list = ctx.expr()

        if not ctx.LBRACKET():
            # Standard assignment: x = value
            val = yield expr_list[0]
            self.variables[var_name] = val
            return val

        # Indexed assignment: x[i, j...] = value
        # The last expression is the value to assign
        val_expr = expr_list[-1]
        assigned_val = yield val_expr

        # Evaluate indices
        indices = []
        for i in range(len(expr_list) - 1):
            indices.append((yield expr_list[i]))

        if var_name not in self.variables:
            raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Variable '{var_name}' not found for indexed assignment.")

        target = self.variables[var_name]

        if self._is_tensor(target):
            # Process indices for PyTorch
            torch_indices = []
            for idx in indices:
                if self._is_list(idx):
                    torch_indices.append(torch.tensor(idx, device=self.device, dtype=torch.long))
                elif self._is_tensor(idx):
                    torch_indices.append(idx.long())
                else:
                    torch_indices.append(int(idx))

            idx_tuple = tuple(torch_indices)
            val_t = self._promote_to_tensor(assigned_val)

            try:
                # Target slice - used to compute expected shape
                target_slice = target[idx_tuple]

                # Squeeze leading ones to match target slice rank if it's smaller
                # but target_slice.ndim might be 0 if it's a scalar location.
                while val_t.ndim > target_slice.ndim and val_t.shape[0] == 1:
                    val_t = val_t.squeeze(0)

                target[idx_tuple] = val_t
                return assigned_val
            except Exception as e:
                raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Indexed assignment to '{var_name}' failed: {str(e)}")

        elif self._is_list(target):
            # Recurse through nested lists if multiple indices provided
            curr = target
            for idx in indices[:-1]:
                curr = curr[int(idx + len(curr) if idx < 0 else idx)]
            last_idx = int(indices[-1])
            curr[last_idx + len(curr) if last_idx < 0 else last_idx] = assigned_val
            return assigned_val
        else:
            raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Indexed assignment not supported for {type(target)}")


    def visitFunctionDef(self, ctx):
        func_name = ctx.VARIABLE().getText()
        params = []
        if ctx.paramList():
            params = [node.getText() for node in ctx.paramList().VARIABLE()]

        self.functions[func_name] = {
            "params": params,
            "body": ctx.block() if ctx.block() else ctx.expr()
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
                for e in ctx.exprList().expr():
                    args.append((yield e))

            if len(args) != len(params):
                raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Function '{func_name}' expects {len(params)} arguments, got {len(args)}"
                )

            # Create a new scope for function execution
            new_vars = self.variables.copy()
            for param, arg in zip(params, args):
                new_vars[param] = arg

            # Push current variables to scope stack
            self._scope_stack.append(self.variables)

            # Update variables and depth
            self.variables = new_vars
            self.depth += 1
            self.variables["depth"] = float(self.depth)

            try:
                # Visit the body using yield (trampoline will handle it)
                res = yield func_def["body"]
                if isinstance(res, ReturnSignal):
                    return res.value

                return res

            finally:
                # Restore variables and depth
                self.variables = self._scope_stack.pop()
                self.depth -= 1

        raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Unknown function: {func_name}")

    def visitNoiseFunc(self,ctx):
        seed_val = yield ctx.expr()
        seed = int(seed_val.item()) if self._is_tensor(seed_val) else int(seed_val)
        generator = torch.Generator(device=self.device).manual_seed(seed)
        return torch.randn(self.shape, generator=generator, device=self.device)

    def visitRandFunc(self, ctx):
        seed_val = yield ctx.expr()
        seed = int(seed_val.item()) if self._is_tensor(seed_val) else int(seed_val)
        generator = torch.Generator(device=self.device).manual_seed(seed)
        return torch.rand(self.shape, generator=generator, device=self.device)

    def visitExponentialFunc(self, ctx):
        seed_val = yield ctx.expr(0)
        seed = int(seed_val.item()) if self._is_tensor(seed_val) else int(seed_val)
        lambd_val = yield ctx.expr(1)
        lambd = float(lambd_val.item()) if self._is_tensor(lambd_val) else float(lambd_val)
        generator = torch.Generator(device=self.device).manual_seed(seed)
        return torch.empty(self.shape, device=self.device).exponential_(lambd, generator=generator)

    def visitCauchyFunc(self, ctx):
        seed_val = yield ctx.expr(0)
        seed = int(seed_val.item()) if self._is_tensor(seed_val) else int(seed_val)
        median_val = yield ctx.expr(1)
        median = float(median_val.item()) if self._is_tensor(median_val) else float(median_val)
        sigma_val = yield ctx.expr(2)
        sigma = float(sigma_val.item()) if self._is_tensor(sigma_val) else float(sigma_val)
        generator = torch.Generator(device=self.device).manual_seed(seed)
        return torch.empty(self.shape, device=self.device).cauchy_(median, sigma, generator=generator)

    def visitLogNormalFunc(self, ctx):
        seed_val = yield ctx.expr(0)
        seed = int(seed_val.item()) if self._is_tensor(seed_val) else int(seed_val)
        mean_val = yield ctx.expr(1)
        mean = float(mean_val.item()) if self._is_tensor(mean_val) else float(mean_val)
        std_val = yield ctx.expr(2)
        std = float(std_val.item()) if self._is_tensor(std_val) else float(std_val)
        generator = torch.Generator(device=self.device).manual_seed(seed)
        return torch.empty(self.shape, device=self.device).log_normal_(mean, std, generator=generator)

    def visitBernoulliFunc(self, ctx):
        seed_val = yield ctx.expr(0)
        seed = int(seed_val.item()) if self._is_tensor(seed_val) else int(seed_val)
        p = yield ctx.expr(1)
        generator = torch.Generator(device=self.device).manual_seed(seed)
        if self._is_tensor(p):
            return torch.bernoulli(p, generator=generator).to(device=self.device)
        return torch.bernoulli(torch.full(self.shape, p, device=self.device), generator=generator)

    def visitPoissonFunc(self, ctx):
        seed_val = yield ctx.expr(0)
        seed = int(seed_val.item()) if self._is_tensor(seed_val) else int(seed_val)
        lam = yield ctx.expr(1)
        generator = torch.Generator(device=self.device).manual_seed(seed)
        if self._is_tensor(lam):
            return torch.poisson(lam, generator=generator).to(device=self.device)
        return torch.poisson(torch.full(self.shape, lam, device=self.device), generator=generator)

    def visitNvlFunc(self, ctx):
        v = yield ctx.expr(0)
        v1 = yield ctx.expr(1)
        v2 = yield ctx.expr(2)
        v3 = yield ctx.expr(3)
        return torch.nan_to_num(self._promote_to_tensor(v), v1, v2, v3)

    def visitAnyFunc(self, ctx):
        val = yield ctx.expr()
        if self._is_tensor(val): return torch.any(torch.isclose(val, torch.tensor(0.0, device=self.device)) == False).float()
        if self._is_list(val): return float(any(val))
        return float(bool(val))

    def visitAllFunc(self, ctx):
        val = yield ctx.expr()
        if self._is_tensor(val): return torch.all(torch.isclose(val, torch.tensor(0.0, device=self.device)) == False).float()
        if self._is_list(val): return float(all(val))
        return float(bool(val))

    def visitMedianFunc(self, ctx):
        val = yield ctx.expr()
        if self._is_tensor(val): return torch.median(val.float())
        if self._is_list(val): return sorted(val)[len(val)//2]
        return val

    def visitModeFunc(self, ctx):
        val = yield ctx.expr()
        if self._is_tensor(val): return torch.mode(val.float().flatten()).values
        if self._is_list(val):
             from collections import Counter
             return Counter(val).most_common(1)[0][0]
        return val

    def visitCumsumFunc(self, ctx):
        val = self._promote_to_tensor((yield ctx.expr()))
        return torch.cumsum(val, dim=0)

    def visitCumprodFunc(self, ctx):
        val = self._promote_to_tensor((yield ctx.expr()))
        return torch.cumprod(val, dim=0)

    def visitTopkIndFunc(self, ctx):
        val = self._promote_to_tensor((yield ctx.expr(0)))
        k_val = yield ctx.expr(1)
        k = int(k_val.item()) if self._is_tensor(k_val) else int(k_val)
        return torch.topk(val.flatten(), k=min(k, val.numel()), largest=True).indices

    def visitBotkIndFunc(self, ctx):
        val = self._promote_to_tensor((yield ctx.expr(0)))
        k_val = yield ctx.expr(1)
        k = int(k_val.item()) if self._is_tensor(k_val) else int(k_val)
        return torch.topk(val.flatten(), k=min(k, val.numel()), largest=False).indices

    def _apply_spatial_op(self, tsr, op_fn, original_shape):
        """
        Helper to handle spatial operations on different layouts.
        Detects [B, H, W, C], [B, C, H, W], [B, H, W], and [H, W, C].
        """
        ndim = tsr.ndim
        if ndim < 2: return tsr

        layout = "unknown"
        if ndim == 4:
            # Heuristic: BHWC vs BCHW
            # If last dim is 1, 3, or 4 and much smaller than first/middle dims, likely BHWC
            c_last = original_shape[3]
            if c_last <= 4 and c_last < original_shape[1] and c_last < original_shape[2]:
                tsr = tsr.permute(0, 3, 1, 2)
                layout = "bhwc"
            else:
                # Assume BCHW
                layout = "bchw"
        elif ndim == 3:
            # Heuristic: [B, H, W] (Mask) or [H, W, C] (Image)?
            c_last = original_shape[2]
            if c_last <= 4 and c_last < original_shape[0] and c_last < original_shape[1]:
                # image [H, W, C] -> [1, C, H, W]
                tsr = tsr.permute(2, 0, 1).unsqueeze(0)
                layout = "hwc"
            else:
                # mask [B, H, W] -> [B, 1, H, W]
                tsr = tsr.unsqueeze(1)
                layout = "bhw"
        elif ndim == 2:
            # [H, W] -> [1, 1, H, W]
            tsr = tsr.unsqueeze(0).unsqueeze(0)
            layout = "hw"

        res = op_fn(tsr)

        # Restore layout
        if layout == "bhwc":
            return res.permute(0, 2, 3, 1)
        elif layout == "bchw":
            return res
        elif layout == "hwc":
            return res.squeeze(0).permute(1, 2, 0)
        elif layout == "bhw":
            return res.squeeze(1)
        elif layout == "hw":
            return res.squeeze(0).squeeze(0)
        return res

    def visitEdgeFunc(self, ctx):
        tsr_val = yield ctx.expr(0)
        tsr = self._promote_to_tensor(tsr_val)
        original_shape = tsr.shape
        tsr = tsr.float()

        reshap = False
        if len(ctx.expr()) >= 2:
            reshap_val = yield ctx.expr(1)
            reshap = bool(reshap_val.item()) if self._is_tensor(reshap_val) else bool(reshap_val)

        def sobel_op(x):
            kx = torch.tensor([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], device=x.device, dtype=x.dtype)
            ky = torch.tensor([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], device=x.device, dtype=x.dtype)
            gx = self._apply_conv_internal(x, kx, [3, 3], 2)
            gy = self._apply_conv_internal(x, ky, [3, 3], 2)
            return torch.sqrt(gx**2 + gy**2)

        return self._apply_spatial_op(tsr, sobel_op, original_shape) if reshap else sobel_op(tsr)

    def visitGaussianFunc(self, ctx):
        tsr_val = yield ctx.expr(0)
        tsr = self._promote_to_tensor(tsr_val)

        sigma_val = yield ctx.expr(1)
        sigma = float(sigma_val.item()) if self._is_tensor(sigma_val) else float(sigma_val)

        if sigma <= 0: return tsr
        original_shape = tsr.shape
        tsr = tsr.float()
        reshap = False
        if len(ctx.expr()) >= 3:
            reshap_val = yield ctx.expr(2)
            reshap = bool(reshap_val.item()) if self._is_tensor(reshap_val) else bool(reshap_val)
        def blur_op(x):
            kernel_size = int(6 * sigma + 1)
            if kernel_size % 2 == 0: kernel_size += 1
            coords = torch.linspace(-kernel_size//2, kernel_size//2, kernel_size, device=x.device)
            kernel = torch.exp(-coords**2 / (2 * sigma**2))
            kernel = kernel / kernel.sum()


            kh = kernel.view(1, kernel_size)
            x_h = self._apply_conv_internal(x, kh, [kernel_size, 1], 2)

            kv = kernel.view(kernel_size, 1)
            return self._apply_conv_internal(x_h, kv, [1, kernel_size], 2)

        return self._apply_spatial_op(tsr, blur_op, original_shape) if reshap else blur_op(tsr)

    def visitDistFunc(self, ctx):
        x1 = yield ctx.expr(0)
        y1 = yield ctx.expr(1)
        x2 = yield ctx.expr(2)
        y2 = yield ctx.expr(3)
        res_sq = (x2-x1)**2 + (y2-y1)**2
        if self._is_tensor(res_sq):
            return torch.sqrt(res_sq)
        return math.sqrt(res_sq)

    def visitRemapFunc(self, ctx):
        v = yield ctx.expr(0)
        i_min = yield ctx.expr(1)
        i_max = yield ctx.expr(2)
        o_min = yield ctx.expr(3)
        o_max = yield ctx.expr(4)
        epsilon = 1.0e-10
        denom = (i_max - i_min)
        if self._is_tensor(denom):
            denom = torch.where(denom == 0, torch.fill(denom,epsilon), denom)
        elif self._is_list(denom):
            denom = [epsilon if d == 0 else d for d in denom]
            return [o_min + (vi - i_min) * (o_max - o_min) / di for vi, di in zip(v, denom)]
        elif denom == 0:
            denom = epsilon

        return o_min + (v - i_min) * (o_max - o_min) / denom

    def _ensure_dict_storage(self):
        if not isinstance(self._state_storage, dict):
             if not self._state_storage:
                 self._state_storage = {}
             else:
                 self._state_storage = {i: v for i, v in enumerate(self._state_storage)}

    def visitPushFunc(self, ctx):
        self._ensure_dict_storage()
        f= yield ctx.expr(0)
        slot = int(f)
        if slot not in self._state_storage:
            self._state_storage[slot] = []
        value = yield ctx.expr(1)
        self._state_storage[slot].append(value)
        print(self._state_storage.keys())
        return value

    def visitPopFunc(self, ctx):
        self._ensure_dict_storage()
        slot = int((yield ctx.expr()))
        if slot not in self._state_storage or not self._state_storage[slot]:
            raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Pop from empty slot: {slot}")
        return self._state_storage[slot].pop()

    def visitClearFunc(self, ctx):
        self._ensure_dict_storage()
        slot = int((yield ctx.expr()))
        print(self._state_storage.keys())
        if slot in self._state_storage:
            self._state_storage[slot] = []
        return None

    def visitHasFunc(self, ctx):
        self._ensure_dict_storage()
        slot = int((yield ctx.expr()))
        return float(slot in self._state_storage and bool(self._state_storage[slot]))

    def visitGetFunc(self, ctx):
        self._ensure_dict_storage()
        slot = int((yield ctx.expr()))
        if slot not in self._state_storage:
            raise ValueError(f"{ctx.VARIABLE().getPayload().line}:{ctx.VARIABLE().getPayload().column}: Get from empty slot: {slot}")
        storage_list = self._state_storage[slot]
        return storage_list[-1] if storage_list else None

    def visitBreakExp(self, ctx):
        return BreakSignal()

    def visitContinueExp(self, ctx):
        return ContinueSignal()

    def visitEmptyTensorFunc(self, ctx):
        value = (yield ctx.expr()) if ctx.expr() else 0.0
        shape_val = yield ctx.indexExpr()

        if self._is_tensor(shape_val):
            shape = shape_val.int().tolist()
        elif self._is_list(shape_val):
            shape = [int(float(x)) for x in shape_val]
        else:
            shape = [int(float(shape_val))]

        return torch.full(shape, value, device=self.device)
