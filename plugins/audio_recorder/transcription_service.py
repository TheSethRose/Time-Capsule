import threading
from faster_whisper import WhisperModel
from modules.config_manager import config
import logging
import numpy as np
import queue
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Suppress Whisper model's internal logging
logging.getLogger("faster_whisper").setLevel(logging.WARNING)

class TranscriptionService:
    """Service for transcribing audio using the Whisper model."""
    def __init__(self):
        self.audio_queue = None
        self.db_manager = None
        self.model = None
        self.running = False
        self.thread = None

    def start(self, audio_queue, db_manager):
        """Start the transcription service."""
        self.audio_queue = audio_queue
        self.db_manager = db_manager
        model_name = config.get_whisper_model_name()
        logging.info(f"Loading Whisper model: {model_name}")
        try:
            self.model = WhisperModel(model_name, device="cpu", compute_type="int8")
            logging.info("Whisper model loaded successfully")
        except Exception as e:
            logging.error(f"Error loading Whisper model: {str(e)}")
            raise
        self.allowed_languages = config.get_allowed_languages()
        self.min_confidence = config.get_min_transcription_confidence()
        self.running = True
        self.thread = threading.Thread(target=self._transcribe)
        self.thread.start()

    def _transcribe(self):
        """Internal method to handle the transcription process."""
        try:
            while self.running:
                try:
                    # Get audio chunk from the queue
                    audio_chunk = self.audio_queue.get(timeout=1)
                    if audio_chunk.dtype != np.float32:
                        audio_chunk = audio_chunk.astype(np.float32)

                    # Transcribe the audio chunk
                    segments, info = self.model.transcribe(audio_chunk, beam_size=5)

                    # Check if the transcription meets the confidence and language criteria
                    if info.language in self.allowed_languages and info.language_probability >= self.min_confidence:
                        transcription = " ".join(segment.text for segment in segments).strip()
                        if transcription:  # Only process non-empty transcriptions
                            logging.info(f"Transcribed: '{transcription}' (Language: {info.language}, Confidence: {info.language_probability:.2f})")
                            self.db_manager.store_transcription(transcription, info.language, info.language_probability)

                except queue.Empty:
                    time.sleep(0.1)

        except Exception as e:
            logging.error(f"Error during transcription: {str(e)}", exc_info=True)

    def stop(self):
        """Stop the transcription service."""
        self.running = False
        if self.thread:
            self.thread.join(timeout=5)

    def is_running(self):
        """Check if the transcription service is running."""
        return self.running
