import os
import unittest
from audio_recording.audio_recorder import AudioRecorder

class TestAudioRecorder(unittest.TestCase):
    def setUp(self):
        self.output_dir = "/path/to/test/audio/output"
        self.recorder = AudioRecorder(output_dir=self.output_dir)

    def tearDown(self):
        # Clean up the test output directory
        for filename in os.listdir(self.output_dir):
            file_path = os.path.join(self.output_dir, filename)
            os.remove(file_path)

    def test_start_stop_recording(self):
        self.recorder.start_recording()
        # Wait for a short duration to allow recording
        import time
        time.sleep(2)
        self.recorder.stop_recording()

        # Check if the audio file was saved
        audio_files = [f for f in os.listdir(self.output_dir) if f.endswith(".wav")]
        self.assertEqual(len(audio_files), 1)

if __name__ == "__main__":
    unittest.main()