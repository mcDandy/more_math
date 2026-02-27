import torch
from more_math.ConditioningMathNode import ConditioningMathNode

def test_conditioning_token_mismatch_padding():
    # a: 77 tokens
    ta = torch.ones((1, 77, 1024))
    da = {"pooled_output": torch.ones((1, 1024))}
    ca = [(ta, da)]

    # b: 154 tokens (e.g. concatenated)
    tb = torch.ones((1, 154, 1024)) * 0.5
    db = {"pooled_output": torch.ones((1, 1024))}
    cb = [(tb, db)]

    # a + b -> result should have 154 tokens
    # tokens 0-76: 1 + 0.5 = 1.5
    # tokens 77-153: 0 + 0.5 = 0.5
    result_list, stack = ConditioningMathNode.execute(V={"V0": ca, "V1": cb}, F={}, Expression="a + b", Expression_pi="a + b", length_mismatch="pad")
    
    # result_list[0] is a list: [(tensor, dict), ...]
    # Get the first conditioning tuple
    cond_tuple = result_list[0][0]
    res_tensor = cond_tuple[0]
    res_dict = cond_tuple[1]["pooled_output"]
    assert res_tensor.shape == (1, 154, 1024)
    assert torch.allclose(res_tensor[0, :77, :], torch.full((77, 1024), 1.5))
    assert torch.allclose(res_tensor[0, 77:, :], torch.full((77, 1024), 0.5))

    # Pooled output check
    assert res_dict.shape == (1, 1024)

    assert torch.allclose(res_dict, torch.full((1, 1024), 2.0))

if __name__ == "__main__":
    test_conditioning_token_mismatch_padding()
    print("Test passed!")
