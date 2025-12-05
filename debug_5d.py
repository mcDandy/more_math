
import sys
import os
import torch
sys.path.insert(0, os.path.abspath('src'))
# Add ComfyUI path for dependencies if needed
sys.path.insert(0, os.path.abspath('../../')) 
from more_math.LatentMathNode import LatentMathNode

print("Testing 5D tensors...")
node = LatentMathNode()
# Shape: (1, 5, 4, 32, 32)
samples = torch.randn(1, 5, 4, 32, 32)
l_in = {"samples": samples}

try:
    print("Test 1: Identity")
    res = node.execute("a * 1.0", a=l_in)[0]["samples"]
    print("Shape:", res.shape)
    assert res.shape == (1, 5, 4, 32, 32)
    
    res_t = node.execute("a + T", a=l_in)[0]["samples"]
    print("Shape T:", res_t.shape)
    assert torch.allclose(res_t, samples + 5.0), "T addition failed value check"
    print("T addition passed strict check")
    
    print("Test 3: FFT")
    res_fft = node.execute("ifft(fft(a))", a=l_in)[0]["samples"]
    assert torch.allclose(res_fft, samples, atol=1e-5), "FFT roundtrip failed"
    print("FFT passed strict check")
    
except Exception as e:
    import traceback
    traceback.print_exc()
