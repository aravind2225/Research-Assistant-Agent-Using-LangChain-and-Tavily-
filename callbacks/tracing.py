from langchain_core.callbacks import BaseCallbackHandler

from utils.logger import log_event

class ResearchTracer(BaseCallbackHandler):

    def on_chain_start(self, serialized, inputs, **kwargs):

        log_event("Chain Started")

    def on_chain_end(self, outputs, **kwargs):

        log_event("Chain Completed")

    def on_tool_start(self, serialized, input_str, **kwargs):

        log_event(f"Tool Started: {serialized}")

    def on_tool_end(self, output, **kwargs):

        log_event("Tool Completed")

    def on_llm_start(self, serialized, prompts, **kwargs):

        log_event("LLM Started")

    def on_llm_end(self, response, **kwargs):

        log_event("LLM Completed")