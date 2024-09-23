# config/config.py

import os

# Database configuration
DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'chroma_db')

# Whisper model configuration
WHISPER_MODEL_NAME = "base"

# Audio configuration
SAMPLE_RATE = 16000
CHUNK_SIZE = 1024

# User configuration
DEFAULT_USER_ID = 1

# Transcription configuration
ALLOWED_LANGUAGES = ["en"]  # Add more language codes as needed (ex. ["en", "es", "fr"])
MIN_TRANSCRIPTION_CONFIDENCE = 0.5  # Minimum confidence score to accept a transcription
