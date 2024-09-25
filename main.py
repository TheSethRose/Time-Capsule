# main.py

import logging
from flask import Flask
from time_capsule import TimeCapsule
from modules.web_server import configure_routes
import atexit
import signal
import sys
import socket
from werkzeug.serving import make_server
import threading
import os
import time

DEBUG_LOG = "time_capsule_debug.log"

def clear_debug_log():
    """Clear the contents of the debug log file."""
    try:
        open(DEBUG_LOG, 'w').close()
    except Exception as e:
        logging.error(f"Error clearing debug log: {e}")

def configure_logging():
    """Configure logging settings for the application."""
    clear_debug_log()
    logging.basicConfig(
        filename=DEBUG_LOG,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    logging.getLogger('urllib3').setLevel(logging.WARNING)

def create_app(shutdown_event):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    time_capsule = TimeCapsule()
    time_capsule.initialize()
    configure_routes(app, time_capsule, shutdown_event)
    return app, time_capsule

def shutdown_server(server, time_capsule):
    """Shutdown the server and stop the Time Capsule."""
    print("Shutting down Time Capsule Server...")
    logging.info("Shutting down Time Capsule...")
    time_capsule.stop()
    if server:
        server.shutdown()
    print("Server shutdown complete.")
    logging.info("Server shutting down...")

def force_quit():
    """Force quit the application."""
    logging.error("Force quitting the application...")
    os._exit(1)

def signal_handler(signum, frame):
    """Handle system signals for graceful shutdown."""
    logging.info(f"Received signal {signum}. Initiating shutdown...")
    shutdown_event.set()

def is_port_in_use(port):
    """Check if a given port is already in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def main():
    """Main function to run the Time Capsule application."""
    configure_logging()
    logging.info("Initializing Time Capsule...")

    global shutdown_event
    shutdown_event = threading.Event()

    app, time_capsule = create_app(shutdown_event)

    global server
    server = None

    host = '0.0.0.0'
    for port in range(5000, 5011):
        if not is_port_in_use(port):
            try:
                server = make_server(host, port, app)
                print(f"Starting Time Capsule Server on port {port}...")
                print("Time Capsule is now running.")
                print(f"\nAccess the web interface at http://localhost:{port}")

                atexit.register(shutdown_server, server, time_capsule)

                signal.signal(signal.SIGINT, signal_handler)
                signal.signal(signal.SIGTERM, signal_handler)

                server_thread = threading.Thread(target=server.serve_forever)
                server_thread.start()

                while not shutdown_event.is_set():
                    time.sleep(1)

                logging.info("Initiating graceful shutdown...")
                shutdown_server(server, time_capsule)

                server_thread.join(timeout=10)

                if server_thread.is_alive():
                    logging.warning("Graceful shutdown timed out. Force quitting...")
                    force_quit()

                break
            except Exception as e:
                logging.error(f"Error starting server on port {port}: {e}")
    else:
        logging.error("No available ports found between 5000 and 5010.")
        print("No available ports found. Please check your network configuration.")
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
