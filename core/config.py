"""Configuration for WinApt"""
import os
import json

CONFIG_DIR = os.path.expanduser("~/.winapt")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
CACHE_DIR = os.path.join(CONFIG_DIR, "cache")

DEFAULT_CONFIG = {
    "sources": ["winget", "choco"],
    "priority": "winget",
    "cache_ttl": 3600,
    "color_output": True,
    "confirm_install": True,
    "simulate": False
}

def ensure_dirs():
    os.makedirs(CONFIG_DIR, exist_ok=True)
    os.makedirs(CACHE_DIR, exist_ok=True)

def load_config():
    ensure_dirs()
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
            # Merge with defaults
            for key, value in DEFAULT_CONFIG.items():
                if key not in config:
                    config[key] = value
            return config
    return DEFAULT_CONFIG.copy()

def save_config(config):
    ensure_dirs()
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
