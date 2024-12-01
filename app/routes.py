import os
from flask import Blueprint, send_from_directory, jsonify, request, render_template

from app.utils import screenshot_dir, thumbnail_dir, create_thumbnail, extract_text_from_image

routes = Blueprint("routes", __name__)

@routes.route("/screenshots/<filename>")
def serve_screenshot(filename):
    return send_from_directory(screenshot_dir, filename)

@routes.route("/thumbnails/<filename>")
def serve_thumbnail(filename):
    """Serve thumbnail images."""
    return send_from_directory(thumbnail_dir, filename)


@routes.route("/")
def list_screenshots():
    """Display the list of screenshots with thumbnails."""
    # Filter only PNG files and ignore the thumbnail subdirectory
    files = [f for f in os.listdir(screenshot_dir) if f.endswith(".png") and not f.startswith("thumbnails")]
    files.sort(reverse=True)  # Show latest screenshots first

    # Create file links with thumbnails
    for file in files:
        thumbnail_path = os.path.join(thumbnail_dir, file)
        screenshot_path = os.path.join(screenshot_dir, file)
        
        # Generate thumbnail if it doesn't exist
        if not os.path.exists(thumbnail_path):
            create_thumbnail(screenshot_path, thumbnail_path)
        
    return render_template("index.html", files=files)

@routes.route("/extract_text/<filename>", methods=["GET"])
def extract_text(filename):
    """
    Extract and return text from the specified image file.
    """
    image_path = os.path.join(screenshot_dir, filename)
    if not os.path.exists(image_path):
        return jsonify({"error": "File not found"}), 404

    try:
        extracted_text = extract_text_from_image(image_path)
        return jsonify({"filename": filename, "text": extracted_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500