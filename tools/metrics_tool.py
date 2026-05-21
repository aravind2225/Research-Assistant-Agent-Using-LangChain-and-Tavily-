metrics = {
    "tool_calls": 0,
    "errors": 0,
    "response_time": 0
}

def update_tool_calls():

    metrics["tool_calls"] += 1

def update_errors():

    metrics["errors"] += 1

def update_response_time(value):

    metrics["response_time"] = value

def get_metrics():

    return metrics