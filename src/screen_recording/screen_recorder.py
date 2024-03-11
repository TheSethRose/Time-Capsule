import mss
import mss.tools
import time
from PIL import Image
from datetime import datetime
from math import ceil, floor, sqrt
import os
import subprocess
import threading

class ScreenRecorder:
    system_info = None
    
    def __init__(self, system_info, fps=0.5, video_duration=30):
        if ScreenRecorder.system_info is None and system_info is not None:
            ScreenRecorder.system_info = system_info

        self.fps = fps
        self.video_duration = video_duration
        self.running = False

        # self.video_dir = os.path.join(os.getcwd(), "recordings", "videos")
        # self.save_dir = os.path.join(self.video_dir, "temp")
        self.save_dir = "/Users/sethrose/Documents/Development/Repositories/time-capsule/recordings/videos/temp/"
        self.video_dir = "/Users/sethrose/Documents/Development/Repositories/time-capsule/recordings/videos/"

        
    def start_recording(self):
        if not self.running:
            self.running = True
            self.recorder_thread = threading.Thread(target=self._record)
            self.recorder_thread.start()
            print("Screen Recording Service: Started")


    def _record(self):
        with mss.mss() as sct:
            monitors = sct.monitors[1:]
            screenshot_count = 0
            start_time = time.time()
            screenshots = []

            while self.running:
                screenshot = self.capture_screenshot(monitors)
                screenshots.append(screenshot)
                screenshot_count += 1

                if screenshot_count % 15 == 0:
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= self.video_duration:
                        video_thread = threading.Thread(target=self.create_video_from_screenshots, args=(screenshots,))
                        video_thread.start()
                        screenshots = []
                        start_time = time.time()
                        screenshot_count = 0

                time.sleep(2)

    def stop_recording(self):
        self.running = False
        self.recorder_thread.join()
        print("Screen Recording Service: Stopped")

    def capture_screenshot(self, monitors):
        with mss.mss() as sct:
            screenshots = [sct.grab(monitor) for monitor in monitors]
            num_monitors = len(screenshots)

            rows, cols = self.optimal_grid(num_monitors)

            images = [Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX") for img in screenshots]

            max_width = max(monitor['width'] for monitor in monitors)
            max_height = max(monitor['height'] for monitor in monitors)

            resized_images = self.resize_images(images, max_width, max_height)

            grid_width = max(img.width for img in resized_images) * cols
            grid_height = sum(max(img.height for img in resized_images[i:i+cols]) for i in range(0, num_monitors, cols))
            grid = Image.new('RGB', (grid_width, grid_height))

            y_offset = 0
            for i in range(0, num_monitors, cols):
                row_images = resized_images[i:i+cols]
                x_offset = self.center_images(row_images, grid_width)
                for img in row_images:
                    grid.paste(img, (x_offset, y_offset))
                    x_offset += img.width
                y_offset += max(img.height for img in row_images)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            filepath = os.path.join(self.save_dir, filename)
            grid.save(filepath)

            return filepath

    def create_video_from_screenshots(self, screenshots):
        video_timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        video_filename = f"recording_{video_timestamp}.mp4"
        video_filepath = os.path.join(self.video_dir, video_filename)

        subprocess.call(['ffmpeg', '-framerate', str(self.fps), '-pattern_type', 'glob',
                         '-i', self.save_dir + '*.png', '-c:v', 'libx264', '-r', '30',
                         '-pix_fmt', 'yuv420p', video_filepath])
        
        print(f"Video saved: {video_filename}")
        self.clear_screenshots(screenshots)

    def clear_screenshots(self, screenshots):
        for screenshot in screenshots:
            os.remove(screenshot)

    @staticmethod
    def optimal_grid(num_monitors):
        cols = round(sqrt(num_monitors))
        rows = ceil(num_monitors / cols)
        return rows, cols

    @staticmethod
    def resize_images(images, max_width, max_height):
        resized_images = []
        for img in images:
            img = img.resize((max_width, max_height), Image.ANTIALIAS)
            resized_images.append(img)
        return resized_images

    @staticmethod
    def center_images(images, total_width):
        combined_width = sum(img.width for img in images)
        offset = (total_width - combined_width) // 2
        return offset
