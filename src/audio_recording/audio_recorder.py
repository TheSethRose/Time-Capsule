import os
import time
import threading
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

class AudioRecorder:
    def __init__(self, output_dir="/Users/sethrose/Documents/Development/Repositories/time-capsule/recordings/audio", sample_rate=44100, save_interval=300):
        self.output_dir = output_dir
        self.sample_rate = sample_rate
        self.save_interval = save_interval
        self.recording = False
        self.audio_data = []
        self.record_thread = None
        self.save_thread = None

        # Create the output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def start_recording(self):
        self.recording = True
        self.audio_data = []
        self.record_thread = threading.Thread(target=self._record_audio)
        self.save_thread = threading.Thread(target=self._save_audio_interval)
        self.record_thread.start()
        self.save_thread.start()
        print("Audio recording started.")

    def stop_recording(self):
        self.recording = False
        if self.record_thread is not None:
            self.record_thread.join()
        if self.save_thread is not None:
            self.save_thread.join()
        self._save_audio()
        print("Audio recording stopped.")

    def _record_audio(self):
        with sd.Stream(samplerate=self.sample_rate, callback=self._audio_callback):
            while self.recording:
                time.sleep(0.1)

    def _audio_callback(self, indata, outdata, frames, time, status):
        if status:
            print(status)
        self.audio_data.append(indata.copy())

    def _save_audio_interval(self):
        while self.recording:
            time.sleep(self.save_interval)
            self._save_audio()

    def _save_audio(self):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"audio_{timestamp}.wav"
        filepath = os.path.join(self.output_dir, filename)
        audio_data = np.concatenate(self.audio_data, axis=0)
        write(filepath, self.sample_rate, audio_data)
        self.audio_data = []
        print(f"Audio saved: {filepath}")