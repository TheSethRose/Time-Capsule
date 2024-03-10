import os
import time
import unittest
from unittest.mock import patch
from screen_recording.screen_recorder import ScreenRecorder

class TestScreenRecorder(unittest.TestCase):
    def setUp(self):
        self.output_dir = "/path/to/test/output"
        self.recorder = ScreenRecorder(interval=1, output_dir=self.output_dir)

    def tearDown(self):
        # Clean up the test output directory
        for filename in os.listdir(self.output_dir):
            file_path = os.path.join(self.output_dir, filename)
            os.remove(file_path)

    def test_start_stop_recording(self):
        self.recorder.start_recording()
        time.sleep(2)
        self.recorder.stop_recording()

        # Check if screenshots were captured
        screenshots = [f for f in os.listdir(self.output_dir) if f.endswith(".png")]
        self.assertGreater(len(screenshots), 0)

    def test_capture_interval(self):
        self.recorder.start_recording()
        time.sleep(3)
        self.recorder.stop_recording()

        # Check if the number of captured screenshots matches the expected count
        expected_count = 3
        screenshots = [f for f in os.listdir(self.output_dir) if f.endswith(".png")]
        self.assertEqual(len(screenshots), expected_count)

    @patch("os.remove")
    def test_delete_old_screenshots(self, mock_remove):
        # Create dummy screenshot files with different creation times
        now = time.time()
        old_screenshot = os.path.join(self.output_dir, "screenshot_old.png")
        new_screenshot = os.path.join(self.output_dir, "screenshot_new.png")
        open(old_screenshot, "a").close()
        open(new_screenshot, "a").close()
        os.utime(old_screenshot, (now - 3600, now - 3600))  # 1 hour old
        os.utime(new_screenshot, (now, now))  # Current time

        self.recorder._delete_old_screenshots(threshold=1800)  # 30 minutes threshold

        # Check if the old screenshot was deleted
        mock_remove.assert_called_once_with(old_screenshot)

if __name__ == "__main__":
    unittest.main()