import time

import streamlit as st

from agents.research_agent import create_research_agent

from tools.metrics_tool import (
    get_metrics,
    update_response_time
)

from tools.notes_tool import load_notes

from utils.logger import get_logs
from utils.error_handler import handle_error

from ui.streamlit_components import (
    render_header,
    render_sidebar
)

# =========================================================
# SESSION STATE
# =========================================================

if "latest_response" not in st.session_state:

    st.session_state.latest_response = ""

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Research Assistant",
    layout="wide"
)

# =========================================================
# UI
# =========================================================

render_header()

page = render_sidebar()

# =========================================================
# AGENT
# =========================================================

agent = create_research_agent()

# =========================================================
# PAGE : RESEARCH ASSISTANT
# =========================================================

if page == "Research Assistant":

    query = st.text_area(
        "Enter your research query",
        height=150
    )

    if st.button("Run Research"):

        if query:

            start = time.time()

            try:

                with st.spinner("Researching..."):

                    response = agent.invoke(
                        {
                            "input": query
                        }
                    )

                    elapsed = round(
                        time.time() - start,
                        2
                    )

                    update_response_time(elapsed)

                    final_answer = response["output"]

                    st.session_state.latest_response = final_answer

                    # st.success("Research Completed")

                    # st.subheader("🧠 Final Answer")

                    # st.write(st.session_state.latest_response)

            except Exception as e:

                st.error(
                    handle_error(e)
                )

    # =====================================================
    # DOWNLOAD CURRENT RESULT
    # =====================================================

    if st.session_state.latest_response:
        st.success("Research Completed")

        st.subheader("🧠 Final Answer")

        st.write(st.session_state.latest_response)


        st.download_button(
            label="⬇️ Download Result",
            data=st.session_state.latest_response,
            file_name="research_result.md",
            mime="text/markdown"
        )

    # =====================================================
    # METRICS
    # =====================================================

    metrics = get_metrics()

    st.subheader("📊 Metrics")

    m1, m2, m3 = st.columns(3)

    m1.metric(
        "Tool Calls",
        metrics["tool_calls"]
    )

    m2.metric(
        "Errors",
        metrics["errors"]
    )

    m3.metric(
        "Response Time",
        f"{metrics['response_time']} sec"
    )

# =========================================================
# PAGE : EXECUTION TRACE
# =========================================================

elif page == "Execution Trace":

    st.header("🛠 Execution Trace")

    logs = get_logs()

    if not logs:

        st.info("No execution traces available.")

    for log in logs[::-1]:

        st.code(log)

# =========================================================
# PAGE : SAVED RESEARCH NOTES
# =========================================================

elif page == "Saved Research Notes":

    st.header("📝 Saved Research Notes")

    notes = load_notes()

    if not notes:

        st.info("No research notes available.")

    for idx, note in enumerate(notes[::-1]):

        with st.expander(note["query"]):

            st.write(
                note.get(
                    "timestamp",
                    "Timestamp unavailable"
                )
            )

            markdown_content = f"""
            # Research Note

            ## Query

            {note['query']}

            ## Timestamp

            {note.get("timestamp")}

            """

            for result in note["results"]:

                st.markdown(
                    f"""
                    ### {result.get("title")}

                    {result.get("content")}

                    {result.get("url")}
                    """
                )

                markdown_content += f"""
                ## {result.get("title")}

                {result.get("content")}

                URL:
                {result.get("url")}

                ---
                """

            # =============================================
            # DOWNLOAD BUTTON FOR EACH NOTE
            # =============================================

            st.download_button(
                label=f"⬇️ Download Note {idx+1}",
                data=markdown_content,
                file_name=f"research_note_{idx+1}.md",
                mime="text/markdown",
                key=f"download_{idx}"
            )