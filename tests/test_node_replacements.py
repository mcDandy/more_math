import asyncio

import pytest
from comfy_api.latest import io

from more_math.nodes import MoreMathExtension
from more_math.node_replacements import REPLACEMENTS, make_replacement

SCHEMAS = {node.GET_SCHEMA().node_id: node.GET_SCHEMA() for node in asyncio.run(MoreMathExtension.get_node_list())}


@pytest.mark.parametrize("replacement", REPLACEMENTS, ids=[r[0] for r in REPLACEMENTS])
def test_replacement_matches_schemas(replacement):
    node_replace = make_replacement(*replacement).as_dict()
    old = SCHEMAS[node_replace["old_node_id"]]
    new = SCHEMAS[node_replace["new_node_id"]]
    new_inputs = {i.id: i for i in new.inputs}

    # Saved workflows store widget values by position; force_input floats have no widget
    assert node_replace["old_widget_ids"] == [i.id for i in old.inputs if isinstance(i, (io.String.Input, io.Combo.Input))]
    assert sorted(m["old_id"] for m in node_replace["input_mapping"]) == sorted(i.id for i in old.inputs)
    for mapping in node_replace["input_mapping"]:
        top, _, sub = mapping["new_id"].partition(".")
        assert top in new_inputs
        if sub:
            template = new_inputs[top].template
            assert sub.startswith(template.prefix) and int(sub[len(template.prefix):]) < template.max
    assert len(old.outputs) == 1 and type(new.outputs[0]) is type(old.outputs[0])


def test_every_deprecated_node_has_a_replacement():
    deprecated = {node_id for node_id, schema in SCHEMAS.items() if schema.is_deprecated}
    assert deprecated == {r[0] for r in REPLACEMENTS}
