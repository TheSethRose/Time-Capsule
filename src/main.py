import time
from screen_recording.screen_recorder import ScreenRecorder
from audio_recording.audio_recorder import AudioRecorder

screen_recorder = ScreenRecorder()
#audio_recorder = AudioRecorder()

screen_recorder.start_recording()
#audio_recorder.start_recording()

try:
    while True:
        # Keep the program running until interrupted
        time.sleep(0.5)
except KeyboardInterrupt:
    screen_recorder.stop_recording()
    #audio_recorder.stop_recording()
    print("Recording stopped by the user.")