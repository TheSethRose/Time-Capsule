import logging
from modules.database_manager import DatabaseManager
from modules.plugin_manager import PluginManager
from modules.config_manager import config
import threading

class TimeCapsule:
    def __init__(self):
        self.db_manager = None
        self.plugin_manager = PluginManager()
        self.running = False
        self.stop_event = threading.Event()

    def initialize(self):
        logging.info("Initializing Time Capsule...")
        self.db_manager = DatabaseManager(config.get_database_path())

    def start(self):
        if self.running:
            logging.warning("Time Capsule is already running")
            return False

        self.stop_event.clear()
        enabled_plugins = self.plugin_manager.get_enabled_plugins()
        for plugin_name, plugin_instance in enabled_plugins.items():
            try:
                plugin_instance.start(db_manager=self.db_manager)
                logging.debug(f"Started plugin: {plugin_name}")
            except Exception as e:
                logging.error(f"Error starting plugin {plugin_name}: {e}")
        self.running = True
        logging.info("Time Capsule started.")
        return True

    def stop(self):
        if not self.running:
            logging.warning("Time Capsule is not running")
            return False

        self.stop_event.set()
        enabled_plugins = self.plugin_manager.get_enabled_plugins()
        for plugin_name, plugin_instance in enabled_plugins.items():
            try:
                plugin_instance.stop()
                logging.debug(f"Stopped plugin: {plugin_name}")
            except Exception as e:
                logging.error(f"Error stopping plugin {plugin_name}: {e}")
        self.running = False
        logging.info("Time Capsule stopped.")
        return True

    def get_plugins(self):
        return self.plugin_manager.get_plugins()

    def toggle_plugin(self, plugin_name):
        return self.plugin_manager.toggle_plugin(plugin_name)

    def get_status(self):
        return {
            'running': self.running,
            'plugins': self.plugin_manager.get_plugin_statuses(),
        }
