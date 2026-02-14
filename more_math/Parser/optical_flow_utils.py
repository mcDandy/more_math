import torch
import torch.nn.functional as F
from torchvision.models.optical_flow import raft_large, Raft_Large_Weights
from torchvision.utils import flow_to_image as torchvision_flow_to_image
import numpy as np

_raft_model = None

def get_raft_model(device):
    global _raft_model
    if _raft_model is None:
        weights = Raft_Large_Weights.DEFAULT
        _raft_model = raft_large(weights=weights, progress=False).to(device).eval()
    return _raft_model

def warp(x, flow, padding_mode='reflection'):
    """
    Warps an image or tensor using the given flow.
    x: [B, C, H, W]
    flow: [B, 2, H, W] (flow in pixels)
    padding_mode: passed to F.grid_sample (e.g. 'zeros' for occlusion detection)
    """
    b, c, h, w = x.shape
    device = flow.device # Use flow device as the master device
    x = x.to(device)

    # Create grid
    grid_y, grid_x = torch.meshgrid(
        torch.linspace(0, h - 1, h, device=device),
        torch.linspace(0, w - 1, w, device=device),
        indexing='ij'
    )
    # [H, W]

    grid = torch.stack((grid_x, grid_y), dim=0).unsqueeze(0).repeat(b, 1, 1, 1) # [B, 2, H, W]

    # Add flow to grid
    v_grid = grid + flow # [B, 2, H, W]

    # Normalize to [-1, 1] for grid_sample
    v_grid_x = 2.0 * v_grid[:, 0, :, :] / max(w - 1, 1) - 1.0
    v_grid_y = 2.0 * v_grid[:, 1, :, :] / max(h - 1, 1) - 1.0

    v_grid = torch.stack((v_grid_x, v_grid_y), dim=3) # [B, H, W, 2] with (x, y)

    return F.grid_sample(x, v_grid, mode='bilinear', padding_mode=padding_mode, align_corners=True)

def preprocess_image(img, device):
    """
    img: [B, H, W, C] in range [0, 1]
    Returns: [B, 3, H, W] normalized for RAFT
    """
    if img.ndim == 3:
        img = img.unsqueeze(0)

    # ComfyUI [B, H, W, C] -> Torch [B, C, H, W]
    img = img.movedim(-1, 1)

    # Ensure RGB
    if img.shape[1] == 1:
        img = img.expand(-1, 3, -1, -1)
    elif img.shape[1] > 3:
        img = img[:, :3, :, :]

    # Scale to [0, 255] as RAFT transforms usually expect this
    img = img * 255.0

    # Use official transform if possible
    weights = Raft_Large_Weights.DEFAULT
    transform = weights.transforms()

    # The transform expects [0, 255] and returns normalized [-1, 1]
    # It takes (img1, img2) but we can use it for one or just follow its logic
    # Actually, let's just follow the logic: 2 * (img / 255.0) - 1.0
    # Wait, if I do that, it's just 2 * img_01 - 1.0.

    return (2.0 * (img / 255.0) - 1.0).to(device)

def get_optical_flow(img1, img2, tiling_size=0, iterations=12, multi_scale=False):
    """
    img1, img2: [H, W, C] or [B, H, W, C]
    Returns: [B, H, W, 2] flow vectors
    """
    device = img1.device
    model = get_raft_model(device)

    img1_proc = preprocess_image(img1, device)
    img2_proc = preprocess_image(img2, device)

    b, _, h, w = img1_proc.shape

    # Auto-tiling for large images to prevent OOM
    # 2MPx is a reasonable limit for 8GB VRAM without tiling
    if tiling_size <= 0 and (h * w) > 2000000:
        tiling_size = 1024

    # Handle fraction or float conversion
    if 0 < tiling_size < 1:
        tiling_size = int(min(h, w) * tiling_size)
    else:
        tiling_size = int(tiling_size)

    # Ensure divisible by 8 for RAFT
    h_new, w_new = (h // 8) * 8, (w // 8) * 8
    if h != h_new or w != w_new:
        img1_proc = F.interpolate(img1_proc, size=(h_new, w_new), mode='bilinear', align_corners=False)
        img2_proc = F.interpolate(img2_proc, size=(h_new, w_new), mode='bilinear', align_corners=False)

    # Process sequentially to save memory
    flows = []
    with torch.no_grad():
        for i in range(b):
            p1 = img1_proc[i:i+1]
            p2 = img2_proc[i:i+1]

            global_flow = None
            if multi_scale:
                # 1. Global Pass
                # Downsample more aggressively to capture massive jumps (max 256)
                g_size = 256
                g_h = (min(h_new, g_size) // 8) * 8
                g_w = (min(w_new, g_size) // 8) * 8

                gp1 = F.interpolate(p1, size=(g_h, g_w), mode='bilinear', align_corners=False)
                gp2 = F.interpolate(p2, size=(g_h, g_w), mode='bilinear', align_corners=False)

                # Global flow estimation
                global_flow = model(gp1, gp2, num_flow_updates=iterations)[-1]

                # Upsample global flow to high-res
                global_flow = F.interpolate(global_flow, size=(h_new, w_new), mode='bilinear', align_corners=False)
                global_flow[:, 0] *= float(w_new) / g_w
                global_flow[:, 1] *= float(h_new) / g_h

                # print(f"DEBUG: Global flow at center: {global_flow[0, :, h_new//2, w_new//2]}")

                # 2. Warp img2 using global flow
                p2_warped = warp(p2, global_flow)
                target_p2 = p2_warped
            else:
                target_p2 = p2

            # 3. Local Refinement (Tiled or Full)
            if tiling_size > 0:
                f_residual = _tiled_flow(model, p1, target_p2, tiling_size, iterations)
            else:
                f_residual = model(p1, target_p2, num_flow_updates=iterations)[-1]

            # 4. Combine
            if global_flow is not None:
                total_flow = global_flow + f_residual
            else:
                total_flow = f_residual

            flows.append(total_flow)

            if i % 4 == 0 and b > 4:
                torch.cuda.empty_cache()

    flow = torch.cat(flows, dim=0)

    # Resize flow back if needed
    if h != h_new or w != w_new:
        flow = F.interpolate(flow, size=(h, w), mode='bilinear', align_corners=False)
        # Rescale flow values
        flow[:, 0] *= float(w) / w_new
        flow[:, 1] *= float(h) / h_new

    # [B, 2, H, W] -> [B, H, W, 2]
    return flow.movedim(1, -1)

def calculate_occlusion_mask(flow):
    """
    Calculates a disocclusion mask: pixels revealed by motion that have no
    valid source data (e.g. background uncovered when an object moves away).

    flow: [B, H, W, 2] or [H, W, 2]
    Returns: [B, H, W] mask (1.0 = disoccluded/revealed, 0.0 = valid)
    """
    was_single = (flow.ndim == 3)
    if was_single:
        flow = flow.unsqueeze(0)

    # sanitize flow
    flow = torch.nan_to_num(flow, nan=0.0, posinf=0.0, neginf=0.0)

    b, h, w, _ = flow.shape
    device = flow.device

    # [B, H, W, 2] -> [B, 2, H, W] for warp()
    flow_nchw = flow.movedim(-1, 1)

    # Warp a solid-ones image with the flow.
    # Use zero padding so samples from outside are 0, making disocclusions visible
    ones = torch.ones((b, 1, h, w), device=device)
    warped_ones = warp(ones, flow_nchw, padding_mode='zeros')  # [B, 1, H, W]

    # Pixels that are < threshold are disoccluded
    mask = 1.0 - warped_ones.squeeze(1).clamp(0.0, 1.0)  # [B, H, W]

    return mask.squeeze(0) if was_single else mask

def apply_flow(image, flow):
    """
    Warps an image using optical flow vectors.
    image: [B, H, W, C] (ComfyUI format)
    flow:  [B, H, W, 2] (from rife())
    Returns: [B, H, W, C] warped image
    """
    if image.ndim == 3:
        image = image.unsqueeze(0)
    if flow.ndim == 3:
        flow = flow.unsqueeze(0)

    # [B, H, W, 2] -> [B, 2, H, W]
    flow_nchw = flow.movedim(-1, 1)

    # Ensure image is on the same device as flow
    img_nchw = image.movedim(-1, 1).to(flow.device)

    warped = warp(img_nchw, flow_nchw)

    # [B, C, H, W] -> [B, H, W, C]
    return warped.movedim(1, -1)

def flow_to_image(flow):
    """
    Converts flow vectors [B, H, W, 2] to RGB images [B, H, W, 3] for visualization.
    """
    if flow.ndim == 3:
        flow = flow.unsqueeze(0)

    # [B, H, W, 2] -> [B, 2, H, W]
    flow_torch = flow.movedim(-1, 1)

    # torchvision_flow_to_image expects (N, 2, H, W)
    img_uint8 = torchvision_flow_to_image(flow_torch)

    # [B, 3, H, W] -> [B, H, W, 3]
    img = img_uint8.movedim(1, -1).float() / 255.0

    return img

def _tiled_flow(model, img1, img2, tiling_size, iterations):
    """
    Robust tiling implementation with weighted blending and edge coverage.
    """
    b, c, h, w = img1.shape
    device = img1.device

    # Enforce minimum tile size for RAFT
    if tiling_size < 256:
        # If user provided a very small value, maybe they meant fraction? 
        # But for ComfyUI, we'll just enforce a safe minimum.
        tiling_size = max(256, tiling_size)

    # Ensure tiling_size is divisible by 8
    tiling_size = (tiling_size // 8) * 8

    # Clip tiling_size to image dimensions
    t_h = int(min(tiling_size, h))
    t_w = int(min(tiling_size, w))

    # If image is smaller than tiling_size after divisibility adjustments
    if t_h < 8 or t_w < 8:
        return model(img1, img2, num_flow_updates=iterations)[-1]

    output_flow = torch.zeros((b, 2, h, w), device=device)
    weights = torch.zeros((b, 1, h, w), device=device)

    # Stride of 50% overlap is usually good
    stride_h = int(t_h // 2)
    stride_w = int(t_w // 2)

    # Generate coordinates for tiles
    y_coords = list(range(0, h - t_h, stride_h)) + [max(0, h - t_h)]
    x_coords = list(range(0, w - t_w, stride_w)) + [max(0, w - t_w)]

    # Remove duplicates if any (when image size matches stride)
    y_coords = sorted(list(set(y_coords)))
    x_coords = sorted(list(set(x_coords)))

    for y in y_coords:
        for x in x_coords:
            patch1 = img1[:, :, y:y+t_h, x:x+t_w]
            patch2 = img2[:, :, y:y+t_h, x:x+t_w]

            # RAFT expects inputs divisible by 8, but we already ensured t_h, t_w are.
            patch_flow = model(patch1, patch2, num_flow_updates=iterations)[-1]

            # Create local mask for this tile
            # Linear tapering only on overlapping edges
            layer_mask = torch.ones((1, 1, t_h, t_w), device=device)
            overlap_h = stride_h
            overlap_w = stride_w

            if y > 0: # Fade in top
                layer_mask[:, :, :overlap_h, :] *= torch.linspace(0, 1, overlap_h, device=device).view(1, 1, overlap_h, 1)
            if y + t_h < h: # Fade out bottom
                layer_mask[:, :, -overlap_h:, :] *= torch.linspace(1, 0, overlap_h, device=device).view(1, 1, overlap_h, 1)
            if x > 0: # Fade in left
                layer_mask[:, :, :, :overlap_w] *= torch.linspace(0, 1, overlap_w, device=device).view(1, 1, 1, overlap_w)
            if x + t_w < w: # Fade out right
                layer_mask[:, :, :, -overlap_w:] *= torch.linspace(1, 0, overlap_w, device=device).view(1, 1, 1, overlap_w)

            output_flow[:, :, y:y+t_h, x:x+t_w] += patch_flow * layer_mask
            weights[:, :, y:y+t_h, x:x+t_w] += layer_mask

    return output_flow / torch.clamp(weights, min=1e-6)
