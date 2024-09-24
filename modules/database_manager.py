# modules/database_manager.py

import chromadb
import logging
from chromadb.config import Settings
from config.config import config

class DatabaseManager:
    def __init__(self, database_path=None):
        self.client = chromadb.PersistentClient(
            path=database_path or config.get_database_path(),
            settings=Settings(
                allow_reset=True,
                anonymized_telemetry=False
            )
        )
        self.collection = self.client.get_or_create_collection("transcriptions")

    def store_transcription(self, text, language, confidence):
        self.collection.add(
            documents=[text],
            metadatas=[{"language": language, "confidence": confidence}],
            ids=[f"transcription_{self.collection.count() + 1}"]
        )

    # Add more methods as needed for querying and managing the database
