# Time Capsule TODO List

This document tracks the current status of features and planned improvements for the Time Capsule project, listed in a suggested order of implementation.

## Current Status and Future Tasks

| Status | Task | Notes |
|--------|------|-------|
| ✅ | Add microphone recording functionality | Implemented in `modules/audio_recorder.py` |
| ✅ | Implement Fast-Whisper model for audio transcription | Implemented in `modules/transcription_service.py` |
| ✅ | Integrate Chroma vector database for efficient information storage/retrieval | Implemented in `modules/database_manager.py` |
| ⬜ | Implement data encryption for privacy | Update `modules/database_manager.py` and add encryption utilities |
| ⬜ | Add support for multiple audio input sources | Update `modules/audio_recorder.py` |
| ⬜ | Implement sophisticated search functionality | Update `modules/database_manager.py` and potentially create `modules/search_engine.py` |
| ⬜ | Add typed text capture | Create new module `modules/text_capture.py` |
| ⬜ | Implement screen recording functionality | Create new module `modules/screen_recorder.py` |
| ⬜ | Add transcription service for screen recording | Update `modules/transcription_service.py` |
| ⬜ | Add support for video capture and transcription | Create new module `modules/video_capture.py` and update `modules/transcription_service.py` |
| ⬜ | Implement activity categorization and tagging | Update `modules/database_manager.py` and potentially create `modules/activity_classifier.py` |
| ⬜ | Add export functionality for captured data | Create new module `modules/data_exporter.py` |
| ⬜ | Implement timeline view of captured activities | Create new module `modules/timeline_generator.py` |
| ⬜ | Add data visualization features | Create new module `modules/data_visualizer.py` |
| ⬜ | Implement LLM for natural language interaction with digital memory | Create new module `modules/llm_interface.py` |
| ⬜ | Develop advanced memory recall capabilities | Update `modules/database_manager.py` and create `modules/memory_recall.py` |
| ⬜ | Add voice command support for application control | Create new module `modules/voice_commands.py` |
| ⬜ | Develop user interface for interaction and search | Create new directory `ui/` with relevant files |
| ⬜ | Create plugin system for extensibility | Create new directory `plugins/` and update `main.py` |
| ⬜ | Implement cloud sync capabilities | Create new module `modules/cloud_sync.py` |
| ⬜ | Develop mobile app version | Create new repository for mobile app |
