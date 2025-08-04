import torch

def getIndexTensorAlongDim(tensor, dim):
    shape = tensor.shape
    
    # Create values: shape (size of dim)
    values = torch.arange(shape[dim], dtype=torch.float32)

    # Reshape values to align with the target dimension
    view_shape = [1] * len(shape)
    view_shape[dim] = shape[dim]
    values = values.view(*view_shape)

    # Broadcast to full shape
    return values.expand(*shape)
