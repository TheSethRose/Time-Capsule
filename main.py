# main.py

import time
import queue
import logging
import os
from modules.database_manager import DatabaseManager
from modules.plugin_manager import TimeCapsuleApplication
from modules.config_manager import config

# Configure logging to write to a file with a specific format
logging.basicConfig(filename='time_capsule.log', level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def start_time_capsule(plugin_manager):
    """Start the Time Capsule application with the given plugin manager."""
    try:
        clear_screen()  # Clear the screen before starting Time Capsule
        logging.info("Starting Time Capsule")

        # Initialize the database manager and audio queue
        db_manager = DatabaseManager(config.get_database_path())
        audio_q = queue.Queue()

        # Get the list of enabled plugins
        enabled_plugins = plugin_manager.get_enabled_plugins()
        logging.info(f"Enabled plugins: {list(enabled_plugins.keys())}")

        # Start each enabled plugin
        for plugin_name, plugin_instance in enabled_plugins.items():
            logging.info(f"Starting plugin: {plugin_name}")
            try:
                plugin_instance.start(audio_queue=audio_q, db_manager=db_manager)
                logging.info(f"Plugin {plugin_name} started successfully")
            except Exception as e:
                logging.error(f"Error starting plugin {plugin_name}: {str(e)}", exc_info=True)
                raise

        print("Time Capsule started. Press Ctrl+C to stop.")
        logging.info("Time Capsule started. Press Ctrl+C to stop.")

        # Main loop to keep the application running
        while True:
            time.sleep(1)
            running_plugins = [name for name, plugin in enabled_plugins.items() if plugin.is_running()]
            logging.info(f"Currently running plugins: {running_plugins}")
            if not all(plugin.is_running() for plugin in enabled_plugins.values()):
                raise Exception("One or more plugins stopped unexpectedly.")

    except KeyboardInterrupt:
        # Handle user interrupt (Ctrl+C)
        print("Stopping Time Capsule...")
        logging.info("Stopping Time Capsule...")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}", exc_info=True)
    finally:
        # Ensure all plugins are stopped properly
        if 'enabled_plugins' in locals():
            for plugin_name, plugin in enabled_plugins.items():
                try:
                    logging.info(f"Stopping plugin: {plugin_name}")
                    plugin.stop()
                    logging.info(f"Plugin {plugin_name} stopped successfully")
                except Exception as e:
                    logging.error(f"Error stopping plugin {plugin_name}: {str(e)}", exc_info=True)
        logging.info("Time Capsule stopped")

class TimeCapsuleApp(TimeCapsuleApplication):
    """Main application class for Time Capsule."""
    def start_time_capsule(self):
        logging.info("TimeCapsuleApp.start_time_capsule called")
        start_time_capsule(self.plugin_manager)

if __name__ == "__main__":
    app = TimeCapsuleApp()
    try:
        logging.info("Starting TimeCapsuleApp")
        app.run()
    except Exception as e:
        logging.error(f"Unhandled exception in main: {str(e)}", exc_info=True)
    finally:
        logging.info("TimeCapsuleApp finished")
    print("Exiting Time Capsule. Goodbye!")
