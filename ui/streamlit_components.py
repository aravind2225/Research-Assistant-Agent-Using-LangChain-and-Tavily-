import streamlit as st

# =========================================================
# HEADER
# =========================================================

def render_header():

    st.title("🔎 Research Assistant Agent")

    st.markdown("""
    AI Research Assistant using:
    - LangChain
    - Qwen 32B
    - Tavily
    - Streamlit
    """)

# =========================================================
# SIDEBAR
# =========================================================

def render_sidebar():

    st.sidebar.title("📌 Navigation")

    page = st.sidebar.radio(
        "Go To",
        [
            "Research Assistant",
            "Execution Trace",
            "Saved Research Notes"
        ]
    )

    st.sidebar.divider()

    st.sidebar.success(
        "Model: qwen/qwen3-32b"
    )

    st.sidebar.info(
        "Temperature: 0.0"
    )

    return page