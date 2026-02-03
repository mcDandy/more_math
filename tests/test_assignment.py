import torch
from .test_unified_math import parse_and_visit

def test_multidimensional_indexing():
    T = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    vars = {"T": T}

    # 1. Single index (dim 0)
    assert torch.allclose(parse_and_visit("T[0]", vars), torch.tensor([1.0, 2.0]))

    # 2. Multi index
    assert parse_and_visit("T[1, 0]", vars) == 3.0
    assert parse_and_visit("T[0, 1]", vars) == 2.0

    # 3. List indexing on dim 0
    res_list = parse_and_visit("T[[0, 1]]", vars)
    assert torch.allclose(res_list, T)

def test_tensor_assignment():
    T = torch.zeros((2, 2))
    vars = {"T": T}

    # 1. Scalar to position
    parse_and_visit("T[0, 0] = 5.0;", vars)
    assert T[0, 0] == 5.0

    # 2. Scalar to slice (broadcast)
    parse_and_visit("T[1] = 3.0;", vars)
    assert torch.allclose(T[1], torch.tensor([3.0, 3.0]))

    # 3. Tensor to slice
    parse_and_visit("T[0] = [1, 2];", vars)
    assert torch.allclose(T[0], torch.tensor([1.0, 2.0]))

def test_4d_assignment():
    # val[0] expect 4d if dim0=1 or 3d
    T = torch.zeros((2, 3, 4, 4))
    vars = {"T": T}

    # Slice assignment
    val_3d = torch.ones((3, 4, 4))
    parse_and_visit("T[0] = V1;", {"T": T, "V1": val_3d})
    assert torch.allclose(T[0], val_3d)

    # 4D with leading 1 assignment
    val_4d_1 = torch.ones((1, 3, 4, 4)) * 2.0
    parse_and_visit("T[1] = V2;", {"T": T, "V2": val_4d_1})
    assert torch.allclose(T[1], val_4d_1[0])

    # Position assignment
    parse_and_visit("T[0, 1, 2, 3] = 9.0;", vars)
    assert T[0, 1, 2, 3] == 9.0

def test_list_assignment():
    L = [[1, 2], [3, 4]]
    vars = {"L": L}

    # Nested assignment
    parse_and_visit("L[0, 1] = 99;", vars)
    assert L[0][1] == 99

    # Multi-bracket syntax
    parse_and_visit("L[1][0] = 88;", vars)
    assert L[1][0] == 88

def test_enhanced_assignment_logic():
    # 1. Scalar filling: val[0] = scalar
    T = torch.zeros((2, 2, 2))
    vars = {"T": T}
    parse_and_visit("T[0] = 5.0;", vars)
    assert torch.all(T[0] == 5.0)

    # 2. 1-element tensor/list filling
    parse_and_visit("T[1] = [7.0];", vars)
    assert torch.all(T[1] == 7.0)

    # 3. Rank matching (squeeze leading 1s)
    # Target slice T[0, 0] is 1D (shape [2])
    # Value is 3D (shape [1, 1, 2])
    val_3d = torch.tensor([[[9.0, 9.0]]])
    parse_and_visit("T[0, 0] = V1;", {"T": T, "V1": val_3d})
    assert torch.allclose(T[0, 0], torch.tensor([9.0, 9.0]))

if __name__ == "__main__":
    test_multidimensional_indexing()
    test_tensor_assignment()
    test_4d_assignment()
    test_list_assignment()
    test_enhanced_assignment_logic()
    print("Assignment tests passed!")

