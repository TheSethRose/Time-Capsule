# main.py

import time
import queue
import logging
import os
from modules.database_manager import DatabaseManager
from modules.plugin_manager import TimeCapsuleApplication
from config.config import config

logging.basicConfig(filename='time_capsule.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_time_capsule(plugin_manager):
    try:
        clear_screen()  # Clear the screen before starting Time Capsule
        logging.debug("Starting Time Capsule")
        db_manager = DatabaseManager(config.get_database_path())
        audio_q = queue.Queue()
        enabled_plugins = plugin_manager.get_enabled_plugins()

        if not enabled_plugins:
            logging.warning("No plugins are enabled. Time Capsule will not perform any actions.")
            return

        logging.debug(f"Enabled plugins: {list(enabled_plugins.keys())}")

        for plugin_name, plugin_instance in enabled_plugins.items():
            logging.debug(f"Starting plugin: {plugin_name}")
            try:
                plugin_instance.start(audio_queue=audio_q, db_manager=db_manager)
                logging.debug(f"Plugin {plugin_name} started successfully")
            except Exception as e:
                logging.error(f"Error starting plugin {plugin_name}: {str(e)}", exc_info=True)
                raise

        print("Time Capsule started. Press Ctrl+C to stop.")
        logging.info("Time Capsule started. Press Ctrl+C to stop.")

        while True:
            time.sleep(1)
            running_plugins = [name for name, plugin in enabled_plugins.items() if plugin.is_running()]
            logging.debug(f"Currently running plugins: {running_plugins}")
            if not all(plugin.is_running() for plugin in enabled_plugins.values()):
                raise Exception("One or more plugins stopped unexpectedly.")

    except KeyboardInterrupt:
        print("Stopping Time Capsule...")
        logging.info("Stopping Time Capsule...")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}", exc_info=True)
    finally:
        if 'enabled_plugins' in locals():
            for plugin_name, plugin in enabled_plugins.items():
                try:
                    logging.debug(f"Stopping plugin: {plugin_name}")
                    plugin.stop()
                    logging.debug(f"Plugin {plugin_name} stopped successfully")
                except Exception as e:
                    logging.error(f"Error stopping plugin {plugin_name}: {str(e)}", exc_info=True)
        logging.debug("Time Capsule stopped")

class TimeCapsuleApp(TimeCapsuleApplication):
    def start_time_capsule(self):
        logging.debug("TimeCapsuleApp.start_time_capsule called")
        start_time_capsule(self.plugin_manager)

if __name__ == "__main__":
    app = TimeCapsuleApp()
    try:
        logging.debug("Starting TimeCapsuleApp")
        app.run()
    except Exception as e:
        logging.error(f"Unhandled exception in main: {str(e)}", exc_info=True)
    finally:
        logging.debug("TimeCapsuleApp finished")
    print("Exiting Time Capsule. Goodbye!")
