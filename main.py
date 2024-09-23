# main.py

import time
import queue
import logging
from modules.audio_recorder import AudioRecorder
from modules.transcription_service import TranscriptionService
from modules.database_manager import DatabaseManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Initialize the database manager
        db_manager = DatabaseManager()

        # Initialize the audio queue
        audio_q = queue.Queue()

        # Initialize and start the audio recorder
        recorder = AudioRecorder(audio_queue=audio_q)
        recorder.start_recording()

        # Initialize and start the transcription service
        transcription_service = TranscriptionService(audio_queue=audio_q, db_manager=db_manager)
        transcription_service.start_transcription()

        logging.info("Audio recording & Transcription services started. Recording started. Press Ctrl+C to stop.")

        while True:
            time.sleep(1)
            if not recorder.running or not transcription_service.thread.is_alive():
                raise Exception("Recording or transcription service stopped unexpectedly.")

    except KeyboardInterrupt:
        logging.info("Stopping the application...")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
    finally:
        if 'recorder' in locals():
            recorder.stop_recording()
        if 'transcription_service' in locals():
            transcription_service.stop_transcription()

if __name__ == "__main__":
    main()
