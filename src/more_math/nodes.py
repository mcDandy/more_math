from ast import List
from inspect import cleandoc
import re
import tokenize
from io import StringIO
import torch
from .parser import Parser
class Example:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict):
        Tell the main program input parameters of nodes.
    IS_CHANGED:
        optional method to control when the node is re executed.

    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "a": ("CONDITIONING", {

                }),
                "b": ("CONDITIONING", {

                }),
                "string_field": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "a+b"
                }),
            },
        }

    RETURN_TYPES = ("CONDITIONING",)
    #RETURN_NAMES = ("image_output_name",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "test"

    #OUTPUT_NODE = False
    #OUTPUT_TOOLTIPS = ("",) # Tooltips for the output node

    CATEGORY = "Example"

    def test(self, string_field, a, b):
        tokens = tokenize_expression(string_field)
        parser = Parser(tokens)
        ast = parser.parse_expression()
        print("AST:", ast)
        ta = a[0][0].clone()
        tb = b[0][0].clone()
        
        pa = a[0][1]["pooled_output"].clone()
        pb = b[0][1]["pooled_output"].clone()
        result1 = evaluate(ast,{'a':ta,'b':tb})
        result2 = evaluate(ast,{'a':pa,'b':pb})
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
    if not isinstance(ast, tuple):
        return ast  # Return literal values directly (if any)
    
    node_type = ast[0]

    if node_type == 'VARIABLE':
        var_name = ast[1]
        return variables[var_name]

    elif node_type == 'LITERAL':
        return ast[1]  # Literal value

    elif node_type == 'FUNCTION':
        func_name, arg_expr = ast[1]
        arg_val = evaluate(arg_expr, variables)

        if func_name == 'ABS':
            return torch.abs(arg_val)
        elif func_name == 'NORM':
            return torch.linalg.vector_norm(arg_val)
        elif func_name == 'SQRT':
            return torch.sqrt(arg_val)
        elif func_name == 'SIN':
            return torch.sin(arg_val)
        elif func_name == 'COS':
            return torch.cos(arg_val)
        else:
            raise ValueError(f"Unsupported function: {func_name}")

    elif node_type == 'BINOP':
        op, left_expr, right_expr = ast[1]
        left_val = evaluate(left_expr, variables)
        right_val = evaluate(right_expr, variables)

        if op == '+':
            print("Left value:", type(left_val))
            return torch.add(left_val, right_val)
        elif op == '-':
            return torch.subtract(left_val, right_val)
        elif op == '*':
            return torch.multiply(left_val, right_val)
        elif op == '/':
            return torch.divide(left_val, right_val)
        elif op == '^':
            return torch.pow(left_val, right_val)
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
    "Example": Example
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Example": "Example Node"
}
