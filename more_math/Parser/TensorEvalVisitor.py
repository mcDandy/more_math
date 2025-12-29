import torch
import torch.special

from .MathExprVisitor import MathExprVisitor
from ..helper_functions import generate_dim_variables

class TensorEvalVisitor(MathExprVisitor):
    def __init__(self, variables, shape, device=None):
        self.variables = variables
        self.spatial_variables = variables.copy()
        self.shape = shape
        # Infer device from variables if not provided
        if device is None:
             self.device = next((v.device for v in variables.values() if isinstance(v, torch.Tensor)), torch.device("cpu"))
        else:
             self.device = device

    def _fold_nd(self, tsr, spatial_dims):
        # Ensure tensor has rank (spatial_dims + 2)
        # 1. Unsqueeze if too low rank (add dummy channel at dim 1)
        original_shape = tsr.shape
        added_dims = 0
        target_rank = spatial_dims + 2

        while tsr.ndim < target_rank:
            tsr = tsr.unsqueeze(1)
            added_dims += 1

        # 2. Fold leading dimensions into batch if too high rank
        folded = False
        if tsr.ndim > target_rank:
            fold_count = tsr.ndim - target_rank
            new_batch = 1
            for i in range(fold_count + 1):
                new_batch *= tsr.shape[i]
            tsr = tsr.reshape(new_batch, *tsr.shape[fold_count+1:])
            folded = True
        else:
            folded = (added_dims > 0)

        return tsr, original_shape, added_dims, folded

    def _unfold_nd(self, tsr, original_shape, added_dims, folded):
        spatial_dims = tsr.ndim - 2
        # Restore folded batch if any
        if folded and added_dims == 0:
            target_fold_rank = len(original_shape) - (spatial_dims + 1)
            fold_dims = original_shape[:target_fold_rank]
            tsr = tsr.reshape(*fold_dims, *tsr.shape[1:])

        # Squeeze added dims (dummy channels)
        for _ in range(added_dims):
            if tsr.ndim > len(original_shape) and tsr.shape[1] == 1:
                tsr = tsr.squeeze(1)

        return tsr

    def visitPermuteFunc(self, ctx):
        tsr = self.visit(ctx.expr(0))
        # permute(tsr, [d1, d2, ...]) or permute(tsr, d1, d2, ...)
        # Actually FuncN grammar was not used for permute but it could be.
        # Let's check the grammar. I added `PERM '(' expr ',' expr ')'` which is Func2 style.
        # But for permute we need a list.
        dims = self.visit(ctx.expr(1))
        if isinstance(dims, torch.Tensor):
             dims = dims.flatten().long().tolist()
        return tsr.permute(*dims)

    def visitReshapeFunc(self, ctx):
        tsr = self.visit(ctx.expr(0))
        new_shape = self.visit(ctx.expr(1))
        if isinstance(new_shape, torch.Tensor):
             new_shape = new_shape.flatten().long().tolist()
        return tsr.reshape(*new_shape)

    def visitNumberExp(self, ctx):
        return torch.full(self.shape,float(ctx.getText()), device=self.device)

    def visitConstantExp(self, ctx):
        name = ctx.getText().lower()
        if name == "pi":
            return torch.full(self.shape, 3.141592653589793, device=self.device)
        if name == "e":
            return torch.full(self.shape, 2.718281828459045, device=self.device)
        raise ValueError(f"Unknown constant: {name}")

    def visitVariableExp(self, ctx):
        name = ctx.getText()
        if name not in self.variables:
            raise ValueError(f"Variable '{name}' not found")
        val = self.variables[name]
        if not isinstance(val, torch.Tensor):
             return torch.tensor(float(val), device=self.device)
        return val

    def visitParenExp(self, ctx):
        return self.visit(ctx.expr())

    def visitUnaryPlus(self, ctx):
        return +self.visit(ctx.unaryExpr())

    def visitUnaryMinus(self, ctx):
        return -self.visit(ctx.unaryExpr())


    def visitAddExp(self, ctx):
        return torch.add(self.visit(ctx.addExpr()), self.visit(ctx.mulExpr()))

    def visitSubExp(self, ctx):
        return torch.sub(self.visit(ctx.addExpr()), self.visit(ctx.mulExpr()))

    def visitMulExp(self, ctx):
        return torch.mul(self.visit(ctx.mulExpr()), self.visit(ctx.powExpr()))

    def visitDivExp(self, ctx):
        return torch.div(self.visit(ctx.mulExpr()), self.visit(ctx.powExpr()))


    def visitModExp(self, ctx):
        return torch.fmod(self.visit(ctx.mulExpr()), self.visit(ctx.powExpr()))

    def visitPowExp(self, ctx):
        return torch.pow(self.visit(ctx.unaryExpr()), self.visit(ctx.powExpr()))

    def visitToUnary(self, ctx):
        return self.visit(ctx.unaryExpr())

    def visitToPow(self, ctx):
        return self.visit(ctx.powExpr())

    def visitToMul(self, ctx):
        return self.visit(ctx.mulExpr())

    def visitToAdd(self, ctx):
        return self.visit(ctx.addExpr())

    def visitToAnd(self, ctx):
        return self.visit(ctx.andExpr())

    def visitToXor(self, ctx):
        return self.visit(ctx.xorExpr())

    def visitOrExp(self, ctx):
        return torch.logical_or(self.visit(ctx.orExpr()).bool(), self.visit(ctx.xorExpr()).bool())

    def visitXorExp(self, ctx):
        return torch.pow(self.visit(ctx.xorExpr()), self.visit(ctx.andExpr()))

    def visitAndExp(self, ctx):
        return torch.logical_and(self.visit(ctx.andExpr()).bool(), self.visit(ctx.addExpr()).bool())

    def visitNeExp(self, ctx):
        return torch.ne(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()
    def visitEqExp(self, ctx):
        return torch.eq(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()
    def visitGtExp(self, ctx):
        return torch.gt(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()
    def visitLtExp(self, ctx):
        return torch.lt(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()
    def visitGeExp(self, ctx):
        return torch.ge(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()
    def visitLeExp(self, ctx):
        return torch.le(self.visit(ctx.compExpr()), self.visit(ctx.addExpr())).float()

    # Single-argument functions
    def visitSinFunc(self, ctx):   return torch.sin(self.visit(ctx.expr()))
    def visitCosFunc(self, ctx):   return torch.cos(self.visit(ctx.expr()))
    def visitTanFunc(self, ctx):   return torch.tan(self.visit(ctx.expr()))
    def visitAsinFunc(self, ctx):  return torch.asin(self.visit(ctx.expr()))
    def visitAcosFunc(self, ctx):  return torch.acos(self.visit(ctx.expr()))
    def visitAtanFunc(self, ctx):  return torch.atan(self.visit(ctx.expr()))
    def visitSinhFunc(self, ctx):  return torch.sinh(self.visit(ctx.expr()))
    def visitCoshFunc(self, ctx):  return torch.cosh(self.visit(ctx.expr()))
    def visitTanhFunc(self, ctx):  return torch.tanh(self.visit(ctx.expr()))
    def visitAsinhFunc(self, ctx): return torch.asinh(self.visit(ctx.expr()))
    def visitAcoshFunc(self, ctx): return torch.acosh(self.visit(ctx.expr()))
    def visitAtanhFunc(self, ctx): return torch.atanh(self.visit(ctx.expr()))
    def visitAbsFunc(self, ctx):   return torch.abs(self.visit(ctx.expr()))
    def visitAbsExp(self, ctx):    return torch.abs(self.visit(ctx.expr()))

    def visitListExp(self, ctx):
        vals = [self.visit(e) for e in ctx.expr()]
        # If any are tensors with shape, stack them or create a tensor
        if all(v.ndim == 0 for v in vals):
             return torch.tensor([v.item() for v in vals], device=self.device)
        else:
             # Broadcasting stack
             return torch.stack(torch.broadcast_tensors(*vals), dim=0)

    def visitNormExp(self, ctx):   return torch.linalg.norm(self.visit(ctx.expr()))
    def visitSqrtFunc(self, ctx):  return torch.sqrt(self.visit(ctx.expr()))
    def visitLnFunc(self, ctx):    return torch.log(self.visit(ctx.expr()))
    def visitLogFunc(self, ctx):   return torch.log10(self.visit(ctx.expr()))
    def visitExpFunc(self, ctx):   return torch.exp(self.visit(ctx.expr()))
    def visitTNormFunc(self, ctx): return torch.nn.functional.normalize(self.visit(ctx.expr()), p=2, dim=-1)
    def visitSNormFunc(self, ctx): return torch.full(self.shape, torch.linalg.norm(self.visit(ctx.expr())).data[0], device=self.device)
    def visitFloorFunc(self, ctx): return torch.floor(self.visit(ctx.expr()))
    def visitCeilFunc(self, ctx):  return torch.ceil(self.visit(ctx.expr()))
    def visitRoundFunc(self, ctx): return torch.round(self.visit(ctx.expr()))
    def visitGammaFunc(self, ctx): return torch.special.gamma(self.visit(ctx.expr())).exp()
    def visitSigmoidFunc(self, ctx): return torch.sigmoid(self.visit(ctx.expr()))
    def visitReluFunc(self, ctx): return torch.relu(self.visit(ctx.expr()))
    def visitSoftplusFunc(self, ctx): return torch.nn.functional.softplus(self.visit(ctx.expr()))
    def visitGeluFunc(self, ctx): return torch.nn.functional.gelu(self.visit(ctx.expr()))
    def visitSignFunc(self, ctx): return torch.sign(self.visit(ctx.expr()))
    def visitFractFunc(self, ctx):
        val = self.visit(ctx.expr())
        return val - torch.floor(val)

    def visitAnglFunc(self, ctx): return torch.angle(self.visit(ctx.expr()))
    def visitPrintFunc(self, ctx):
        val = self.visit(ctx.expr())
        print(val,end="\n")
        return val

    def visitSfftFunc(self, ctx):
        """
        Spatial FFT - transforms the expression to frequency domain.
        Applies FFT on all dimensions of the tensor.
        """
        old_vars = self.variables
        self.variables = self.spatial_variables.copy()
        try:
            val = self.visit(ctx.expr())
            # Apply FFT on all dimensions
            dims = tuple(range(val.ndim))
            return torch.fft.fftn(val, dim=dims)
        finally:
            self.variables = old_vars


    def visitSwapFunc(self, ctx):
        tsr = self.visit(ctx.expr(0))

        dim_t = self.visit(ctx.expr(1))
        idx1_t = self.visit(ctx.expr(2))
        idx2_t = self.visit(ctx.expr(3))

        dim = int(dim_t.flatten()[0].item())
        i = int(idx1_t.flatten()[0].item())
        j = int(idx2_t.flatten()[0].item())

        # Handle negative dim
        while dim < 0: dim += tsr.ndim
        while i < 0: i += tsr.shape[dim]
        while j < 0: j += tsr.shape[dim]

        indices = torch.arange(tsr.shape[dim], device=tsr.device)

        val_i = indices[i].clone()
        indices[i] = indices[j]
        indices[j] = val_i

        return torch.index_select(tsr, dim, indices)

    def visitSifftFunc(self, ctx):
        """
        Spatial IFFT - evaluates expression in frequency domain then transforms back.
        Provides frequency coordinate variables for each dimension:
        - Kx, Ky, Kz: frequency indices for last 3 dims (0-indexed)
        - K: isotropic frequency magnitude (Euclidean distance from DC)
        - Fx, Fy, Fz: size of each frequency dimension
        """
        old_vars = self.variables
        self.variables = self.variables.copy()
        device = self.device

        ndim = len(self.shape)
        dim_names = ['x', 'y', 'z', 'w', 'v', 'u']  # Names for dims (from last to first)

        # Generate frequency coordinates for each dimension
        k_components = []
        for i in range(ndim):
            dim_idx = ndim - 1 - i  # Start from last dim
            size_d = self.shape[dim_idx]

            # Create frequency indices (0-indexed, will be shifted for DC centering if needed)
            values = torch.arange(size_d, dtype=torch.float32, device=device)
            view_shape = [1] * ndim
            view_shape[dim_idx] = size_d
            values = values.view(*view_shape).expand(*self.shape)

            # Bind named variables (Kx, Ky, Kz for last 3 dims)
            if i < len(dim_names):
                var_name = f'K{dim_names[i]}'
                self.variables[var_name] = values
                self.variables[f'F{dim_names[i]}'] = float(size_d)

            # Generic fallback for all dims
            self.variables[f'K_dim{dim_idx}'] = values
            self.variables[f'F_dim{dim_idx}'] = float(size_d)

            k_components.append(values)
        # Calculate isotropic K (Euclidean distance from DC)
        k_sq_sum = torch.zeros(self.shape, device=device)
        for k_val in k_components:
            k_sq_sum = k_sq_sum + k_val ** 2

        self.variables['K'] = torch.sqrt(k_sq_sum)
        self.variables['frequency'] = self.variables['K']

        # Legacy aliases
        if 'Kx' in self.variables:
            self.variables['frequency_count'] = self.variables.get('Fx', 1.0)
        self.variables = self.variables | generate_dim_variables(values)

        try:
            val = self.visit(ctx.expr())
            # Apply IFFT on all dimensions
            dims = tuple(range(val.ndim))
            return torch.fft.ifftn(val, dim=dims).real
        finally:
            self.variables = old_vars

    # Two-argument functions
    def visitPowFunc(self, ctx):
        return torch.pow(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
    def visitAtan2Func(self, ctx):
        return torch.atan2(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitClampFunc(self, ctx): return torch.clamp(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.expr(2)))
    def visitLerpFunc(self, ctx):
        a = self.visit(ctx.expr(0))
        b = self.visit(ctx.expr(1))
        w = self.visit(ctx.expr(2))
        return torch.lerp(a, b, w)

    def visitSmoothstepFunc(self, ctx):
        x = self.visit(ctx.expr(0))
        edge0 = self.visit(ctx.expr(1))
        edge1 = self.visit(ctx.expr(2))

        # Scale, bias and saturate x to 0..1 range
        t = torch.clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
        return t * t * (3.0 - 2.0 * t)

    def visitStepFunc(self, ctx):
        x = self.visit(ctx.expr(0))
        edge = self.visit(ctx.expr(1))
        # step(edge, x) = 1 if x >= edge else 0
        return torch.where(x >= edge, 1.0, 0.0)
    # N-argument functions
    def visitSMinFunc(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        if len(args) == 1:
            return torch.min(args[0])  # Global min of single tensor
        return torch.min(torch.stack(torch.broadcast_tensors(*args)))

    def visitSMaxFunc(self, ctx):
        args = [self.visit(e) for e in ctx.expr()]
        if len(args) == 1:
            return torch.max(args[0])  # Global max of single tensor
        return torch.max(torch.stack(torch.broadcast_tensors(*args)))

    def visitTMinFunc(self, ctx):
        return torch.minimum(self.visit(ctx.expr(0)),self.visit(ctx.expr(1)))
    def visitTMaxFunc(self, ctx):
        return torch.maximum(self.visit(ctx.expr(0)),self.visit(ctx.expr(1)))

    def visitFunc1Exp(self, ctx):
        return self.visitChildren(ctx)
    def visitFunc2Exp(self, ctx):
        return self.visitChildren(ctx)
    def visitFuncNExp(self, ctx):
        return self.visitChildren(ctx)
    def visitFunc3Exp(self, ctx):
        return self.visitChildren(ctx)
    def visitFunc4Exp(self, ctx):
        return self.visitChildren(ctx)

    def _normalize_coord(self, coord, size):
        if size > 1:
            return (coord / (size - 1)) * 2.0 - 1.0
        return torch.zeros_like(coord)

    def visitMapFunc(self, ctx):
        tensor = self.visit(ctx.expr(0))
        coords = [self.visit(ctx.expr(i)) for i in range(1, len(ctx.expr()))]
        num_coords = len(coords)

        if num_coords == 0: return tensor
        if num_coords > 3:
            raise ValueError("map() supports max 3 mapping functions.")

        spatial_in_shape = tensor.shape[-num_coords:]
        leading_shape = tensor.shape[:-num_coords]

        batch_size = 1
        for s in leading_shape: batch_size *= s


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
            print("Reshape failed in map(); attempting expand workaround.")
            grid_view = grid.expand(batch_size, *([-1] * len(grid_spatial_shape)), -1)
            grid_view = grid_view.reshape(batch_size, *grid_view.shape[-(num_coords+1):-1], num_coords)

        if num_coords == 1:
            input_final = input_view.reshape(batch_size, 1, 1, -1)
            y_zeros = torch.zeros_like(grid_view[..., :1])
            grid_final = torch.cat([grid_view, y_zeros], dim=-1).unsqueeze(1)
            output = torch.nn.functional.grid_sample(input_final, grid_final, align_corners=True)

        elif num_coords == 2:
            grid_final = grid_view.reshape(batch_size, *grid_view.shape[-3:-1], 2)
            output = torch.nn.functional.grid_sample(input_view, grid_final, align_corners=True)
        else:
            grid_final = grid_view.reshape(batch_size, *grid_view.shape[-4:-1], 3)
            output = torch.nn.functional.grid_sample(input_view, grid_final, align_corners=True)

        actual_spatial = grid_view.shape[1:-1]
        final_shape = list(leading_shape) + list(actual_spatial)
        return output.reshape(final_shape)


    def _kernel_coords(self, size, device):
        half = size // 2
        return torch.arange(size, device=device).float() - half

    def visitConvFunc(self, ctx):
        """
        N-dimensional convolution.
        conv(tensor, kw, expr)           - 1D conv on last dim
        conv(tensor, kw, kh, expr)       - 2D conv on last 2 dims
        conv(tensor, kw, kh, kd, expr)   - 3D conv on last 3 dims

        Kernel expression uses kX, kY, kZ as centered coordinates.
        """
        img = self.visit(ctx.expr(0))
        num_args = len(ctx.expr())

        # Parse kernel sizes based on argument count
        if num_args == 3:
            kernel_sizes = [int(self.visit(ctx.expr(1)).flatten()[0].item())]
            k_expr_ctx = ctx.expr(2)
        elif num_args == 4:
            kernel_sizes = [
                int(self.visit(ctx.expr(1)).flatten()[0].item()),
                int(self.visit(ctx.expr(2)).flatten()[0].item())
            ]
            k_expr_ctx = ctx.expr(3)
        elif num_args == 5:
            kernel_sizes = [
                int(self.visit(ctx.expr(1)).flatten()[0].item()),
                int(self.visit(ctx.expr(2)).flatten()[0].item()),
                int(self.visit(ctx.expr(3)).flatten()[0].item())
            ]
            k_expr_ctx = ctx.expr(4)
        else:
            raise ValueError("conv() expects 3-5 arguments: (tensor, kw, [kh], [kd], kernel_expr|list)")

        num_spatial = len(kernel_sizes)

        kw = kernel_sizes[0]
        kh = kernel_sizes[1] if num_spatial >= 2 else 1
        kd = kernel_sizes[2] if num_spatial >= 3 else 1

        kx = self._kernel_coords(kw, self.device).view(1, 1, kw).expand(kd, kh, kw)
        ky = self._kernel_coords(kh, self.device).view(1, kh, 1).expand(kd, kh, kw)
        kz = self._kernel_coords(kd, self.device).view(kd, 1, 1).expand(kd, kh, kw)

        k_variables = self.variables.copy()
        k_variables.update({
            'kX': kx, 'kY': ky, 'kZ': kz,
            'kW': float(kw), 'kH': float(kh), 'kD': float(kd),
            'kernel_width': float(kw), 'kernel_height': float(kh), 'kernel_depth': float(kd)
        })

        k_visitor = TensorEvalVisitor(k_variables, (kd, kh, kw), device=self.device)
        kernel = k_visitor.visit(k_expr_ctx)

        if kernel.numel() == 1:
            kernel = kernel.expand(kd, kh, kw).clone()
        elif kernel.numel() == kw * kh * kd:
            kernel = kernel.reshape(kd, kh, kw)

        leading_shape = img.shape[:-num_spatial] if num_spatial < img.ndim else ()
        spatial_shape = img.shape[-num_spatial:]

        combined_leading = 1
        for s in leading_shape:
            combined_leading *= s

        if len(leading_shape) == 0:
            reshaped = img.unsqueeze(0).unsqueeze(0)
        else:
            reshaped = img.reshape(combined_leading, 1, *spatial_shape)

        channels = reshaped.shape[1]

        if num_spatial == 1:
            kernel_1d = kernel.flatten()[:kw]
            conv_kernel = kernel_1d.view(1, 1, kw).expand(channels, 1, kw)
            output = torch.nn.functional.conv1d(reshaped, conv_kernel, padding=kw//2, groups=channels)
        elif num_spatial == 2:
            kernel_2d = kernel[0] if kd > 1 else kernel.reshape(kh, kw)
            conv_kernel = kernel_2d.view(1, 1, kh, kw).expand(channels, 1, kh, kw)
            output = torch.nn.functional.conv2d(reshaped, conv_kernel, padding=(kh//2, kw//2), groups=channels)
        elif num_spatial == 3:
            conv_kernel = kernel.view(1, 1, kd, kh, kw).expand(channels, 1, kd, kh, kw)
            output = torch.nn.functional.conv3d(reshaped, conv_kernel, padding=(kd//2, kh//2, kw//2), groups=channels)
        else:
            raise ValueError(f"conv() supports up to 3 spatial dimensions, got {num_spatial}")

        output = output.squeeze(1)
        if len(leading_shape) == 0:
            output = output.squeeze(0)
        else:
            final_shape = list(leading_shape) + list(output.shape[1:])
            output = output.reshape(final_shape)

        return output

    def visitAtomExp(self, ctx):
        return self.visitChildren(ctx)

    def visitFunc2Expr(self, ctx):
        return self.visit(ctx.getChild(0))  # forward to Atan2Func, PowFunc, etc.

    def visitExpr(self, ctx):
       return self.visitChildren(ctx)

    def visitPrintShapeFunc(self, ctx):
        tsr = self.visit(ctx.expr())
        print(tsr.shape)
        return tsr