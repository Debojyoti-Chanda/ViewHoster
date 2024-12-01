import os
import time
import pyautogui
from PIL import Image

import pytesseract

# # Directory to store screenshots
# screenshot_dir = "screenshots"

# Directory to store screenshots
base_dir = os.path.dirname(os.path.abspath(__file__))  # Base directory of the app
screenshot_dir = os.path.join(base_dir, "..", "screenshots")  # Absolute path for screenshots directory

thumbnail_dir = os.path.join(screenshot_dir, "thumbnails")
os.makedirs(thumbnail_dir, exist_ok=True)

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
            if file_age > 10 * 60:  # 10 minutes in seconds
                os.remove(filepath)
                print(f"Deleted old screenshot: {filepath}")

# Utility function to create a thumbnail
def create_thumbnail(image_path, thumbnail_path, size=(100, 100)):
    """Generate a thumbnail for the given image."""
    with Image.open(image_path) as img:
        img.thumbnail(size)
        img.save(thumbnail_path, "PNG")

# Function to extract text from an image
def extract_text_from_image(image_path):
    """Extract text from an image using Tesseract OCR."""
    with Image.open(image_path) as img:
        text = pytesseract.image_to_string(img)
    return text