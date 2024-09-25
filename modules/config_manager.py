# Configuration manager for loading and saving application settings

import os
import json

class Config:
    """Configuration manager for loading and saving application settings."""
    def __init__(self):
        # Path to config.json in the main directory
        self.config_file = "config.json"
        self.config = self._load_config()

    def _load_config(self):
        """Load the configuration from the JSON file."""
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                return json.load(f)
        return {}  # Return an empty dict if file doesn't exist

    def _save_config(self):
        """Save the current configuration to the JSON file."""
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=2)

    def get_plugin_state(self, plugin_name):
        """Get the enabled state of a plugin."""
        return self.config["plugins"].get(plugin_name, True)

    def set_plugin_state(self, plugin_name, state):
        """Set the enabled state of a plugin."""
        self.config["plugins"][plugin_name] = state
        self._save_config()

    def get_database_path(self):
        """Get the path to the database."""
        return self.config["database"]["path"]

    def get_audio_sample_rate(self):
        """Get the audio sample rate."""
        return self.config["audio_recorder"]["audio"]["sample_rate"]

    def get_audio_chunk_size(self):
        """Get the audio chunk size."""
        return self.config["audio_recorder"]["audio"]["chunk_size"]

    def get_whisper_model_name(self):
        """Get the name of the Whisper model."""
        return self.config["audio_recorder"]["transcription"]["whisper_model"]

    def get_allowed_languages(self):
        """Get the list of allowed languages for transcription."""
        return self.config["audio_recorder"]["transcription"]["allowed_languages"]

    def get_min_transcription_confidence(self):
        """Get the minimum confidence score for transcriptions."""
        return self.config["audio_recorder"]["transcription"]["min_confidence"]

    def get_default_user_id(self):
        """Get the default user ID."""
        return self.config["user"]["default_user_id"]

    def get_refresh_interval(self):
        """Get the refresh interval for the web interface."""
        return self.config.get("refresh_interval", 5)  # Default to 5 if not specified

config = Config()

# Use these functions to access configuration values
DATABASE_PATH = config.get_database_path()
WHISPER_MODEL_NAME = config.get_whisper_model_name()
SAMPLE_RATE = config.get_audio_sample_rate()
CHUNK_SIZE = config.get_audio_chunk_size()
DEFAULT_USER_ID = config.get_default_user_id()
ALLOWED_LANGUAGES = config.get_allowed_languages()
MIN_TRANSCRIPTION_CONFIDENCE = config.get_min_transcription_confidence()
