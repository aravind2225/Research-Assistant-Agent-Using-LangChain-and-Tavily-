from tools.tavily_search import tavily_search_tool
from tools.notes_tool import get_saved_notes

def get_tools():

    return [
        tavily_search_tool,
        get_saved_notes
    ]