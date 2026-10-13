import torch

from more_math.Parser import optical_flow_utils as ofu
from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.helper_functions import parse_expr

def test_permute_and_apply():
    image = torch.arange(24.0).reshape(1, 2, 4, 3)
    tree = parse_expr("permute(image, [0, 3, 1, 2])")
    result = UnifiedMathVisitor({"image": image}).visit(tree)
    assert torch.equal(result, image.permute(0, 3, 1, 2))

    image = torch.rand(1, 32, 32, 3)
    flow = torch.zeros(1, 32, 32, 2)
    warped = ofu.apply_flow(image, flow)
    assert warped.shape == image.shape
    assert torch.allclose(warped, image, atol=1e-5)
