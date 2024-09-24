# plugins/audio_recorder/audio_recorder.py

import pyaudio
import numpy as np
import threading
import logging
from config.config import config
from .transcription_service import TranscriptionService

class AudioRecorder:
    def __init__(self):
        self.audio_queue = None
        self.sample_rate = config.get_audio_sample_rate()
        self.chunk_size = config.get_audio_chunk_size()
        self.running = False
        self.p = None
        self.stream = None
        self.buffer = np.array([], dtype=np.float32)
        self.transcription_service = TranscriptionService()

    def start(self, audio_queue, db_manager):
        logging.debug("Starting AudioRecorder")
        self.audio_queue = audio_queue
        self.running = True
        self.thread = threading.Thread(target=self.record)
        self.thread.start()
        self.transcription_service.start(audio_queue, db_manager)
        logging.debug("AudioRecorder started")

    def stop(self):
        logging.debug("Stopping AudioRecorder")
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()
        self._close_stream()
        self.transcription_service.stop()
        logging.debug("AudioRecorder stopped")

    def _close_stream(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        if self.p:
            self.p.terminate()

    def record(self):
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
        return self.running and self.transcription_service.is_running()
