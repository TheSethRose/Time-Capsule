import time
from pynput import keyboard, mouse
from datetime import datetime
from utils.tokenization_utils import TokenizationUtils


class TextCapture:
    system_info = None

    def __init__(self, system_info, output_dir="/Users/sethrose/Documents/Development/Repositories/time-capsule/recordings/text"):
        if TextCapture.system_info is None and system_info is not None:
            TextCapture.system_info = system_info
        self.output_dir = output_dir
        self.current_minute = None
        self.key_listener = None
        self.mouse_listener = None
        self.current_phrase = ""
        self.tokenization_utils = TokenizationUtils(output_dir)  # Create an instance of TokenizationUtils
        self.last_activity_time = time.time()
        self.inactivity_threshold = 5  # Inactivity threshold in seconds
        self.current_window = None
        self.last_click_time = 0
        self.click_threshold = 1  # Click threshold in seconds

    def start_capture(self):
        self.key_listener = keyboard.Listener(on_press=self.on_key_press)
        self.mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
        self.key_listener.start()
        self.mouse_listener.start()
        print("Text Capture: Started")

    def stop_capture(self):
        self.key_listener.stop()
        self.mouse_listener.stop()
        self.save_current_phrase()  # Save any remaining phrase before stopping
        print("Text Capture: Stopped")

    def on_key_press(self, key):
        current_minute = datetime.now().strftime("%Y-%m-%d_%H%M")

        if self.current_minute is None:
            self.current_minute = current_minute
        elif self.current_minute != current_minute:
            self.save_current_phrase()
            self.current_minute = current_minute

        try:
            char = key.char
            self.current_phrase += char
            self.last_activity_time = time.time()

            # Check for specific key combinations associated with context switching
            if key == keyboard.Key.alt_l or key == keyboard.Key.cmd:
                self.save_current_phrase(context_switch=True)
            elif key == keyboard.Key.enter:
                self.save_current_phrase(context_switch=True)

        except AttributeError:
            if key == keyboard.Key.space:
                self.current_phrase += " "
            elif key == keyboard.Key.backspace:
                self.current_phrase = self.current_phrase[:-1]
            # Add more special key handling as needed

        # Check for long pauses
        if time.time() - self.last_activity_time >= self.inactivity_threshold:
            self.save_current_phrase(context_switch=True)
            self.last_activity_time = time.time()

    def on_mouse_click(self, x, y, button, pressed):
        if pressed:
            current_time = time.time()
            if current_time - self.last_click_time <= self.click_threshold:
                self.save_current_phrase(context_switch=True)
            self.last_click_time = current_time

    def save_current_phrase(self, context_switch=False):
        if self.current_phrase.strip():
            timestamp = datetime.now().isoformat()

            # Error handling for system_info being None
            if TextCapture.system_info is None:
                raise ValueError("System information is not available. `system_info` has not been initialized.")

            os_info = TextCapture.system_info.get_info("os")
            machine_info = TextCapture.system_info.get_info("machine")
            architecture_info = TextCapture.system_info.get_info("architecture")
            cpu_info = TextCapture.system_info.get_info("cpu")
            memory_info = TextCapture.system_info.get_info("memory")
            active_window = TextCapture.system_info.get_active_window()

            metadata = {
                "os": os_info,
                "machine": machine_info,
                "architecture": architecture_info,
                "cpu": cpu_info,
                "memory": memory_info,
                "window": active_window
            }

            self.tokenization_utils.process_text_capture(self.current_phrase, timestamp, metadata, context_switch)
            self.current_phrase = ""  # Reset the current phrase after saving


    def get_active_window(self):
        # Implement the logic to get the active window or application
        # You can use platform-specific libraries or modules for this purpose
        # Return a string representing the active window or application
        return "Active Window"