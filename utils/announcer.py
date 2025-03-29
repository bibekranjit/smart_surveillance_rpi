import os
from config import EVENT_MESSAGES

def announce(event_key):
    message = EVENT_MESSAGES.get(event_key, "Alert triggered")
    print(f"[ALERT] {message}")
    # os.system(f"espeak '{message}'")