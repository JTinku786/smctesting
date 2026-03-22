import subprocess
import sys

import streamlit as st


def ensure_smartmoneyconcepts() -> bool:
    """Install smartmoneyconcepts without dependencies if it's missing."""
    try:
        import smartmoneyconcepts  # noqa: F401
        return True
    except ModuleNotFoundError:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "smartmoneyconcepts", "--no-deps"]
            )
            import smartmoneyconcepts  # noqa: F401
            return True
        except Exception:
            return False


st.title("SMC Import Check")
if ensure_smartmoneyconcepts():
    st.success("smartmoneyconcepts is available.")
else:
    st.error(
        "smartmoneyconcepts could not be imported or installed. "
        "Try running: pip install smartmoneyconcepts --no-deps"
    )
