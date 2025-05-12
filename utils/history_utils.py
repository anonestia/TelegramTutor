import os
import json
from datetime import datetime
import pytz

JAKARTA_TZ = pytz.timezone("Asia/Jakarta")

def ensure_chat_history_folder():
    os.makedirs("chat_history", exist_ok=True)

def get_history_file_path(chat_id: int, user_id: int, is_group: bool) -> str:
    ensure_chat_history_folder()
    filename = f"{chat_id}.json" if is_group else f"{user_id}.json"
    return os.path.join("chat_history", filename)

def load_history(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_history(file_path, history):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def format_history(history):
    formatted = []
    for entry in history:
        user_part = f"(User ID: <@{entry['user_id']}>) {entry['user_display']} at {entry['timestamp']}: {entry['user_message']}" if 'user_message' in entry else ""
        ai_part = f"Deva (You) at {entry['timestamp']}: {entry['ai_response']}" if 'ai_response' in entry else ""
        system_part = f"System entry at {entry['timestamp']}: {entry['system_message']}" if 'system_message' in entry else ""
        dialogue = "\n".join(part for part in [user_part, ai_part, system_part] if part)
        if dialogue:
            formatted.append(dialogue)
    return "\n".join(formatted)

def add_to_history(history, user_id, user_display, user_message=None, ai_response=None, system_message=None, limit=15):
    timestamp = datetime.now(JAKARTA_TZ).strftime('%Y-%m-%d %H:%M:%S')
    entry = {
        "user_id": user_id,
        "user_display": user_display,
        "timestamp": timestamp
    }
    if user_message: entry["user_message"] = user_message
    if ai_response: entry["ai_response"] = ai_response
    if system_message: entry["system_message"] = system_message

    history.append(entry)
    if len(history) > limit:
        history = history[-limit:]
    return history

def clear_history_file(file_path):
    with open(file_path, 'w') as f:
        json.dump([], f)
