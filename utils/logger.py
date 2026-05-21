from datetime import datetime

logs = []

def log_event(message):

    timestamp = datetime.now().strftime("%H:%M:%S")

    logs.append(
        f"[{timestamp}] {message}"
    )

def get_logs():

    return logs