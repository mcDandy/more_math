"""Color math node using integer color representation."""

from __future__ import annotations

import copy
from typing import Any

import torch
from comfy_api.latest import io

from .ParseTree import MrmthParseTree
from .Parser.UnifiedMathVisitor import UnifiedMathVisitor
from .Stack import MrmthStack
from .helper_functions import checkLazyNew, get_f_variable, get_v_variable, parse_expr


class ColorMathNode(io.ComfyNode):
    """Apply expression math to Color values converted to packed RGB integers."""

    @classmethod
    def define_schema(cls) -> io.Schema:
        """Define node schema."""
        return io.Schema(
            node_id="mrmth_ag_ColorMathNode",
            category="More math",
            display_name="Color math",
            inputs=[
                io.Autogrow.Input(id="V", template=io.Autogrow.TemplatePrefix(io.Color.Input("values"), prefix="V", min=1, max=50)),
                io.Autogrow.Input(id="F", template=io.Autogrow.TemplatePrefix(io.Float.Input("float", default=0.0, optional=True, lazy=True, force_input=True), prefix="F", min=1, max=50)),

                io.MultiType.Input(
                    io.String.Input("Expression", default="V0", multiline=False),
                    types=[io.String, MrmthParseTree],
                    tooltip="Expression evaluated over packed color integers.",
                ),
                io.Boolean.Input(
                    id="remember_stack",
                    default=False,
                    display_name="Remember stack across batch",
                ),
                MrmthStack.Input(
                    id="stack",
                    tooltip="Access stack between nodes",
                    optional=True,
                ),
            ],
            outputs=[
                io.Color.Output(id="color"),
                MrmthStack.Output(),
            ],
        )

    @staticmethod
    def _hex_to_int(color_hex: str) -> int:
        """Convert #RRGGBB/#RRGGBBAA into packed ARGB 0xAARRGGBB."""
        s = str(color_hex).strip()
        if not s.startswith("#"):
            raise ValueError(f"Invalid color format: {color_hex}")
        s = s[1:]

        if len(s) == 6:  # RRGGBB
            rr = int(s[0:2], 16)
            gg = int(s[2:4], 16)
            bb = int(s[4:6], 16)
            aa = 0xFF
        elif len(s) == 8:  # RRGGBBAA
            rr = int(s[0:2], 16)
            gg = int(s[2:4], 16)
            bb = int(s[4:6], 16)
            aa = int(s[6:8], 16)
        else:
            raise ValueError(f"Invalid color format: {color_hex}")

        return ((aa & 0xFF) << 24) | ((rr & 0xFF) << 16) | ((gg & 0xFF) << 8) | (bb & 0xFF)

    @staticmethod
    def _int_to_hex(value: int) -> str:
        """Convert packed ARGB 0xAARRGGBB into #RRGGBBAA."""
        v = int(value) & 0xFFFFFFFF
        aa = (v >> 24) & 0xFF
        rr = (v >> 16) & 0xFF
        gg = (v >> 8) & 0xFF
        bb = v & 0xFF
        return f"#{rr:02x}{gg:02x}{bb:02x}{aa:02x}"

    @classmethod
    def check_lazy_status(
        cls,
        Expression: Any,
        V: dict[str, str],
        F: dict[str, float],
        remember_stack: bool = False,
        stack: dict | None = None,
    ) -> list[str]:
        """Return unresolved lazy inputs for expression."""
        return checkLazyNew(Expression, V, F)

    @classmethod
    def execute(
        cls,
        V: dict[str, str],
        F: dict[str, float],
        Expression: Any,
        remember_stack: bool = False,
        stack: dict | None = None,
    ) -> io.NodeOutput:
        """Execute color expression and return resulting color."""
        print(V)
        print("---")
        work_stack = stack if remember_stack else (
            copy.deepcopy(stack) if stack is not None else {}
        )

       # if not V:
      #      raise ValueError("At least one color input is required.")

        variables: dict[str, Any] = {}

        # Legacy aliases.
        variables["a"] = cls._hex_to_int(V.get("V0", "#000000"))
        variables["b"] = cls._hex_to_int(V.get("V1", "#000000"))
        variables["c"] = cls._hex_to_int(V.get("V2", "#000000"))
        variables["d"] = cls._hex_to_int(V.get("V3", "#000000"))

        # All color inputs as packed ints.
        color_int_inputs: dict[str, int] = {}
        for k, val in V.items():
            color_int_inputs[k] = cls._hex_to_int(val if val is not None else "#000000")
            variables[k] = color_int_inputs[k]

        v_stacked, v_cnt = get_v_variable(color_int_inputs, length_mismatch="do nothing")
        if v_stacked is not None:
            variables["V"] = v_stacked
            variables["Vcnt"] = float(v_cnt)
            variables["V_count"] = float(v_cnt)

        # Float aliases and F array.
        variables["w"] = F.get("F0", 0.0) if F.get("F0") is not None else 0.0
        variables["x"] = F.get("F1", 0.0) if F.get("F1") is not None else 0.0
        variables["y"] = F.get("F2", 0.0) if F.get("F2") is not None else 0.0
        variables["z"] = F.get("F3", 0.0) if F.get("F3") is not None else 0.0

        f_stacked, f_cnt = get_f_variable(F)
        if f_stacked is not None:
            variables["F"] = f_stacked
            variables["Fcnt"] = float(f_cnt)
            variables["F_count"] = float(f_cnt)

        for k, val in F.items():
            variables[k] = val if val is not None else 0.0

        tree = parse_expr(Expression) if isinstance(Expression, str) else Expression

        visitor = UnifiedMathVisitor(
            variables=variables,
            shape=(1,),
            device=torch.device("cpu"),
            state_storage=work_stack,
        )
        result = visitor.visit(tree)
        out_color = cls._int_to_hex(result)

        returned_stack = work_stack if remember_stack else copy.deepcopy(work_stack)
        return io.NodeOutput(out_color, returned_stack)
