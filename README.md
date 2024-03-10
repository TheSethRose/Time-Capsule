# Time Capsule

Introducing Time Capsule
The open-source, self-hosted AI assistant that empowers you with perfect memory! 🧠💡

Time Capsule is a powerful tool that continuously captures and stores your digital activities, including screen recordings, audio recordings, and typed text. It enables you to search and retrieve any information you've seen, said, or heard on your device, providing you with a comprehensive digital memory.

## ✨ Key Features

- 🔒 Own your data with secure local storage
- 🖥️ Continuous capture of screen, audio & text
- 🔍 Search & find anything instantly
- 💻 Customize & extend with open source code

## 🚧 Work in Progress

Time Capsule is currently under active development, with several exciting features in the pipeline:

- 🗣️ Auto-record & transcribe meetings
- 🧠 Get AI-generated summaries & insights
- 🌐 Cross-platform support for Windows, Linux, and macOS
- 🔐 Data encryption and privacy controls
- 🎨 Intuitive user interface for easy navigation and playback
- 📊 Data visualization and analytics

## 📂 Project Structure

The Time Capsule project follows a modular and organized structure:

- `src/`: Contains the main source code files
  - `screen_recording/`: Module for screen recording functionality
  - `audio_recording/`: Module for audio recording functionality
  - `ocr/`: Module for optical character recognition (OCR)
  - `typed_text/`: Module for capturing typed text
  - `main.py`: Main entry point of the application
- `recordings/`: Directory for storing recorded data
  - `screenshots/`: Subdirectory for screen recordings
  - `audio/`: Subdirectory for audio recordings
- `tests/`: Contains unit tests for various modules
- `docs/`: Documentation files
- `requirements.txt`: Lists the required Python dependencies
- `setup.py`: Setup script for the project

## 🛠️ Current Functionality

- Screen recording:
  - Captures screenshots at a configurable interval (default: 1 second)
  - Encodes screenshots directly into H.264 video using FFmpeg
  - Saves screen recordings in MP4 format at a specified interval (default: 30 seconds)
  - Automatically deletes old recordings older than 30 minutes
- Audio recording:
  - Records audio continuously using the system's default audio input device
  - Saves audio recordings in WAV format at a specified interval (default: 5 minutes)
- Deletion of old recordings:
  - Automatically deletes screen recordings and audio recordings older than 30 minutes to manage storage space

## 📋 TODO

- Implement optical character recognition (OCR) to extract text from screen recordings
- Implement capturing of typed text and saving it with timestamps
- Integrate speech-to-text functionality to transcribe audio recordings
- Develop a search functionality to quickly find specific information based on keywords or timestamps
- Implement data encryption to ensure the security of recorded data
- Design and implement an intuitive user interface for easy navigation and playback of recordings
- Add support for cross-platform deployment on Windows, Linux, and macOS
- Integrate AI-powered features for generating summaries and insights from recorded data
- Implement data visualization and analytics to provide meaningful insights into user activity
- Optimize performance and resource usage for efficient continuous recording
- Enhance privacy controls and implement secure data deletion mechanisms
- Write comprehensive documentation and guides for installation, configuration, and usage
- Set up a project website and community forum for user support and engagement

## 🤝 Contributing

We welcome contributions from the open-source community to help improve and expand the capabilities of Time Capsule. If you'd like to contribute, please refer to our [contribution guidelines](CONTRIBUTING.md) for more information.

## 📄 License

Time Capsule is released under the [MIT License](LICENSE).

## 📧 Contact

For any questions, suggestions, or feedback, please feel free to reach out to me on X at [@TheSethRose](https://www.x.com/TheSethRose)

## ❤️ Support

<a href="https://www.buymeacoffee.com/TheSethRose" target="_blank"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee!&emoji=&slug=TheSethRose&button_colour=000000&font_colour=ffffff&font_family=Cookie&outline_colour=ffffff&coffee_colour=FFDD00" alt="Buy Me A Coffee!"></a>


