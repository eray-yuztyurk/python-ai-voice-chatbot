"""
User Settings (loaded from .env)
Values that can be customized per environment
"""

import os
from dotenv import load_dotenv
from .constants import (
    DEFAULT_STT_MODEL_NAME,
    DEFAULT_LLM_PROVIDER,
    DEFAULT_TTS_RATE,
    DEFAULT_TTS_VOLUME,
    DEFAULT_TTS_PITCH,
    DEFAULT_SERVER_HOST,
    DEFAULT_SERVER_PORT,
    DEFAULT_OPEN_BROWSER,
    DEFAULT_AUDIO_OUTPUT_DIR,
    DEFAULT_AUDIO_INPUT_DIR
)

load_dotenv()

# API Keys (user must provide)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Model selection (user can override)
DEFAULT_STT_MODEL = os.getenv("DEFAULT_STT_MODEL", DEFAULT_STT_MODEL_NAME)
LLM_PROVIDER = os.getenv("DEFAULT_LLM_PROVIDER", DEFAULT_LLM_PROVIDER)

# File paths (user can override)
AUDIO_OUTPUT_DIR = os.getenv("AUDIO_OUTPUT_DIR", DEFAULT_AUDIO_OUTPUT_DIR)
AUDIO_INPUT_DIR = os.getenv("AUDIO_INPUT_DIR", DEFAULT_AUDIO_INPUT_DIR)

# Server settings (user can override)
SERVER_HOST = os.getenv("SERVER_HOST", DEFAULT_SERVER_HOST)
SERVER_PORT = int(os.getenv("SERVER_PORT", str(DEFAULT_SERVER_PORT)))
OPEN_BROWSER = os.getenv("OPEN_BROWSER", str(DEFAULT_OPEN_BROWSER)).lower() == "true"

# TTS voice settings (user can override)
TTS_RATE = os.getenv("TTS_RATE", DEFAULT_TTS_RATE)
TTS_VOLUME = os.getenv("TTS_VOLUME", DEFAULT_TTS_VOLUME)
TTS_PITCH = os.getenv("TTS_PITCH", DEFAULT_TTS_PITCH)
