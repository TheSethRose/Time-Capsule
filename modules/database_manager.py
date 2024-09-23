# modules/database_manager.py

import chromadb
import logging
import os
from config.config import DATABASE_PATH

class DatabaseManager:
    def __init__(self):
        self.db_path = DATABASE_PATH
        self.client = self.create_connection()
        self.preferences_collection = self.client.get_or_create_collection(name="preferences")
        self.commands_collection = self.client.get_or_create_collection(name="commands")

    def create_connection(self):
        """Create a connection to the Chroma database."""
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

            client = chromadb.PersistentClient(path=self.db_path)
            print(f"Chroma database connected successfully at {self.db_path}")
            return client
        except Exception as e:
            print(f"Error connecting to Chroma database: {e}")
            return None

    def set_preference(self, user_id, key, value):
        """Set a user preference."""
        try:
            self.preferences_collection.upsert(
                ids=[f"{user_id}_{key}"],
                documents=[value],
                metadatas=[{"user_id": user_id, "key": key}]
            )
            print(f"Preference '{key}' set to '{value}' for user {user_id}.")
        except Exception as e:
            print(f"Error setting preference: {e}")

    def get_preference(self, user_id, key):
        """Retrieve a user preference."""
        try:
            results = self.preferences_collection.get(
                where={"user_id": user_id, "key": key}
            )
            return results['documents'][0] if results['documents'] else None
        except Exception as e:
            print(f"Error retrieving preference: {e}")
            return None

    def add_command(self, user_id, command_text):
        """Add a learned command for a user."""
        try:
            self.commands_collection.add(
                ids=[f"{user_id}_{command_text}"],
                documents=[command_text],
                metadatas=[{"user_id": user_id}]
            )
            logging.info(f"Added to Database (User {user_id}): '{command_text}'")
        except Exception as e:
            logging.error(f"Error adding command to database: {e}")

    def get_commands(self, user_id):
        """Retrieve all commands for a user."""
        try:
            results = self.commands_collection.get(
                where={"user_id": user_id}
            )
            return results['documents']
        except Exception as e:
            print(f"Error retrieving commands: {e}")
            return []
