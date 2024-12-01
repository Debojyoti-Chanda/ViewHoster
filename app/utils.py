import os
import time
import pyautogui

# # Directory to store screenshots
# screenshot_dir = "screenshots"

# Directory to store screenshots
base_dir = os.path.dirname(os.path.abspath(__file__))  # Base directory of the app
screenshot_dir = os.path.join(base_dir, "..", "screenshots")  # Absolute path for screenshots directory

# Ensure the screenshot directory exists
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

def take_screenshot():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(screenshot_dir, filename)
    
    # Capture and save the screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print(f"Screenshot saved: {filepath}")

def delete_old_screenshots():
    current_time = time.time()
    for filename in os.listdir(screenshot_dir):
        filepath = os.path.join(screenshot_dir, filename)
        if os.path.isfile(filepath):
            file_age = current_time - os.path.getmtime(filepath)
            if file_age > 20 * 60:  # 20 minutes in seconds
                os.remove(filepath)
                print(f"Deleted old screenshot: {filepath}")
