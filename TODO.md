# Time Capsule Project TODO

## Project Setup
- [X] Create the project folder structure
- [X] Set up a virtual environment for the project
- [X] Install the required dependencies

## Screen Recording
- [X] Implement the `ScreenRecorder` class in `src/screen_recording/screen_recorder.py`
  - [X] Implement the `start_recording()` method to capture screenshots at regular intervals
  - [X] Implement the `stop_recording()` method to stop the screen recording
  - [X] Implement the `save_screenshot()` method to save the captured screenshots
- [X] Write tests for the `ScreenRecorder` class in `tests/test_screen_recording.py`
- [ ] Investigate cross-platform screen recording libraries (e.g., PyAutoGUI, MSS) for compatibility with Windows, Linux, and macOS
- [ ] Optimize screen recording by encoding directly to a video format (e.g., H.264) instead of saving as individual image files
- [ ] Consider increasing the screenshot capture frequency for more granular search results and smoother playback

## Audio Recording
- [X] Implement the `AudioRecorder` class in `src/audio_recording/audio_recorder.py`
  - [X] Implement the `start_recording()` method to start audio recording
  - [X] Implement the `stop_recording()` method to stop audio recording
  - [X] Implement the `save_audio()` method to save the recorded audio
- [X] Write tests for the `AudioRecorder` class in `tests/test_audio_recording.py`
- [ ] Investigate cross-platform audio recording libraries (e.g., PyAudio, sounddevice) for compatibility with Windows, Linux, and macOS
- [ ] Ensure audio recording works with any audio source, not just specific applications like Zoom

## Speech-to-Text Transcription
- [ ] Integrate a cross-platform speech-to-text library (e.g., Vosk, DeepSpeech) for offline transcription
- [ ] Implement the `transcribe_audio()` method to perform transcription on saved audio files
- [ ] Store transcripts, timestamps, and speaker metadata in the SQLite database
- [ ] Optimize transcription by subsampling or deferring processing when running on battery

## Optical Character Recognition (OCR)
- [ ] Investigate cross-platform OCR libraries (e.g., Tesseract, EasyOCR) for compatibility with Windows, Linux, and macOS
- [ ] Implement the `OCRProcessor` class in `src/ocr/ocr_processor.py`
  - [ ] Implement the `process_image()` method to perform OCR on a given screenshot
  - [ ] Implement the `save_extracted_text()` method to save the extracted text with timestamps
- [ ] Write tests for the `OCRProcessor` class in `tests/test_ocr.py`
- [ ] Optimize OCR by subsampling or deferring processing when running on battery

## Typed Text Capturing
- [ ] Implement the `TypedTextCapture` class in `src/typed_text/typed_text_capture.py`
  - [ ] Investigate cross-platform keyboard monitoring libraries (e.g., pynput, keyboard) for compatibility with Windows, Linux, and macOS
  - [ ] Implement the `start_capture()` method to start capturing typed text
  - [ ] Implement the `stop_capture()` method to stop capturing typed text
  - [ ] Implement the `save_typed_text()` method to save the captured typed text with timestamps
- [ ] Write tests for the `TypedTextCapture` class in `tests/test_typed_text.py`

## Data Storage
- [ ] Set up a SQLite database for storing recorded data
- [ ] Design the database schema for screen recordings, audio transcripts, extracted text, and typed text
- [ ] Implement database operations for saving and retrieving data from the timeline
- [ ] Adopt a storage structure similar to Rewind, with video files in chunks and metadata in SQLite
- [ ] Optimize storage format for long-term archival, considering directory structure and database performance

## Search and Indexing
- [ ] Implement SQLite FTS (full-text search) for efficient searching of transcripts, OCR results, and typed text
- [ ] Capture and index metadata like focused app, window title, and browser URL for contextual search

## Integration and Main Application
- [ ] Integrate the `ScreenRecorder`, `AudioRecorder`, `OCRProcessor`, and `TypedTextCapture` classes in `src/main.py`
- [ ] Implement the main application flow, including starting and stopping recordings, processing data, and storing it in the database
- [ ] Implement command-line interface or configuration options for controlling the application

## User Interface
- [ ] Design and implement a cross-platform user interface using a Python GUI framework (e.g., PyQt, wxPython, Kivy)
- [ ] Develop an intuitive timeline view for browsing and searching captured data
- [ ] Create views for searching, browsing, and viewing recorded data
- [ ] Implement search functionality to query data based on keywords, timestamps, or other criteria
- [ ] Implement playback options for screen recordings and audio transcripts
- [ ] Incorporate features like starring important moments and displaying favicons for web pages

## Data Export and Sharing
- [ ] Implement data export functionality to allow users to export their recorded data in a portable format (e.g., JSON, CSV)
- [ ] Explore options for securely sharing recorded data with other users or integrating with cloud storage services

## Privacy and Security
- [ ] Implement app exclusion and selective deletion features for user privacy
- [ ] Incorporate data encryption at rest, using techniques like AES encryption with user-provided passwords
- [ ] Ensure that all data is stored locally on the user's device and not transmitted to any external servers

## Performance Optimization
- [ ] Profile the application to identify performance bottlenecks
- [ ] Optimize database queries and indexing strategies
- [ ] Implement caching mechanisms for frequently accessed data
- [ ] Explore options for parallel processing and asynchronous operations to improve performance

## Testing and Quality Assurance
- [ ] Write unit tests for all major components and classes
- [ ] Write integration tests to ensure proper functionality and data flow
- [ ] Perform thorough manual testing of the application on Windows, Linux, and macOS
- [ ] Set up continuous integration and continuous deployment (CI/CD) pipelines for automated testing and releases

## Documentation and Community Support
- [ ] Write a comprehensive README.md file with project overview, installation instructions, and usage guidelines
- [ ] Create detailed documentation for developers, including API references and contribution guidelines
- [ ] Set up a project website or landing page to showcase the features and benefits of Time Capsule
- [ ] Establish a community forum or discussion platform for user support and feedback
- [ ] Encourage contributions from the open-source community to enhance and extend the project

## Deployment and Distribution
- [ ] Provide detailed installation instructions for Windows, Linux, and macOS
- [ ] Create distribution packages (e.g., executables, installers) for easy installation on different platforms
- [ ] Explore options for automated updates and bug fixes
- [ ] Consider publishing Time Capsule on package managers (e.g., pip, Homebrew) for easy installation and updates