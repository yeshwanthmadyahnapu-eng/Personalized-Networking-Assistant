import json
import os

HISTORY_FILE = "database/history.json"
FEEDBACK_FILE = "database/feedback.json"


def save_history(data):
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)

    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)

    # Prevent duplicate consecutive entries
    if len(history) > 0:
        last = history[-1]
        if (
            last["title"] == data["title"] and
            last["description"] == data["description"]
        ):
            return

    history.append(data)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)


def save_feedback(data):
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w") as f:
            json.dump([], f)

    with open(FEEDBACK_FILE, "r") as f:
        feedback = json.load(f)

    feedback.append(data)

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(feedback, f, indent=4)

def load_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return []

    with open(FEEDBACK_FILE, "r") as f:
        return json.load(f)