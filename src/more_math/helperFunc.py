import torch
from io import StringIO
import tokenize

def to_tensor(val, ref):
            if isinstance(val, torch.Tensor):
                return val
            # Convert float/int, to tensor with the same shape as ref
            return torch.full_like(ref, float(val))
def evaluate_tensor_expression(ast, variables):
    """
    Evaluates AST using variables.
    Allows standard geometric functions(sin,cos,tan) and standard arithmetic functions with additions of.
    """
    if not isinstance(ast, tuple):
        return ast  # Return literal values directly (if any)
    
    node_type = ast[0]

    if node_type == 'VARIABLE':
        var_name = ast[1]
        if var_name not in variables:
            raise ValueError(f"Variable '{var_name}' not found in variables: {list(variables.keys())}")
        return variables[var_name]

    elif node_type == 'LITERAL':
        return ast[1]  # Literal value

    elif node_type == 'UNARYOP':
        op, operand_expr = ast[1]
        operand_val = evaluate_tensor_expression(operand_expr, variables)
        if op == '+':
            return operand_val
        elif op == '-':
            return torch.neg(operand_val)
        else:
            raise ValueError(f"Unsupported unary operator: {op}")

    elif node_type == 'FUNCTION':
        func_name, arg_exprs = ast[1]
        if not isinstance(arg_exprs, (list, tuple)):
            arg_exprs = [arg_exprs]
        arg_vals = [evaluate_tensor_expression(arg, variables) for arg in arg_exprs]

        if func_name == 'ABS':
            return torch.abs(arg_vals[0])
        elif func_name == 'NORM':
            return torch.nn.functional.normalize(arg_vals[0], p=2, dim=-1)
        elif func_name == 'SQRT':
            return torch.sqrt(arg_vals[0])
        elif func_name == 'SIN':
            return torch.sin(arg_vals[0])
        elif func_name == 'COS':
            return torch.cos(arg_vals[0])
        elif func_name == 'TAN':
            return torch.tan(arg_vals[0])
        elif func_name == 'MAX':
            return torch.max(*arg_vals)
        elif func_name == 'MIN':
            return torch.max(*arg_vals)
        else:
            raise ValueError(f"Unsupported function: {func_name}")

    elif node_type == 'BINOP':
        op, left_expr, right_expr = ast[1]
        left_val = evaluate_tensor_expression(left_expr, variables)
        right_val = evaluate_tensor_expression(right_expr, variables)
        if op == '+':
            return torch.add(left_val, right_val)
        elif op == '-':
            return torch.subtract(left_val, right_val)
        elif op == '*':
            return torch.multiply(left_val, right_val)
        elif op == '/':
            return torch.divide(left_val, right_val)
        elif op == '^':
            return torch.pow(to_tensor(left_val,variables['a']).type(torch.complex64), to_tensor(right_val,variables['a']).type(torch.complex64)).real
        elif op == '%':
            return torch.fmod(left_val, right_val)
        else:
            raise ValueError(f"Unsupported operator: {op}")

    elif node_type == 'PARENTHESIS':
        expr = ast[1]
        return evaluate_tensor_expression(expr, variables)

    else:
        raise ValueError(f"Unknown AST node type: {node_type}")
def tokenize_expression(expr):
    f = StringIO(expr)
    tokens_gen = tokenize.generate_tokens(f.readline)
    filtered_tokens = []
    for toktype, tokval, _, _, _ in tokens_gen:
        token_name = tokenize.tok_name[toktype]
        if token_name in {'COMMENT', 'NL'}:  # Skip comments and newlines
            continue
        filtered_tokens.append((token_name, tokval.strip()))
    return filtered_tokens
