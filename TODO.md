# Time Capsule TODO List

This document tracks the current status of features and planned improvements for the Time Capsule project, listed in a suggested order of implementation to achieve MVP and beyond.

## Core Functionality (MVP)

| Status | Task | Notes |
|--------|------|-------|
| ✅ | Add microphone recording functionality | Implemented in `plugins/audio_recorder/audio_recorder.py` |
| ✅ | Implement Fast-Whisper model for audio transcription | Implemented in `plugins/transcription_service/transcription_service.py` |
| ✅ | Integrate Chroma vector database for efficient information storage/retrieval | Implemented in `modules/database_manager.py` |
| ⬜ | Create interactive CLI menu system | Update `main.py` to include main menu and plugin management |
| ⬜ | Implement plugin detection and management | Create new module `modules/plugin_manager.py` |
| ⬜ | Create configuration system for enabling/disabling plugins | Update `config/config.py` to store plugin states |
| ⬜ | Refactor main application logic to use enabled plugins | Update `main.py` to load and use enabled plugins |
| ⬜ | Implement basic LLM interface for querying stored data | Create new module `modules/llm_interface.py` |
| ⬜ | Develop web interface for database management | Create new directory `web/` with relevant files |
| ⬜ | Implement data visualization in web interface | Update `web/` directory |
| ⬜ | Create timeline view of captured activities | Update `web/` directory |
| ⬜ | Implement activity categorization and tagging | Update `modules/database_manager.py` |
| ⬜ | Develop memory recall features | Create new module `modules/memory_recall.py` |
| ⬜ | Implement sophisticated search functionality | Update `modules/database_manager.py` |
| ⬜ | Add export functionality for captured data | Create new module `modules/data_exporter.py` |

## Planned Plugins

| Status | Task | Notes |
|--------|------|-------|
| ⬜ | Implement screen recording as a plugin | Create `plugins/screen_recorder/` |
| ⬜ | Implement folder monitoring as a plugin | Create `plugins/folder_monitor/` |
| ⬜ | Add voice command support for application control | Create `plugins/voice_commands/` |

## Future Enhancements

| Status | Task | Notes |
|--------|------|-------|
| ⬜ | Enhance web interface with advanced features | Update `web/` directory |
| ⬜ | Implement data encryption for privacy | Update `modules/database_manager.py` and add encryption utilities |
| ⬜ | Develop mobile app version | Create new repository for mobile app |
