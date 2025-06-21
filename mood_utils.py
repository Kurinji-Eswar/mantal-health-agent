import os
import json
from datetime import datetime

def detect_mood(text):
    text = text.lower()
    if any(word in text for word in ["happy", "excited", "joy", "great", "awesome"]):
        return "😊 Happy"
    elif any(word in text for word in ["sad", "down", "upset", "depressed"]):
        return "😔 Sad"
    elif any(word in text for word in ["angry", "mad", "furious"]):
        return "😠 Angry"
    elif any(word in text for word in ["anxious", "nervous", "worried"]):
        return "😟 Anxious"
    else:
        return "😐 Neutral"

def save_mood_log(user_id, mood, message, filename='logs/mood_logs.json'):
    entry = {
        "user_id": user_id,
        "mood": mood,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }

    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Load existing data or initialize new
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(entry)

    # Save updated data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
