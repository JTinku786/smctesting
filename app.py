import subprocess
import sys

import streamlit as st

st.title("SMC Import Check")

try:
    import smartmoneyconcepts as smc  # noqa: F401
    st.success("smartmoneyconcepts imported successfully.")
except Exception as exc:
    st.error("smartmoneyconcepts import failed.")
    st.code(f"{type(exc).__name__}: {exc}")
    st.info(
        "Install dependency in your environment before starting the app:\n"
        "pip install smartmoneyconcepts --no-deps"
    )
