import importlib
import os
import logging
from modules.config_manager import config

class PluginManager:
    """Manager for loading and managing plugins."""
    def __init__(self):
        self.config = config
        self.plugins = self._load_plugins()

    def _load_plugins(self):
        """Load plugins from the plugins directory."""
        plugins = {}
        plugin_dir = "plugins"
        logging.debug(f"Loading plugins from directory: {plugin_dir}")
        for item in os.listdir(plugin_dir):
            if os.path.isdir(os.path.join(plugin_dir, item)) and not item.startswith("__"):
                plugin_name = item.replace("_", " ").title().replace(" ", "")
                enabled = self.config.get_plugin_state(plugin_name)
                logging.debug(f"Found plugin: {plugin_name}, enabled: {enabled}")
                plugins[plugin_name] = {
                    'enabled': enabled,
                    'instance': None
                }
                if enabled:
                    logging.info(f"Loaded plugin: {plugin_name}")
        return plugins

    def get_plugins(self):
        """Get the state of all plugins."""
        return {name: info['enabled'] for name, info in self.plugins.items()}

    def get_enabled_plugins(self):
        """Get instances of all enabled plugins."""
        enabled_plugins = {}
        for name, info in self.plugins.items():
            if info['enabled']:
                plugin_instance = self._get_plugin_instance(name)
                if plugin_instance:
                    enabled_plugins[name] = plugin_instance
        logging.debug(f"Enabled plugins: {list(enabled_plugins.keys())}")
        return enabled_plugins

    def _get_plugin_instance(self, plugin_name):
        """Get an instance of a plugin by name."""
        if self.plugins[plugin_name]['instance'] is None:
            module_name = ''.join(['_' + c.lower() if c.isupper() else c for c in plugin_name]).lstrip('_')
            full_module_path = f"plugins.{module_name}.{module_name}"
            try:
                logging.debug(f"Attempting to import module: {full_module_path}")
                module = importlib.import_module(full_module_path)
                plugin_class = getattr(module, plugin_name)
                self.plugins[plugin_name]['instance'] = plugin_class()
                logging.debug(f"Successfully loaded plugin: {plugin_name}")
            except (ImportError, AttributeError) as e:
                logging.error(f"Error loading plugin {plugin_name}: {e}")
                return None
        return self.plugins[plugin_name]['instance']

    def toggle_plugin(self, plugin_name):
        """Toggle the enabled state of a plugin."""
        if plugin_name in self.plugins:
            self.plugins[plugin_name]['enabled'] = not self.plugins[plugin_name]['enabled']
            self.config.set_plugin_state(plugin_name, self.plugins[plugin_name]['enabled'])
            return True
        return False

    def get_plugin_statuses(self):
        """Get the status of all plugins."""
        return {name: {'enabled': info['enabled'], 'loaded': info['instance'] is not None} for name, info in self.plugins.items()}
