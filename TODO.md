# Time Capsule TODO List

This document tracks the current status of features and planned improvements for the Time Capsule project, listed in a suggested order of implementation to achieve MVP and beyond.

Note: This was created by an LLM, so some of the todo items may be incorrect or misaligned. Please take that into consideration when working through this list.

## Current Status and Future Tasks

| Status | Task | Notes |
|--------|------|-------|
| ✅ | Add microphone recording functionality | Implemented in `modules/audio_recorder.py` |
| ✅ | Implement Fast-Whisper model for audio transcription | Implemented in `modules/transcription_service.py` |
| ✅ | Integrate Chroma vector database for efficient information storage/retrieval | Implemented in `modules/database_manager.py` |
| ⬜ | Create plugin system for extensibility | Create new directory `plugins/` and update `main.py` |
| ⬜ | Convert microphone recording to a plugin | Move `audio_recorder.py` to `plugins/audio_recorder/` |
| ⬜ | Implement screen recording as a plugin | Create `plugins/screen_recorder/` |
| ⬜ | Implement folder monitoring as a plugin | Create `plugins/folder_monitor/` |
| ⬜ | Add transcription service for screen recording | Update `modules/transcription_service.py` |
| ⬜ | Develop basic web interface for database CRUD operations | Create new directory `web/` with relevant files |
| ⬜ | Implement sophisticated search functionality | Update `modules/database_manager.py` and potentially create `modules/search_engine.py` |
| ⬜ | Integrate LLM for chatting with captured data | Create new module `modules/llm_interface.py` |
| ⬜ | Implement basic activity categorization and tagging | Update `modules/database_manager.py` |
| ⬜ | Add export functionality for captured data | Create new module `modules/data_exporter.py` |
| ⬜ | Implement simple timeline view of captured activities | Create new module `modules/timeline_generator.py` |
| ⬜ | Add basic data visualization features | Create new module `modules/data_visualizer.py` |
| ⬜ | Develop simple memory recall capabilities | Update `modules/database_manager.py` and create `modules/memory_recall.py` |
| ⬜ | Add support for multiple audio input sources | Update `plugins/audio_recorder/` |
| ⬜ | Add voice command support for application control | Create new plugin `plugins/voice_commands/` |
| ⬜ | Enhance web interface with advanced features | Update `web/` directory |
| ⬜ | Implement advanced activity categorization and tagging | Create `modules/activity_classifier.py` |
| ⬜ | Develop advanced memory recall capabilities | Update `modules/memory_recall.py` |
| ⬜ | Implement cloud sync capabilities | Create new module `modules/cloud_sync.py` |
| ⬜ | Implement data encryption for privacy | Update `modules/database_manager.py` and add encryption utilities |
| ⬜ | Develop mobile app version | Create new repository for mobile app |
