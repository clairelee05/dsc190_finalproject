import json
from pathlib import Path

CONFIG_PATH = Path.home() / ".email_tool_config.json"


def load_config():
    if not CONFIG_PATH.exists():
        return {"content": []}

    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)
