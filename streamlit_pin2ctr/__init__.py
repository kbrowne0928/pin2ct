import os
import streamlit.components.v1 as components

_component_func = components.declare_component(
    "gauge_meter",
    url="http://localhost:3001",
)


def st_gauge_chart(label: str, value: int = 0, key=None):
    component_value = _component_func(label=label, initialValue=[value], key=key, default=[value])
    return component_value[0]