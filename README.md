# Time Capsule

Introducing Time Capsule
The open-source, self-hosted AI assistant that empowers you with perfect memory! 🧠💡

Time Capsule is a powerful tool that continuously captures and stores your digital activities, including screen recordings, audio recordings, and typed text. It enables you to search and retrieve any information you've seen, said, or heard on your device, providing you with a comprehensive digital memory.

## ✨ Key Features

- 🔒 Own your data with secure local storage
- 🖥️ Continuous capture of screen at 0.5 FPS, audio & text
- 🔍 Search & find anything instantly
- 💻 Customize & extend with open source code
- 🔐 Encrypted storage for enhanced security
- ⚡ Optimized performance using FFmpeg & hardware acceleration
- 🐧🪟🍎 Cross-platform support for Windows, Linux, and macOS

## 🚀 Current Functionality

- Screen recording:
  - Captures screenshots at a fixed interval of 2 seconds (0.5 FPS)
  - Encodes screenshots directly into H.264 video using FFmpeg
  - Saves screen recordings in MP4 format at a configurable interval (default: 5 minutes)
  - Automatically deletes old recordings based on a configurable retention policy
- Audio recording:
  - Records audio continuously using the system's default audio input device
  - Saves audio recordings in WAV format at a configurable interval (default: 5 minutes)

## 🚧 Work in Progress

Time Capsule is currently under active development, with several exciting features in the pipeline:

- 📝 Optical character recognition (OCR) to extract text from screen recordings
- ⌨️ Capturing of typed text and saving it with timestamps
- 🗣️ Speech-to-text functionality to transcribe audio recordings
- 🔍 Search functionality to quickly find specific information based on keywords or timestamps
- 🔐 Data encryption to ensure the security of recorded data
- 🎨 Intuitive user interface for easy navigation and playback of recordings
- 📊 Data visualization and analytics
- ⚙️ Performance optimizations and resource usage improvements
- 🚀 Automated deployment and distribution for easy installation on various platforms

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

## 🤝 Contributing

We welcome contributions from the open-source community to help improve and expand the capabilities of Time Capsule. If you'd like to contribute, please refer to our [contribution guidelines](CONTRIBUTING.md) for more information.

## 📄 License

Time Capsule is released under the [MIT License](LICENSE).

## 📧 Contact

For any questions, suggestions, or feedback, please feel free to reach out to me on X at [@TheSethRose](https://www.x.com/TheSethRose)

## ❤️ Support

<a href="https://www.buymeacoffee.com/TheSethRose" target="_blank"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee!&emoji=&slug=TheSethRose&button_colour=000000&font_colour=ffffff&font_family=Cookie&outline_colour=ffffff&coffee_colour=FFDD00" alt="Buy Me A Coffee!"></a>
