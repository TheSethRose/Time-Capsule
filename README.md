# Time Capsule

Time Capsule is a powerful tool designed to continuously capture and store your digital activities, creating a comprehensive digital memory. Currently, it focuses on audio capture and transcription, with plans to expand to other forms of digital activity logging and advanced memory recall features.

## ✨ Current Features

- 🎙️ Real-time microphone recording
- 🗣️ Speech-to-text transcription using Fast-Whisper library
- ⚙️ Configurable language and confidence settings (`config/config.py`)
- 💾 Database storage of transcribed text (SQLite, to be replaced with Vector Database)

## 🚀 Future Features

- 🔗 Integration with a vector database for efficient storage and retrieval of information
- 🤖 LLM integration for natural language interaction with your digital memory
- 🧠 Advanced memory recall capabilities, allowing users to query their digital history
- 📊 Expanded data capture (screen recordings, typed text, etc.)

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TheSethRose/Time-Capsule.git
   cd Time-Capsule
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure settings in `config/config.py` according to your preferences.

## 🖥️ Usage

Start capturing audio:

```bash
python main.py
```

Press `Ctrl+C` to stop the application.

## 📝 Planned Functionality

Future versions of Time Capsule aim to provide a seamless interface for interacting with your digital memory. Example queries:

- "What did we agree upon in that meeting last Thursday?"
- "When is my doctor's appointment?"
- "How much was my electricity bill?"
- "What was the last message I sent to my partner?"

These features will leverage vector databases and large language models to provide accurate, context-aware responses based on your captured digital activities.

## 📋 TODO List

- [x] Add microphone recording functionality
- [x] Implement Fast-Whisper model for audio transcription
- [ ] Implement screen recording functionality
- [ ] Add transcription service for screen recording
- [ ] Add typed text capture
- [ ] Develop user interface for interaction and search
- [ ] Implement data encryption for privacy
- [ ] Add support for multiple audio input sources
- [ ] Create plugin system for extensibility
- [ ] Implement sophisticated search functionality
- [ ] Add data visualization features
- [ ] Develop mobile app version
- [ ] Implement cloud sync capabilities
- [ ] Add support for video capture and transcription
- [ ] Implement activity categorization and tagging
- [ ] Add export functionality for captured data
- [ ] Implement timeline view of captured activities
- [ ] Add voice command support for application control
- [ ] Integrate vector database for efficient information storage/retrieval
- [ ] Implement LLM for natural language interaction with digital memory
- [ ] Develop advanced memory recall capabilities

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For any questions, suggestions, or feedback, please feel free to reach out to me on X at [@TheSethRose](https://www.x.com/TheSethRose)

## ❤️ Support

<a href="https://www.buymeacoffee.com/TheSethRose" target="_blank"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee!&emoji=&slug=TheSethRose&button_colour=000000&font_colour=ffffff&font_family=Cookie&outline_colour=ffffff&coffee_colour=FFDD00" alt="Buy Me A Coffee!"></a>

## ⚠️ Disclaimer

Ensure compliance with all applicable laws and regulations when using this software, particularly regarding privacy and data protection.
