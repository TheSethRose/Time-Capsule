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
        logging.info("Audio recording stopped.")

    def record(self):
        """Continuously record audio and put audio data into the queue."""
        p = pyaudio.PyAudio()
        try:
            stream = p.open(format=pyaudio.paFloat32,
                            channels=1,
                            rate=self.sample_rate,
                            input=True,
                            frames_per_buffer=self.chunk_size)

            buffer = np.array([], dtype=np.float32)
            while self.running:
                data = stream.read(self.chunk_size)
                audio_data = np.frombuffer(data, dtype=np.float32)
                buffer = np.concatenate((buffer, audio_data))

                # Put 3 seconds of audio into the queue
                if len(buffer) >= self.sample_rate * 3:
                    self.audio_queue.put(buffer.copy())
                    buffer = np.array([], dtype=np.float32)

        except Exception as e:
            logging.error(f"Error recording audio: {e}", exc_info=True)
        finally:
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            p.terminate()
            self.running = False
