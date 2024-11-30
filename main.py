import pyautogui
from PIL import Image
import schedule
import threading
import time
import os
from flask import Flask, send_from_directory

app = Flask(__name__)
screenshot_dir = "screenshots"

# Ensure the screenshot directory exists
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

# Take a screenshot every 30 seconds
def take_screenshot():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(screenshot_dir, filename)
    
    # Capture and save the screenshot using Pillow
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)  # Explicit save using Pillow
    print(f"Screenshot saved: {filepath}")

# Schedule screenshots
schedule.every(30).seconds.do(take_screenshot)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Flask route to serve screenshots
@app.route("/screenshots/<filename>")
def serve_screenshot(filename):
    return send_from_directory(screenshot_dir, filename)

@app.route("/")
def list_screenshots():
    files = os.listdir(screenshot_dir)
    files.sort(reverse=True)  # Show latest screenshots first
    file_links = [f"<li><a href='/screenshots/{file}'>{file}</a></li>" for file in files]
    return f"""
    <h1>Available Screenshots</h1>
    <ul>
        {''.join(file_links)}
    </ul>
    <p>Access this page from your phone using the server's IP and port.</p>
    """

# Run Flask app
def run_server():
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    # Start scheduler in a separate thread
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()

    # Start the Flask server
    print("Starting server...")
    run_server()
