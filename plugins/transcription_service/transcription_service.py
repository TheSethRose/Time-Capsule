# modules/transcription_service.py

from faster_whisper import WhisperModel
import numpy as np
import threading
import queue
import logging
import time
from config.config import WHISPER_MODEL_NAME, DEFAULT_USER_ID, ALLOWED_LANGUAGES, MIN_TRANSCRIPTION_CONFIDENCE

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress Whisper model's internal logging
logging.getLogger("faster_whisper").setLevel(logging.WARNING)

class TranscriptionService:
    def __init__(self, audio_queue, db_manager):
        self.audio_queue = audio_queue
        self.db_manager = db_manager
        self.model = WhisperModel(WHISPER_MODEL_NAME, device="cpu", compute_type="int8")
        self.running = False

    def start_transcription(self):
        """Start the transcription service in a separate thread."""
        self.running = True
        self.thread = threading.Thread(target=self.transcribe)
        self.thread.start()

    def stop_transcription(self):
        """Stop the transcription service."""
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join(timeout=5)

    def transcribe(self):
        """Continuously process audio chunks and perform transcription."""
        try:
            while self.running:
                try:
                    audio_chunk = self.audio_queue.get(timeout=1)
                    if audio_chunk.dtype != np.float32:
                        audio_chunk = audio_chunk.astype(np.float32)

                    segments, info = self.model.transcribe(audio_chunk, beam_size=5)

                    if info.language in ALLOWED_LANGUAGES and info.language_probability >= MIN_TRANSCRIPTION_CONFIDENCE:
                        transcription = " ".join(segment.text for segment in segments).strip()
                        if transcription:  # Only process non-empty transcriptions
                            logging.info(f"'{transcription}' (Language: {info.language}, Confidence: {info.language_probability:.2f})")
                            self.db_manager.add_command(user_id=DEFAULT_USER_ID, command_text=transcription)

                except queue.Empty:
                    time.sleep(0.1)

        except Exception as e:
            logging.error(f"Error during transcription: {e}", exc_info=True)
