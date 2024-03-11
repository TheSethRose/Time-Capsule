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

# 🚧 Work in Progress 🚧

Time Capsule is currently under active development, with several exciting features in the pipeline.

## 🚀 Current Functionality

- **Screen recording**

  - Captures screenshots at a fixed interval of 2 seconds (0.5 FPS)
  - Encodes screenshots directly into H.264 video using FFmpeg
  - Saves screen recordings in MP4 format at a configurable interval (default: 5 minutes)
  - Automatically deletes old recordings based on a configurable retention policy

- **Audio recording**

  - Records audio continuously using the system's default audio input device
  - Saves audio recordings in WAV format at a configurable interval (default: 5 minutes)

- **Typed text capture:**
  - Captures typed text across applications using the pynput library
  - Detects context switches based on mouse clicks, window focus changes, key presses, long pauses, and token limit reached
  - Saves captured text periodically to JSON files with timestamps and metadata
  - Provides configuration options for enabling/disabling text capture and specifying storage interval

## 📝 Features Awaiting Implementation

- 📝 Optical character recognition (OCR) to extract text from screen recordings
- 🗣️ Speech-to-text functionality to transcribe audio recordings
- 🔍 Search functionality to quickly find specific information based on keywords or timestamps
- 🔐 Data encryption to ensure the security of recorded data
- 🎨 Intuitive user interface for easy navigation and playback of recordings

## 💻 Installation Instructions

Follow these detailed steps to get the project running on your local machine, irrespective of your operating system.

### 1. Clone the Repository

First, clone the project to your local machine. Open a terminal (or Command Prompt on Windows) and execute:

```bash
git clone https://github.com/TheSethRose/time-capsule.git
```

Navigate into the cloned directory:

```bash
cd time-capsule
```

### 2. Create and Activate a Virtual Environment

Creating a virtual environment is crucial for managing project-specific dependencies.

- **For MacOS/Linux/Raspberry Pi:**

  Create the virtual environment:

  ```bash
  python3 -m venv time-capsule-env
  ```

  Activate it:

  ```bash
  source time-capsule-env/bin/activate
  ```

- **For Windows:**

  Create the virtual environment:

  ```bash
  python -m venv time-capsule-env
  ```

  Activate it:

  ```bash
  .\time-capsule-env\Scripts\activate
  ```

### 3. Install Dependencies

With your environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Configuration is handled through environment variables. Start by copying the example configuration file:

```bash
cp .env.example .env
```

Open `.env` in a text editor and adjust the settings to match your development setup.

### 5. Adjust Configuration Settings

Ensure you review the `.env` file thoroughly to tailor the application settings to your preferences and requirements.

### 6. Run the Application

With everything set up, start the application with:

```bash
python main.py
```

This will initialize the application based on your `.env` configurations.

### 7. After Installation

After installation, you can now start using the Time Capsule application. The application will automatically start recording and storing data in the specified directories.
To customize the application further, you can modify the code and configuration files as needed.

## 📂 Project Structure

The Time Capsule project follows a modular and organized structure:

- `src/`: Contains the main source code files
  - `screen_recording/`: Module for screen recording functionality
  - `audio_recording/`: Module for audio recording functionality
  - `ocr/`: Module for optical character recognition (OCR)
  - `text/`: Module for capturing typed text
  - `main.py`: Main entry point of the application
- `recordings/`: Directory for storing recorded data
  - `screenshots/`: Subdirectory for screen recordings
  - `audio/`: Subdirectory for audio recordings
  - `text/`: Subdirectory for captured text data
- `tests/`: Contains unit tests for various modules
- `utils/`: Contains utility modules
  - `system_info.py`: Module for retrieving system information
  - `tokenization_utils.py`: Module for tokenizing and storing text data
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
