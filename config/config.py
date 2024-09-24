# config/config.py

import os
import json

class Config:
    def __init__(self):
        self.config_file = "config/config.json"
        self.config = self._load_config()

    def _load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                return json.load(f)
        return {}  # Return an empty dict if file doesn't exist

    def _save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=2)

    def get_plugin_state(self, plugin_name):
        return self.config["plugins"].get(plugin_name, True)

    def set_plugin_state(self, plugin_name, state):
        self.config["plugins"][plugin_name] = state
        self._save_config()

    def get_database_path(self):
        return self.config["database"]["path"]

    def get_audio_sample_rate(self):
        return self.config["audio_recorder"]["audio"]["sample_rate"]

    def get_audio_chunk_size(self):
        return self.config["audio_recorder"]["audio"]["chunk_size"]

    def get_whisper_model_name(self):
        return self.config["audio_recorder"]["transcription"]["whisper_model"]

    def get_allowed_languages(self):
        return self.config["audio_recorder"]["transcription"]["allowed_languages"]

    def get_min_transcription_confidence(self):
        return self.config["audio_recorder"]["transcription"]["min_confidence"]

    def get_default_user_id(self):
        return self.config["user"]["default_user_id"]

config = Config()

# Use these functions to access configuration values
DATABASE_PATH = config.get_database_path()
WHISPER_MODEL_NAME = config.get_whisper_model_name()
SAMPLE_RATE = config.get_audio_sample_rate()
CHUNK_SIZE = config.get_audio_chunk_size()
DEFAULT_USER_ID = config.get_default_user_id()
ALLOWED_LANGUAGES = config.get_allowed_languages()
MIN_TRANSCRIPTION_CONFIDENCE = config.get_min_transcription_confidence()
