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

# Delete screenshots older than 20 minutes
def delete_old_screenshots():
    current_time = time.time()
    for filename in os.listdir(screenshot_dir):
        filepath = os.path.join(screenshot_dir, filename)
        if os.path.isfile(filepath):
            file_age = current_time - os.path.getmtime(filepath)
            if file_age > 20 * 60:  # 20 minutes in seconds
                os.remove(filepath)
                print(f"Deleted old screenshot: {filepath}")

# Schedule screenshots
schedule.every(30).seconds.do(take_screenshot)  # Take a screenshot every 30 seconds
schedule.every(1).minutes.do(delete_old_screenshots)  # Run cleanup every 1 minutes

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
    file_links = [f"<li><a href='/screenshots/{file}' target='_blank'>{file}</a></li>" for file in files]

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Available Screenshots</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            header {{
                background-color: #6200ea;
                color: white;
                padding: 20px;
                text-align: center;
                width: 100%;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                margin: 0;
                font-size: 2rem;
            }}
            ul {{
                list-style: none;
                padding: 0;
                margin: 20px auto;
                width: 80%;
                max-width: 600px;
            }}
            li {{
                background: white;
                margin: 10px 0;
                padding: 10px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }}
            li a {{
                text-decoration: none;
                color: #6200ea;
                font-weight: bold;
            }}
            li a:hover {{
                color: #3700b3;
            }}
            footer {{
                margin-top: 20px;
                padding: 10px;
                text-align: center;
                color: #888;
                font-size: 0.9rem;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Available Screenshots</h1>
        </header>
        <ul>
            {''.join(file_links)}
        </ul>
        <footer>
            <p>Access this page from your phone using the server's IP and port.</p>
            <p>Created by Debojyoti Chanda. </p>
        </footer>
    </body>
    </html>
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
