import pyautogui
from PIL import Image
# Capture the screenshot and explicitly save it
screenshot = pyautogui.screenshot()
screenshot.save("test_screenshot.png")  # Explicit save using PIL
print("Screenshot saved using Pillow!")
# import os

# print("Current working directory:", os.getcwd())