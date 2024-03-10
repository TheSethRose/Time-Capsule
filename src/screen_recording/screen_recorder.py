import os
import threading
import time
import numpy as np
import pyautogui
from PIL import Image
from datetime import datetime, timedelta
import ffmpeg
import cv2

class ScreenRecorder:
    def __init__(self, interval=1, save_interval=30, output_dir="/Users/sethrose/Documents/Development/Repositories/time-capsule/recordings/screenshots"):
        self.output_dir = output_dir
        self.interval = interval
        self.save_interval = save_interval
        self.running = False
        self.thread = None
        self.process = None

    def start_recording(self):
        self.running = True
        self.thread = threading.Thread(target=self._record_screen)
        self.thread.start()
        print("Screen recording started.")

    def stop_recording(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()
        if self.process is not None:
            self.process.stdin.close()
            self.process.wait()
        print("Screen recording stopped.")

    def _record_screen(self):
        screen_size = pyautogui.size()
        video_size = (screen_size[0], screen_size[1])  # Set video size to match the screen size
        fps = 1  # Set the desired frame rate to 0.5 fps

        start_time = datetime.now()
        timestamp = start_time.strftime("%Y%m%d_%H%M%S")
        video_filename = f"screen_recording_{timestamp}.mp4"
        video_filepath = os.path.join(self.output_dir, video_filename)

        self.process = (
            ffmpeg
            .input('pipe:', format='rawvideo', pix_fmt='bgr24', s='{}x{}'.format(video_size[0], video_size[1]))
            .output(video_filepath, vcodec='libx264', pix_fmt='yuv420p', r=fps)
            .overwrite_output()
            .run_async(pipe_stdin=True)
        )

        while self.running:
            screenshot = self._capture_screenshot()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            frame = cv2.resize(frame, video_size)  # Resize the frame to match the video size
            self.process.stdin.write(frame.tobytes())

            current_time = datetime.now()
            elapsed_time = (current_time - start_time).total_seconds()

            if elapsed_time >= self.save_interval:
                self.process.stdin.close()
                self.process.wait()
                print(f"Screen recording saved: {video_filepath}")

                start_time = current_time
                timestamp = start_time.strftime("%Y%m%d_%H%M%S")
                video_filename = f"screen_recording_{timestamp}.mp4"
                video_filepath = os.path.join(self.output_dir, video_filename)

                self.process = (
                    ffmpeg
                    .input('pipe:', format='rawvideo', pix_fmt='bgr24', s='{}x{}'.format(video_size[0], video_size[1]))
                    .output(video_filepath, vcodec='libx264', pix_fmt='yuv420p', r=fps)
                    .overwrite_output()
                    .run_async(pipe_stdin=True)
                )

            self._delete_old_recordings()
            time.sleep(self.interval)

        self.process.stdin.close()
        self.process.wait()
        print(f"Screen recording saved: {video_filepath}")

    def _capture_screenshot(self):
        screenshot = pyautogui.screenshot()
        return screenshot

    def _delete_old_recordings(self):
        current_time = datetime.now()
        thirty_minutes_ago = current_time - timedelta(minutes=30)

        for filename in os.listdir(self.output_dir):
            if filename.startswith("screen_recording_"):
                file_path = os.path.join(self.output_dir, filename)
                creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                if creation_time < thirty_minutes_ago:
                    os.remove(file_path)
                    print(f"Deleted old screen recording: {file_path}")