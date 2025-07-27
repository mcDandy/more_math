from ast import List
from email.policy import default
from inspect import cleandoc
import re
import tokenize
from io import StringIO
import torch
from .parser import Parser
class ConditioningMathNode:
    """
    This node enables the use of math expressions in the conditioning of the image. It is recommended to keep the Tensor expression the same as the pooled_output expression.
    INPUTS:
        a, b, c, d:
            Conditioning, bound to variables with the same name. Defaults to zero conditioning if not provided.
        w, x, y, z:
            Floats, bound to variables of the expression. Defaults to 0.0 if not provided.
        Tensor expression:
            String, describing expression to mix tensor part of conditioning. Tensor probably describes the composition of the image as it has the say what is on the image. Valid functions are sin, cos, tan, abs, sqrt, min, max, norm. Valid operators are +, -, *, /, ^, %.
        Pooled output expression:
            String, describing expression to mix pooled_output part of conditioning. pooled_output does not have that much say in the image but can change some details of the image or completly change the image in some cases, probably also used for positional and temporal conditioning. Expression uses same syntax as Tensor.
        
    OUTPUTS:
        CONDITIONING:
            Returns a CONDITIONING object that contains the result of the math expression applied to the input conditionings.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
        """
        return {
            "required": {
                "a": ("CONDITIONING", {

                }),

                "Tensor": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "a+b",
                    "description": "Describes composition of the image. Valid functions are sin,cos,tan,abs,sqrt,min,max. Valid operators are +,-,*,/,^,%"

                }),
                "pooled_output": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "a+b",
                    "description": "Can change some details of the image, probably also used for positional and temporal conditioning."
                }),
            },
            "optional": {
                "b": ("CONDITIONING", {
                    "default": 0,
                }),
                "c": ("CONDITIONING", {
                    "default": 0,
                }),
                "d": ("CONDITIONING", {
                    "default": 0,
                }),
                "w": ("FLOAT", {
                    "default": 0,
                    "forceInput":True
                }),
                "x": ("FLOAT", {
                    "default": 0,
                    "forceInput":True
                }),
                "y": ("FLOAT", {
                    "default": 0,
                    "forceInput":True
                }),
                "z": ("FLOAT", {
                    "default": 0,
                    "forceInput":True
                }),


                # "int_field": ("INT", {"default": 0, "min": 0, "max": 100, "step": 1}),
                # "float_field": ("FLOAT", {"default": 0.5, "min": -10.0, "max": 10.0, "step": 0.001}),
            }
        }

    RETURN_TYPES = ("CONDITIONING",)
    #RETURN_NAMES = ("image_output_name",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "condMathNode"

    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node

    CATEGORY = "More math"

    def condMathNode(self, Tensor,pooled_output, a, b=None, c=None, d=None,w=0.0,x=0.0,y=0.0,z=0.0):
        if b is None:
           b = [[torch.zeros_like(a[0][0]), {"pooled_output": torch.zeros_like(a[0][1]["pooled_output"])}]] 
        if c is None:
           c = [[torch.zeros_like(a[0][0]), {"pooled_output": torch.zeros_like(a[0][1]["pooled_output"])}]] 
        if d is None:
           d = [[torch.zeros_like(a[0][0]), {"pooled_output": torch.zeros_like(a[0][1]["pooled_output"])}]] 
        tokens = tokenize_expression(Tensor)
        parser = Parser(tokens)
        ast = parser.parse_expression()
        tokens = tokenize_expression(pooled_output)
        parser = Parser(tokens)
        ast1 = parser.parse_expression()
        print("AST:", ast)
        print("AST1:", ast1)
        ta = a[0][0].clone()
        tb = b[0][0].clone()
        pa = a[0][1]["pooled_output"].clone()
        pb = b[0][1]["pooled_output"].clone()
        tc = c[0][0].clone()
        td = d[0][0].clone()
        pc = c[0][1]["pooled_output"].clone()
        pd = d[0][1]["pooled_output"].clone()
        def to_tensor(val, ref):
            if isinstance(val, torch.Tensor):
                return val
            # Convert float/int, to tensor with the same shape as ref
            return torch.full_like(ref, float(val))

        result1 = evaluate(ast, {'a': ta, 'b': tb, 'c': tc, 'd': td,'w':w,'x':x,'y':y,'z':z})
        result2 = evaluate(ast1, {'a': pa, 'b': pb,'c': pc, 'd': pd,'w':w,'x':x,'y':y,'z':z})

        result1 = to_tensor(result1, ta)
        result2 = to_tensor(result2, pa)

        result = [[result1, {"pooled_output": result2}]]
        print("Result:", result)
        return (result,)

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""
def evaluate(ast, variables):
    """
    Evaluates AST using variables.
    Allows standard geometric functions and standard arithmetic functions.
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
        operand_val = evaluate(operand_expr, variables)
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
        arg_vals = [evaluate(arg, variables) for arg in arg_exprs]

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
        left_val = evaluate(left_expr, variables)
        right_val = evaluate(right_expr, variables)
        if op == '+':
            return torch.add(left_val, right_val)
        elif op == '-':
            return torch.subtract(left_val, right_val)
        elif op == '*':
            return torch.multiply(left_val, right_val)
        elif op == '/':
            return torch.divide(left_val, right_val)
        elif op == '^':
            return torch.pow(left_val, right_val)
        elif op == '%':
            return torch.fmod(left_val, right_val)
        else:
            raise ValueError(f"Unsupported operator: {op}")

    elif node_type == 'PARENTHESIS':
        expr = ast[1]
        return evaluate(expr, variables)

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


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "DMConditioningMathNode": ConditioningMathNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ConditioningMathNode": "Conditioning math node",
    "Tensor": "Tensor expression",
    "pooled_output": "Pooled output expression"
}
