import platform
import psutil
import subprocess

class SystemInfo:
    def __init__(self):
        self.os_name = platform.system()
        self.os_release = platform.release()
        self.os_version = platform.version()
        self.machine = platform.machine()
        self.processor = platform.processor()
        self.architecture = platform.architecture()[0]
        self.cpu_count = psutil.cpu_count(logical=True)
        self.memory = psutil.virtual_memory().total  # In bytes

    def get_info(self, info_type):
        if info_type == "os":
            return f"{self.os_name} {self.os_release} ({self.os_version})"
        elif info_type == "machine":
            return f"{self.machine} - {self.processor}"
        elif info_type == "architecture":
            return f"Architecture: {self.architecture}"
        elif info_type == "cpu":
            return f"CPU Cores: {self.cpu_count}"
        elif info_type == "memory":
            # Convert bytes to GB for readability
            memory_gb = round(self.memory / (1024**3), 2)
            return f"Total System Memory: {memory_gb} GB"
        else:
            return "Invalid info type specified."

    def get_active_window(self):
        if self.os_name == "Windows":
            import win32gui
            window = win32gui.GetForegroundWindow()
            title = win32gui.GetWindowText(window)
            return title
        elif self.os_name == "Darwin":  # macOS
            script = 'tell application "System Events" to get the name of the first process whose frontmost is true'
            output = subprocess.check_output(["osascript", "-e", script]).decode("utf-8").strip()
            return output
        else:  # Assume Unix-like systems (Linux, BSD, etc.)
            try:
                output = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"]).decode("utf-8").strip()
                return output
            except FileNotFoundError:
                return "Unknown"