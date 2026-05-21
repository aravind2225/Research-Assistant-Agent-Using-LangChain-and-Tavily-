import streamlit as st

from datetime import datetime

from langchain.tools import tool

# =========================================================
# SESSION STATE
# =========================================================

if "research_history" not in st.session_state:

    st.session_state.research_history = []

# =========================================================
# SAVE NOTE
# =========================================================

def save_note(query, results):

    st.session_state.research_history.append(
        {
            "query": query,

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "results": results
        }
    )

# =========================================================
# LOAD NOTES
# =========================================================

def load_notes():

    return st.session_state.research_history

# =========================================================
# TOOL
# =========================================================

@tool
def get_saved_notes(dummy: str = "") -> str:
    """
    Retrieve previously saved research notes
    from current user session.
    """

    notes = load_notes()

    if not notes:

        return "No saved notes available."

    formatted = ""

    for note in notes[-3:]:

        formatted += f"""
Query:
{note['query']}

Timestamp:
{note['timestamp']}
"""

    return formatted