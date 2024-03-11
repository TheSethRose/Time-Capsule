# Load standard modules
import time

# Load custom modules
from utils.system_info import SystemInfo
from src.screen_recording.screen_recorder import ScreenRecorder
from src.audio_recording.audio_recorder import AudioRecorder
from src.text.text_capture import TextCapture

# Get system information
system_info = SystemInfo()

print("Recording Process: Initializing Services...")

# Initialize recording services and pass system information
screen_recorder = ScreenRecorder(system_info=system_info)
#audio_recorder = AudioRecorder(system_info=system_info)
text_capture = TextCapture(system_info=system_info)

print("Recording Process: Starting Individual Services...")

# Start recording services
screen_recorder.start_recording()
#audio_recorder.start_recording()
text_capture.start_capture()

try:
    while True:
        # Keep the program running until interrupted
        time.sleep(0.5)
except KeyboardInterrupt:
    screen_recorder.stop_recording()
    #audio_recorder.stop_recording()
    text_capture.stop_capture()

    print("Recording Process: Interrupted by User")

