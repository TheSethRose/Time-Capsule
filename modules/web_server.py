from flask import render_template, request, jsonify
from modules.config_manager import config
import psutil
import os
import time
import logging

DEBUG_LOG_PATH = "/Users/sethrose/Documents/Development/python-projects/Time-Capsule/time_capsule_debug.log"

def configure_routes(app, time_capsule, shutdown_event):
    @app.route('/')
    def index():
        plugins = time_capsule.get_plugins()
        database_path = config.get_database_path()
        refresh_interval = config.get_refresh_interval()
        debug_log = get_debug_log()
        return render_template('index.html',
                               plugins=plugins,
                               database_path=database_path,
                               refresh_interval=refresh_interval,
                               debug_log=debug_log)

    @app.route('/start_time_capsule', methods=['POST'])
    def start_time_capsule():
        success = time_capsule.start()
        return jsonify({'success': success})

    @app.route('/stop_time_capsule', methods=['POST'])
    def stop_time_capsule():
        success = time_capsule.stop()
        return jsonify({'success': success})

    @app.route('/toggle_plugin/<plugin_name>', methods=['POST'])
    def toggle_plugin(plugin_name):
        success = time_capsule.toggle_plugin(plugin_name)
        return jsonify({'success': success})

    @app.route('/status')
    def get_status():
        status = time_capsule.get_status()
        status.update({
            'cpu_usage': psutil.cpu_percent(),
            'memory_usage': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'total_storage': get_database_size(),
            'uptime': get_uptime(),
            'debug_log': get_debug_log()
        })
        return jsonify(status)

    @app.route('/stop_server', methods=['POST'])
    def stop_server():
        shutdown_event.set()
        return jsonify({'success': True})

def get_database_size():
    db_path = config.get_database_path()
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(db_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / (1024 * 1024 * 1024)  # Convert to GB

def get_uptime():
    return int(time.time() - psutil.boot_time())

def get_debug_log():
    if os.path.exists(DEBUG_LOG_PATH):
        with open(DEBUG_LOG_PATH, "r") as f:
            return "".join(f.readlines()[-100:])  # Return last 100 lines
    return "No log data available."
