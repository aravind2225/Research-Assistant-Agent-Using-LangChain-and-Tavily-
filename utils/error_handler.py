from tools.metrics_tool import update_errors

from utils.logger import log_event

def handle_error(error):

    update_errors()

    log_event(str(error))

    return f"ERROR: {str(error)}"