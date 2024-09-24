import importlib
import os
import npyscreen
import logging
import curses
from config.config import config

class GreenOnBlackTheme(npyscreen.ThemeManager):
    default_colors = {
        'DEFAULT': 'GREEN_BLACK',
        'FORMDEFAULT': 'GREEN_BLACK',
        'NO_EDIT': 'YELLOW_BLACK',
        'STANDOUT': 'CYAN_BLACK',
        'CURSOR': 'WHITE_BLACK',
        'CURSOR_INVERSE': 'BLACK_WHITE',
        'LABEL': 'GREEN_BLACK',
        'LABELBOLD': 'WHITE_BLACK',
        'CONTROL': 'YELLOW_BLACK',
        'IMPORTANT': 'GREEN_BLACK',
        'SAFE': 'GREEN_BLACK',
        'WARNING': 'YELLOW_BLACK',
        'DANGER': 'RED_BLACK',
        'CRITICAL': 'BLACK_RED',
        'GOOD': 'GREEN_BLACK',
        'GOODHL': 'GREEN_BLACK',
        'VERYGOOD': 'BLACK_GREEN',
        'CAUTION': 'YELLOW_BLACK',
        'CAUTIONHL': 'BLACK_YELLOW',
    }

class CustomMultiSelect(npyscreen.MultiSelect):
    def __init__(self, *args, **keywords):
        super(CustomMultiSelect, self).__init__(*args, **keywords)
        self.how_exited = None

    def display_value(self, vl):
        selected = self.value and vl in self.value
        return '(●) ' + str(vl) if selected else '(○) ' + str(vl)

class PluginManagementForm(npyscreen.ActionForm):
    def create(self):
        self.plugin_manager = self.parentApp.plugin_manager
        self.plugins = self.add(CustomMultiSelect,
                                values=self.get_plugin_list(),
                                max_height=10,
                                name="Plugins",
                                scroll_exit=True)
        self.plugins.add_handlers({" ": self.toggle_plugin})

    def get_plugin_list(self):
        return [f"{name}" for name in self.plugin_manager.get_plugins().keys()]

    def toggle_plugin(self, input):
        plugin_name = self.plugins.values[self.plugins.cursor_line]
        self.plugin_manager.toggle_plugin(plugin_name)
        self.plugins.value = [
            i for i, (name, enabled) in enumerate(self.plugin_manager.get_plugins().items())
            if enabled
        ]
        self.plugins.display()

    def beforeEditing(self):
        self.plugins.value = [
            i for i, (name, enabled) in enumerate(self.plugin_manager.get_plugins().items())
            if enabled
        ]

    def on_ok(self):
        self.parentApp.switchFormPrevious()

    def on_cancel(self):
        self.parentApp.switchFormPrevious()

class MainForm(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.TitleText, name="Welcome to Time Capsule", editable=False)
        self.add(npyscreen.ButtonPress, name="Start Time Capsule", when_pressed_function=self.start_time_capsule)
        self.add(npyscreen.ButtonPress, name="Manage Plugins", when_pressed_function=self.manage_plugins)

    def start_time_capsule(self):
        logging.debug("MainForm.start_time_capsule called")
        self.parentApp.setNextForm(None)
        self.parentApp.switchFormNow()
        curses.endwin()  # End the curses window
        self.parentApp.start_time_capsule()

    def manage_plugins(self):
        self.parentApp.switchForm("PLUGINS")

    def on_ok(self):
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.parentApp.setNextForm(None)

class PluginManager:
    def __init__(self):
        self.config = config
        self.plugins = self._load_plugins()

    def _load_plugins(self):
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
        return plugins

    def get_plugins(self):
        return {name: info['enabled'] for name, info in self.plugins.items()}

    def get_enabled_plugins(self):
        enabled_plugins = {}
        for name, info in self.plugins.items():
            if info['enabled']:
                plugin_instance = self._get_plugin_instance(name)
                if plugin_instance:
                    enabled_plugins[name] = plugin_instance
        logging.debug(f"Enabled plugins: {list(enabled_plugins.keys())}")
        return enabled_plugins

    def _get_plugin_instance(self, plugin_name):
        if self.plugins[plugin_name]['instance'] is None:
            # Convert CamelCase to snake_case for the module name
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
        self.plugins[plugin_name]['enabled'] = not self.plugins[plugin_name]['enabled']
        self.config.set_plugin_state(plugin_name, self.plugins[plugin_name]['enabled'])
        logging.debug(f"Toggled plugin {plugin_name}: enabled = {self.plugins[plugin_name]['enabled']}")

def get_plugin_management_form():
    return PluginManagementForm

def get_main_form():
    return MainForm

def set_theme():
    npyscreen.setTheme(GreenOnBlackTheme)

class TimeCapsuleApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        set_theme()
        self.plugin_manager = PluginManager()
        self.addForm("MAIN", get_main_form(), name="Time Capsule")
        self.addForm("PLUGINS", get_plugin_management_form(), name="Manage Plugins")

    def start_time_capsule(self):
        logging.debug("TimeCapsuleApplication.start_time_capsule called")
        from main import start_time_capsule  # Import here to avoid circular import
        start_time_capsule(self.plugin_manager)
