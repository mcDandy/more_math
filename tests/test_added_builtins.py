import pytest
import torch
from comfy.k_diffusion import sampling as k_sampling

from more_math.Parser.UnifiedMathVisitor import UnifiedMathVisitor
from more_math.helper_functions import parse_expr


def _visit(expression, variables=None):
    return UnifiedMathVisitor(variables or {}).visit(parse_expr(expression))


@pytest.mark.parametrize("expression, expected", [
    ('interp(12, [0, 24], [0, 1])', 0.5),
    ('interp(6, [0, 24], [0, 1], "smooth")', 0.15625),
    ('interp(23, [0, 24], [0, 1], "step")', 0.0),
    ('interp(24, [0, 24], [0, 1], "step")', 1.0),
    ('interp(-5, [0, 24], [2, 1])', 2.0),
    ('interp(99, [0, 24], [2, 1])', 1.0),
    ('interp(12, [24, 0], [1, 0])', 0.5),
])
def test_interp_scalar(expression, expected):
    assert _visit(expression) == pytest.approx(expected)


def test_interp_tensor_positions():
    x = torch.tensor([-1.0, 6.0, 12.0, 30.0])

    assert torch.allclose(_visit('interp(x, [0, 24], [0, 1])', {"x": x}), torch.tensor([0.0, 0.25, 0.5, 1.0]))
    assert torch.equal(_visit('interp(x, [0, 24], [0, 1], "step")', {"x": x}), torch.tensor([0.0, 0.0, 0.0, 1.0]))


def test_interp_between_tensor_keyframes():
    result = _visit('interp(0.25, [0, 1], [a, b])', {"a": torch.zeros(2), "b": torch.ones(2)})

    assert torch.allclose(result, torch.full((2,), 0.25))


@pytest.mark.parametrize("expression, reference", [
    ('sigm_karras(10, 0.03, 14.6)', lambda: k_sampling.get_sigmas_karras(10, 0.03, 14.6)),
    ('sigm_karras(10, 0.03, 14.6, 5)', lambda: k_sampling.get_sigmas_karras(10, 0.03, 14.6, 5.0)),
    ('sigm_exponential(10, 0.03, 14.6)', lambda: k_sampling.get_sigmas_exponential(10, 0.03, 14.6)),
    ('sigm_polyexponential(10, 0.03, 14.6, 2)', lambda: k_sampling.get_sigmas_polyexponential(10, 0.03, 14.6, 2.0)),
    ('sigm_laplace(10, 0.03, 14.6, 0.1, 0.6)', lambda: k_sampling.get_sigmas_laplace(10, 0.03, 14.6, 0.1, 0.6)),
])
def test_sigma_schedules_match_comfy(expression, reference):
    assert torch.allclose(_visit(expression), reference())


@pytest.mark.parametrize("mode, expected", [
    ("normal", 0.8),
    ("multiply", 0.4),
    ("screen", 0.9),
    ("difference", 0.3),
    ("darken", 0.5),
])
def test_blend_modes(mode, expected):
    assert _visit(f'blend(0.5, 0.8, "{mode}")').item() == pytest.approx(expected)


def test_blend_opacity_and_broadcast():
    base = torch.full((2, 2, 3), 0.5)
    result = _visit('blend(base, [1, 0, 0], "multiply", 0.5)', {"base": base})

    assert result.shape == (2, 2, 3)
    assert torch.allclose(result[0, 0], torch.tensor([0.5, 0.25, 0.25]))


def test_blend_unknown_mode_lists_modes():
    with pytest.raises(ValueError, match="screen"):
        _visit('blend(0.5, 0.8, "nope")')


def test_overlay_blend_mode_only_changes_the_pasted_region():
    base = torch.full((4, 4), 0.5)
    result = _visit('overlay(base, top, [1, 1], 1, "multiply")', {"base": base, "top": torch.full((2, 2), 0.5)})

    assert torch.allclose(result[1:3, 1:3], torch.full((2, 2), 0.25))
    assert result[0, 0] == 0.5


def test_overlay_without_mode_is_unchanged():
    base = torch.zeros(4, 4)
    result = _visit('overlay(base, top, [1, 1], 0.5)', {"base": base, "top": torch.ones(2, 2)})

    assert torch.allclose(result[1:3, 1:3], torch.full((2, 2), 0.5))


def test_overlay_blend_mode_needs_tensors():
    with pytest.raises(ValueError, match="needs tensors"):
        _visit('overlay("hello", "xy", 1, 1, "screen")')


def test_luminance_and_grayscale():
    assert _visit('luminance([1, 1, 1])').item() == pytest.approx(1.0)

    image = torch.rand(1, 2, 2, 4)
    gray = _visit('grayscale(img)', {"img": image})
    luma = 0.2126 * image[..., 0] + 0.7152 * image[..., 1] + 0.0722 * image[..., 2]

    assert gray.shape == image.shape
    assert torch.allclose(gray[..., 1], luma)
    assert torch.equal(gray[..., 3], image[..., 3])
    assert torch.allclose(_visit('luminance(img)', {"img": image}), luma)


def test_distance_transform():
    mask = torch.ones(5, 5)
    mask[0, :] = mask[-1, :] = mask[:, 0] = mask[:, -1] = 0
    result = _visit('distance_transform(m)', {"m": mask})

    assert result.shape == (5, 5)
    assert result[2, 2] == 2.0
    assert result[1, 1] == 1.0
    assert result[0, 0] == 0.0
    assert _visit('distance_transform(m)', {"m": mask.unsqueeze(0)}).shape == (1, 5, 5)


def test_regex_functions():
    assert _visit('regex_search("frame_0042.png", "[0-9]+")') == 6.0
    assert _visit('regex_search("frame.png", "[0-9]+")') == -1.0
    assert _visit('regex_replace("a1b22", "[0-9]+", "#")') == "a#b#"
    assert _visit(r'regex_replace("ab", "(a)", "<\1>")') == "<a>b"


def test_format():
    assert _visit('format(1 / 3, 2)') == "0.33"
    assert _visit('format(x)', {"x": torch.tensor(0.3)}) == "0.3"
    assert _visit('format(x, ".1f")', {"x": torch.tensor([0.5, 1.5])}) == ["0.5", "1.5"]
