# modules/audio_recorder.py

import pyaudio
import numpy as np
import threading
import logging
from config.config import SAMPLE_RATE, CHUNK_SIZE

class AudioRecorder:
    def __init__(self, audio_queue):
        self.audio_queue = audio_queue
        self.sample_rate = SAMPLE_RATE
        self.chunk_size = CHUNK_SIZE
        self.running = False
        self.p = None
        self.stream = None
        self.buffer = np.array([], dtype=np.float32)

    def start_recording(self):
        """Start the audio recording in a separate thread."""
        self.running = True
        self.thread = threading.Thread(target=self.record)
        self.thread.start()
        logging.info("Audio recording started.")

    def stop_recording(self):
        """Stop the audio recording."""
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()
        self._close_stream()
        logging.info("Audio recording stopped.")

    def _close_stream(self):
        """Close the PyAudio stream and terminate PyAudio."""
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        if self.p:
            self.p.terminate()

    def record(self):
        """Continuously record audio and put audio data into the queue."""
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
            logging.error(f"Error recording audio: {e}", exc_info=True)
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
