# import os
# import time
# from dotenv import load_dotenv

# from tavily import TavilyClient

# from langchain.tools import tool

# from tenacity import retry
# from tenacity import stop_after_attempt
# from tenacity import wait_fixed

# from utils.logger import log_event

# from tools.notes_tool import save_note
# from tools.metrics_tool import update_tool_calls
# load_dotenv()
# client = TavilyClient(
#     api_key=os.getenv("TAVILY_API_KEY")
# )

# # =========================================================
# # SEARCH
# # =========================================================

# @retry(
#     stop=stop_after_attempt(3),
#     wait=wait_fixed(2)
# )
# def search_web(query: str):

#     start = time.time()

#     log_event(f"Searching web: {query}")

#     response = client.search(
#         query=query,
#         max_results=6,
#         search_depth="advanced"
#     )

#     elapsed = round(time.time() - start, 2)

#     log_event(f"Search completed in {elapsed}s")

#     update_tool_calls()

#     return response["results"]

# # =========================================================
# # TOOL
# # =========================================================

# @tool
# def tavily_search_tool(query: str) -> str:
#     """
#     Search the web for latest information,
#     AI trends, research topics,
#     comparisons, and news.
#     """

#     try:

#         results = search_web(query)

#         compressed_results = []

#         for item in results:

#             compressed_results.append(
#                 {
#                     "title": item.get("title"),
#                     "url": item.get("url"),
#                     "content": item.get("content", "")[:200]
#                 }
#             )

#         save_note(query, compressed_results)

#         formatted = ""

#         for idx, item in enumerate(results, start=1):

#             title = item.get("title", "")

#             url = item.get("url", "")

#             content = item.get("content", "")

#             # IMPORTANT:
#             # LIMIT CONTENT SIZE

#             content = content[:400]

#             formatted += f"""
#             Source {idx}

#             Title:
#             {title}

#             URL:
#             {url}

#             Summary:
#             {content}

#             """

#         return formatted

#     except Exception as e:

#         log_event(f"Tool Error: {str(e)}")

#         return f"Search failed: {str(e)}"

import os
import time

from tavily import TavilyClient
from dotenv import load_dotenv
from langchain.tools import tool

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_fixed

from utils.logger import log_event

from tools.notes_tool import save_note
from tools.metrics_tool import update_tool_calls
load_dotenv()
client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

# =========================================================
# SEARCH
# =========================================================

@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2)
)
def search_web(query: str):

    start = time.time()

    log_event(f"Searching web: {query}")

    response = client.search(
        query=query,
        max_results=3
    )

    elapsed = round(time.time() - start, 2)

    log_event(f"Search completed in {elapsed}s")

    update_tool_calls()

    return response["results"]

# =========================================================
# TOOL
# =========================================================

@tool
def tavily_search_tool(query: str) -> str:
    """
    Search the web for latest information,
    AI trends, research topics,
    comparisons, and news.
    """

    try:

        results = search_web(query)

        compressed_results = []

        formatted = ""

        for idx, item in enumerate(results, start=1):

            title = item.get("title", "")

            url = item.get("url", "")

            content = item.get("content", "")[:300]

            compressed_results.append(
                {
                    "title": title,
                    "url": url,
                    "content": content
                }
            )

            formatted += f"""
Source {idx}

Title:
{title}

URL:
{url}

Summary:
{content}

"""

        save_note(
            query,
            compressed_results
        )

        return formatted

    except Exception as e:

        log_event(f"Tool Error: {str(e)}")

        return f"Search failed: {str(e)}"