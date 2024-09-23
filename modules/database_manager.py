# modules/database_manager.py

import sqlite3
from sqlite3 import Error
from config.config import DATABASE_PATH
import logging

class DatabaseManager:
    def __init__(self):
        self.db_file = DATABASE_PATH
        self.conn = self.create_connection()
        self.create_tables()

    def create_connection(self):
        """Create a database connection to the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_file, check_same_thread=False)
            print("Database connected successfully.")
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        """Create tables for user preferences and commands."""
        create_preferences_table = """
        CREATE TABLE IF NOT EXISTS preferences (
            user_id INTEGER,
            preference_key TEXT,
            preference_value TEXT,
            PRIMARY KEY (user_id, preference_key)
        );
        """

        create_commands_table = """
        CREATE TABLE IF NOT EXISTS commands (
            command_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            command_text TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES preferences (user_id)
        );
        """

        try:
            cursor = self.conn.cursor()
            cursor.execute(create_preferences_table)
            cursor.execute(create_commands_table)
            self.conn.commit()
            print("Tables created successfully.")
        except Error as e:
            print(f"Error creating tables: {e}")

    def set_preference(self, user_id, key, value):
        """Set a user preference."""
        insert_preference = """
        INSERT INTO preferences (user_id, preference_key, preference_value)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id, preference_key) DO UPDATE SET preference_value=excluded.preference_value;
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_preference, (user_id, key, value))
            self.conn.commit()
            print(f"Preference '{key}' set to '{value}' for user {user_id}.")
        except Error as e:
            print(f"Error setting preference: {e}")

    def get_preference(self, user_id, key):
        """Retrieve a user preference."""
        select_preference = """
        SELECT preference_value FROM preferences
        WHERE user_id = ? AND preference_key = ?;
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(select_preference, (user_id, key))
            result = cursor.fetchone()
            return result[0] if result else None
        except Error as e:
            print(f"Error retrieving preference: {e}")
            return None

    def add_command(self, user_id, command_text):
        """Add a learned command for a user."""
        insert_command = """
        INSERT INTO commands (user_id, command_text)
        VALUES (?, ?);
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_command, (user_id, command_text))
            self.conn.commit()
            logging.info(f"Added to Database (User {user_id}): '{command_text}'")
        except Error as e:
            logging.error(f"Error adding command to database: {e}")

    def get_commands(self, user_id):
        """Retrieve all commands for a user."""
        select_commands = """
        SELECT command_text FROM commands
        WHERE user_id = ?;
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(select_commands, (user_id,))
            results = cursor.fetchall()
            return [row[0] for row in results]
        except Error as e:
            print(f"Error retrieving commands: {e}")
            return []
