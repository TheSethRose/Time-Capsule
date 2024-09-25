# plugins/audio_recorder/audio_recorder.py

import pyaudio
import numpy as np
import threading
import logging
import os
import queue
from modules.config_manager import config
from .transcription_service import TranscriptionService

class AudioRecorder:
    """Class for recording audio and managing the transcription service."""
    def __init__(self):
        self.audio_queue = queue.Queue()
        self.sample_rate = config.get_audio_sample_rate()
        self.chunk_size = config.get_audio_chunk_size()
        self.running = False
        self.p = None
        self.stream = None
        self.buffer = np.array([], dtype=np.float32)
        self.transcription_service = TranscriptionService()
        self.model_path = os.path.join(os.path.dirname(__file__), 'model')

    def start(self, db_manager):
        """Start the audio recorder and transcription service."""
        logging.debug("Starting AudioRecorder")
        self.running = True

        # Ensure the model is initialized before starting
        self._initialize_model()

        self.thread = threading.Thread(target=self.record)
        self.thread.start()
        self.transcription_service.start(self.audio_queue, db_manager)
        logging.debug("AudioRecorder started")

    def _initialize_model(self):
        model_name = config.get_whisper_model_name()
        if not os.path.exists(self.model_path):
            os.makedirs(self.model_path)
            logging.info(f"Created model directory: {self.model_path}")

        self.transcription_service.initialize_model(model_name, self.model_path)

    def stop(self):
        """Stop the audio recorder and transcription service."""
        logging.debug("Stopping AudioRecorder")
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()
        self._close_stream()
        self.transcription_service.stop()
        logging.debug("AudioRecorder stopped")

    def _close_stream(self):
        """Close the audio stream and terminate PyAudio."""
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        if self.p:
            self.p.terminate()

    def record(self):
        """Record audio and put chunks into the queue."""
        logging.debug("Starting audio recording")
        self.p = pyaudio.PyAudio()
        try:
            self.stream = self.p.open(format=pyaudio.paFloat32,
                                      channels=1,
                                      rate=self.sample_rate,
                                      input=True,
                                      frames_per_buffer=self.chunk_size,
                                      stream_callback=self._audio_callback)

            self.stream.start_stream()

            while self.running:
                if not self.stream.is_active():
                    break
                threading.Event().wait(0.1)  # Sleep to reduce CPU usage

        except Exception as e:
            logging.error(f"Error in audio recording: {str(e)}", exc_info=True)
        finally:
            self._close_stream()
            self.running = False

    def _audio_callback(self, in_data, frame_count, time_info, status):
        """Callback function for processing audio stream data."""
        if status:
            logging.warning(f"PyAudio callback status: {status}")

        audio_data = np.frombuffer(in_data, dtype=np.float32)
        self.buffer = np.concatenate((self.buffer, audio_data))

        # Put 3 seconds of audio into the queue
        if len(self.buffer) >= self.sample_rate * 3:
            self.audio_queue.put(self.buffer[:self.sample_rate * 3].copy())
            self.buffer = self.buffer[self.sample_rate * 3:]

        return (in_data, pyaudio.paContinue)

    def is_running(self):
        """Check if the audio recorder and transcription service are running."""
        return self.running and self.transcription_service.is_running()
