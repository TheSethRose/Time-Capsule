# Time Capsule

Time Capsule is a powerful tool designed to continuously capture and store your digital activities, creating a comprehensive digital memory. Currently, it focuses on audio capture and transcription, with plans to expand to other forms of digital activity logging and advanced memory recall features.

## 🚧 Work in Progress 🚧

**DISCLAIMER: Time Capsule is currently under heavy construction. Many features mentioned in this README are planned but not yet implemented. The current version focuses primarily on audio capture and transcription.**

## ✨ Current Features

- 🎙️ Real-time microphone recording
- 🗣️ Speech-to-text transcription using Fast-Whisper library
- ⚙️ Configurable language and confidence settings (`config/config.py`)
- 💾 Database storage of transcribed text using Chroma vector database

## 🚀 Future Features

- 🖥️ Screen recording and transcription
- 📁 Folder monitoring for important documents
- 🌐 Web interface for database management
- 🤖 LLM integration for natural language interaction with your digital memory
- 🧠 Advanced memory recall capabilities, allowing users to query their digital history
- 📊 Data visualization and timeline view

For a detailed list of current and planned features, please see our [TODO list](TODO.md).

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

These features will leverage Chroma vector database and large language models to provide accurate, context-aware responses based on your captured digital activities.

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
