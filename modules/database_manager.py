# modules/database_manager.py

import chromadb
from chromadb.config import Settings
from modules.config_manager import config

class DatabaseManager:
    """Manager for handling database operations."""
    def __init__(self, database_path=None):
        # Initialize the ChromaDB client with the specified database path
        self.client = chromadb.PersistentClient(
            path=database_path or config.get_database_path(),
            settings=Settings(
                allow_reset=True,
                anonymized_telemetry=False
            )
        )
        # Get or create the collection for storing transcriptions
        self.collection = self.client.get_or_create_collection("transcriptions")

    def store_transcription(self, text, language, confidence):
        """Store a transcription in the database."""
        self.collection.add(
            documents=[text],
            metadatas=[{"language": language, "confidence": confidence}],
            ids=[f"transcription_{self.collection.count() + 1}"]
        )

    # Add more methods as needed for querying and managing the database
