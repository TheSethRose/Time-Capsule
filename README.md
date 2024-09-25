# Time Capsule

Time Capsule is a powerful tool designed to continuously capture and store your digital activities, creating a comprehensive digital memory. It provides a core system for data management with a web interface for interaction and optional plugins for various data capture methods.

## ✨ Current Features

- 🎙️ Real-time microphone recording
- 🗣️ Speech-to-text transcription using Fast-Whisper library
- 💾 Database storage of transcribed text using Chroma vector database
- 🔌 Plugin system for extensibility
- ⚙️ Configurable settings via JSON configuration file
- 🖥️ Web interface for managing plugins and starting the application
- 📊 Transcription service for processing audio recordings
- 🌐 Flask-based web server for handling HTTP requests and responses
- 🔄 Real-time status updates including CPU, memory, and disk usage

## 🚀 Future Features

For a detailed list of planned features, please see our [TODO list](TODO.md).

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

4. Configure settings in `config.json` according to your preferences.

## 🖥️ Usage

Start the Time Capsule application:

```bash
python main.py
```

The application will start and display the URL for accessing the web interface. Use this interface to manage plugins and control the Time Capsule.

Press `Ctrl+C` in the terminal to initiate a graceful shutdown of the application.

## 🧩 Plugin System

Time Capsule uses a plugin system for extensibility. Plugins are located in the `plugins` directory. Each plugin should be in its own subdirectory and contain a main class that matches the plugin name.

To create a new plugin:

1. Create a new directory in the `plugins` folder with your plugin name.
2. Create a Python file with the same name as your plugin.
3. Implement the main plugin class with `start()` and `stop()` methods.

Plugins can be enabled or disabled through the web interface or by modifying the `config.json` file.

## 🔧 Configuration

The `config.json` file contains various settings for the application, including:

- Database path
- Audio recording settings
- Transcription settings
- Plugin states
- Web interface refresh interval

Modify this file to customize the behavior of Time Capsule.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For any questions, suggestions, or feedback, please feel free to reach out to me on X at [@TheSethRose](https://www.x.com/TheSethRose)

## ❤️ Support

<a href="https://www.buymeacoffee.com/TheSethRose" target="_blank"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee!&emoji=&slug=TheSethRose&button_colour=000000&font_colour=ffffff&font_family=Cookie&outline_colour=ffffff&coffee_colour=FFDD00" alt="Buy Me A Coffee!"></a>

## ⚠️ Disclaimer

Ensure compliance with all applicable laws and regulations when using this software, particularly regarding privacy and data protection. Time Capsule captures and stores personal data, so use it responsibly and with proper consent.
