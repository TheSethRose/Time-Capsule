# Time Capsule Project

## Project Setup

- [x] Create the project folder structure
- [x] Set up a virtual environment for the project
- [x] Install the required dependencies

## Screen Recording

- [x] Implement the `ScreenRecorder` class in `src/screen_recording/screen_recorder.py`
  - [x] Use PyAutoGUI to capture screenshots at a fixed interval of 2 seconds (0.5 FPS)
  - [x] Temporarily store screenshots as PNG files
  - [x] Implement a background process for continuous screenshot capture
  - [x] Provide configuration options for screenshot interval & output directory

- [ ] Implement platform-specific libraries to identify & filter out excluded apps & private browser windows
  - [ ] Research & select appropriate libraries for each supported platform (MacOS, Windows, Linux)
  - [ ] Integrate the selected libraries into the screen recording module
  - [ ] Test the exclusion functionality on each platform

- [x] Write tests for the `ScreenRecorder` class in `tests/test_screen_recording.py`

- [x] Optimize screen recording by encoding directly to H.264 video format using FFmpeg
  - [x] Compress screenshots directly to H.264 using FFmpeg's libx264 encoder
  - [ ] Investigate & implement hardware acceleration for video encoding on supported platforms
  - [x] Store encoded video files with timestamped filenames
  - [x] Implement a background process for periodic video encoding

- [ ] Implement automatic deletion of old recordings based on a configurable retention policy
  - [ ] Add a configuration option for specifying the retention period
  - [ ] Implement a background task to periodically check & delete old recordings

## Audio Recording

- [x] Implement the `AudioRecorder` class in `src/audio_recording/audio_recorder.py`
  - [x] Use sounddevice library to capture audio from the default microphone at 44.1 kHz
  - [x] Save audio recordings in WAV format at a configurable interval (default: 5 minutes)
  - [x] Implement a background process for continuous audio recording
  - [x] Provide configuration options for audio device selection & recording interval

- [x] Write tests for the `AudioRecorder` class in `tests/test_audio_recording.py`

- [ ] Integrate with OpenAI Whisper library for real-time speech-to-text conversion
  - [ ] Research & evaluate the integration process with OpenAI Whisper
  - [ ] Implement a background process for continuous audio transcription
  - [ ] Handle potential errors & edge cases during the transcription process
  - [ ] Save transcripts along with timestamps in JSON format
  - [ ] Provide configuration options for enabling/disabling transcription

## Optical Character Recognition (OCR)

- [ ] Implement the `OCRProcessor` class in `src/ocr/ocr_processor.py`
  - [ ] Use Tesseract OCR library to extract text from captured screenshots
  - [ ] Preprocess screenshots using OpenCV to enhance text visibility
    - [ ] Investigate & implement suitable image preprocessing techniques
    - [ ] Test & optimize the preprocessing pipeline for different types of screenshots
  - [ ] Perform text localization using Tesseract's page segmentation modes
    - [ ] Evaluate different page segmentation modes for optimal text localization
    - [ ] Implement logic to select the appropriate segmentation mode based on screenshot content
  - [ ] Apply OCR to identified regions & extract text content
  - [ ] Save extracted text with corresponding screenshot timestamps in JSON format
  - [ ] Implement a background process for periodic OCR processing

- [ ] Write tests for the `OCRProcessor` class in `tests/test_ocr.py`
  - [ ] Develop test cases for different scenarios (e.g., screenshots with varying text content & layouts)
  - [ ] Ensure adequate test coverage for the OCR functionality

- [ ] Optimize OCR performance by subsampling / deferring processing based on system load & power source
  - [ ] Implement logic to monitor system load & power source
  - [ ] Adjust OCR processing frequency / defer processing based on the monitored metrics
  - [ ] Test & fine-tune the optimization strategy for different system configurations

## Typed Text Capturing

- [x] Implement the `TextCapture` class in `src/text/text_capture.py`
  - [x] Use pynput library to monitor & capture typed text across applications
  - [x] Implement event listeners to capture key presses & store typed text in memory
    - [ ] Handle special keys & key combinations appropriately
    - [x] Implement logic to handle text editing & modifications
  - [x] Periodically save captured typed text to a JSON file with timestamps
  - [ ] Provide configuration options for enabling/disabling typed text capture & specifying storage interval

- [ ] Write tests for the `TextCapture` class in `tests/test_text.py`
  - [ ] Develop test cases for different typing scenarios & edge cases
  - [ ] Ensure adequate test coverage for the typed text capture functionality

## Data Storage & Indexing

- [ ] Set up SQLite as the lightweight database system for storing recorded data
  - [ ] Install & configure SQLite in the project environment
  - [ ] Create a database connection & initialization script

- [ ] Design a database schema with tables for screen recordings, audio transcripts, extracted text & typed text
  - [ ] Identify the required fields & relationships between tables
  - [ ] Create SQL scripts / ORM models to define the database schema

- [ ] Implement indexing on timestamp columns for fast searching & retrieval
  - [ ] Analyze query patterns & determine appropriate indexing strategies
  - [ ] Create necessary indexes on timestamp columns

- [ ] Provide an API / query interface for searching & retrieving data based on user-defined criteria
  - [ ] Design & implement an API layer for querying the recorded data
  - [ ] Support querying based on timestamps, keywords & other relevant criteria

- [ ] Optimize the database structure by partitioning data based on time ranges for improved performance & manageability
  - [ ] Evaluate different partitioning strategies (e.g., monthly, quarterly)
  - [ ] Implement scripts / tools to automate the partitioning process

## User Interface

- [ ] Design the user interface mockups & wireframes
  - [ ] Create sketches / wireframes for the main screens & components
  - [ ] Gather feedback & iterate on the design

- [ ] Develop a cross-platform user interface using PyQt
  - [ ] Familiarize with PyQt & its layout system
  - [ ] Implement the main windows & screens based on the design mockups
  - [ ] Ensure a consistent & intuitive user experience across platforms

- [ ] Implement search functionality for querying data based on keywords, timestamps, / other criteria
  - [ ] Integrate the search API / query interface with the user interface
  - [ ] Provide user-friendly options for specifying search criteria
  - [ ] Display search results in a clear & organized manner

- [ ] Provide playback options for screen recordings & audio transcripts with controls
  - [ ] Implement a media player component for video & audio playback
  - [ ] Include controls for play, pause, seek & speed adjustment
  - [ ] Synchronize the playback of screen recordings with audio transcripts

- [ ] Enable exporting of selected data points in CSV & PDF formats
  - [ ] Implement data export functionality for selected recordings / search results
  - [ ] Generate CSV & PDF files with appropriate formatting & structure

- [ ] Incorporate features for starring important moments, bulk deletion & privacy management
  - [ ] Add options to mark specific recordings / moments as starred / important
  - [ ] Implement bulk deletion functionality for selected recordings / time ranges
  - [ ] Provide privacy settings for controlling data retention & deletion

## Security & Privacy

- [ ] Implement AES encryption using PyCryptodome to secure stored data
  - [x] Research & understand the usage of PyCryptodome for AES encryption
  - [ ] Design & implement a secure encryption scheme for stored data
  - [ ] Ensure the encryption keys are securely generated & managed

- [ ] Encrypt video files, audio transcripts & text data on disk using user-provided passwords
  - [ ] Prompt users to set a strong password for data encryption
  - [ ] Integrate the user-provided password into the encryption process
  - [ ] Handle password changes & re-encryption of existing data

- [ ] Use secure key derivation functions for generating encryption keys from user passwords
  - [ ] Evaluate & select a suitable key derivation function (e.g., PBKDF2, Scrypt)
  - [ ] Implement the key derivation process using the chosen function

- [ ] Provide options for configurable data retention policies & secure data deletion
  - [ ] Allow users to specify data retention periods for different types of recorded data
  - [ ] Implement secure deletion methods to permanently remove expired / deleted data

- [ ] Allow exclusion of specific apps / windows from recording based on platform-specific mechanisms
  - [ ] Investigate platform-specific APIs / techniques for identifying & excluding apps / windows
  - [ ] Provide user-friendly options for configuring exclusion rules

- [ ] Implement features for bulk deletion of recordings by app, time range, / other criteria
  - [ ] Develop user interface components for selecting & deleting recordings in bulk
  - [ ] Optimize the deletion process to handle large volumes of data efficiently

## Performance Optimization

- [ ] Analyze the application's performance & identify bottlenecks
  - [ ] Use profiling tools to measure execution times & resource usage
  - [ ] Identify performance-critical sections of the codebase

- [ ] Optimize video encoding using hardware acceleration & appropriate encoding settings
  - [ ] Profile the video encoding process & identify opportunities for optimization
  - [ ] Fine-tune encoding settings based on the target platform & hardware capabilities

- [ ] Explore options to subsample / defer OCR & speech-to-text processing based on system load & power source
  - [ ] Monitor system load & power source (battery vs. AC power) in real-time
  - [ ] Adjust the frequency / priority of OCR & speech-to-text processing accordingly
  - [ ] Test & validate the impact of subsampling / deferral on performance & accuracy

- [ ] Utilize caching mechanisms to store frequently accessed data in memory for faster retrieval
  - [ ] Identify frequently accessed data points / query results
  - [ ] Implement caching layers to store & retrieve data from memory
  - [ ] Develop cache invalidation strategies to ensure data consistency

- [ ] Continuously monitor & profile the application to identify & address performance bottlenecks
  - [ ] Integrate performance monitoring & logging into the application
  - [ ] Regularly analyze performance metrics & logs to identify areas for improvement
  - [ ] Optimize critical code paths & algorithms based on the collected insights

## Cross-Platform Compatibility

- [ ] Identify & evaluate cross-platform libraries & frameworks for each major component
  - [ ] Research & compare libraries for screen recording, audio recording, OCR, etc.
  - [ ] Consider factors such as platform support, performance & maintenance

- [ ] Develop & test the application on each supported platform (MacOS, Windows, Linux)
  - [ ] Set up development & testing environments for each platform
  - [ ] Ensure the application builds & runs successfully on each platform
  - [ ] Perform thorough testing to identify & fix platform-specific issues

- [ ] Provide platform-specific installation & configuration guides
  - [ ] Document the installation process & dependencies for each platform
  - [ ] Include step-by-step instructions for configuring the application on each platform

- [ ] Address platform-specific challenges / limitations that arise during development
  - [ ] Investigate & find workarounds for any platform-specific constraints
  - [ ] Modify the codebase / architecture to accommodate platform differences
  - [ ] Continuously test & validate the application's behavior on each platform

## Documentation & Community Support

- [ ] Write comprehensive documentation for users & developers
  - [ ] Create user guides & tutorials for installing, configuring & using the application
  - [ ] Develop API documentation & code examples for developers
  - [ ] Include troubleshooting guides & FAQs to address common issues

- [ ] Set up a project website / wiki to host the documentation
  - [ ] Choose a suitable platform for hosting the documentation (e.g., GitHub Pages, ReadTheDocs)
  - [ ] Organize & structure the documentation for easy navigation & accessibility

- [ ] Establish a community forum / discussion platform for users & contributors
  - [ ] Select a platform for hosting the community forum (e.g., Discourse, GitHub Discussions)
  - [ ] Set up categories & guidelines for discussions & support
  - [ ] Actively participate in the community & provide timely responses to questions & feedback

- [ ] Develop contribution guidelines & a code of conduct for the project
  - [ ] Define the process for submitting bug reports, feature requests & pull requests
  - [ ] Establish coding standards, style guides & review processes for contributions
  - [ ] Foster an inclusive & welcoming environment for contributors

## Deployment & Distribution

- [ ] Determine the target platforms & distribution channels for the application
  - [ ] Identify the primary platforms (e.g., MacOS, Windows, Linux) for distribution
  - [ ] Evaluate potential distribution channels (e.g., GitHub Releases, platform-specific package managers)

- [ ] Prepare detailed installation instructions & dependencies for each platform
  - [ ] Document the system requirements & prerequisites for each platform
  - [ ] Provide step-by-step installation guides, including any necessary dependencies

- [ ] Create distribution packages using tools like PyInstaller / py2app
  - [ ] Research & select the appropriate packaging tools for each platform
  - [ ] Configure & build distribution packages for easy installation
  - [ ] Test the installation process & ensure the packages work as expected

- [ ] Set up automated build & release processes using CI/CD pipelines
  - [ ] Choose a suitable CI/CD platform (e.g., GitHub Actions, Travis CI)
  - [ ] Define the build & release workflows for each platform
  - [ ] Automate the creation & publishing of distribution packages

- [ ] Establish a mechanism for delivering updates & bug fixes
  - [ ] Determine the update strategy (e.g., manual updates, automatic updates)
  - [ ] Implement an update system using mechanisms like GitHub Releases / a custom update server
  - [ ] Provide clear instructions for users to update the application when new versions are available

- [ ] Explore publishing the application on platform-specific package managers
  - [ ] Research the requirements & guidelines for publishing on each package manager
  - [ ] Prepare the necessary metadata, documentation & package files
  - [ ] Submit the application for review & inclusion in the package repositories

- [ ] Monitor user feedback & issues reported through various channels
  - [ ] Set up a system for tracking & prioritizing user-reported issues & feature requests
  - [ ] Provide timely responses & updates to users regarding the resolution of their concerns
  - [ ] Continuously improve the application based on user feedback & real-world usage patterns
