import os
from flask import Blueprint, send_from_directory

from app.utils import screenshot_dir, thumbnail_dir, create_thumbnail

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
    file_links = []
    for file in files:
        thumbnail_path = os.path.join(thumbnail_dir, file)
        screenshot_path = os.path.join(screenshot_dir, file)
        
        # Generate thumbnail if it doesn't exist
        if not os.path.exists(thumbnail_path):
            create_thumbnail(screenshot_path, thumbnail_path)
        
        # HTML for each file
        file_links.append(f"""
        <li>
            <a href='/screenshots/{file}' target='_blank'>
                <img src='/thumbnails/{file}' alt='{file}' style='width: 50px; height: auto; margin-right: 10px; vertical-align: middle;'>
                {file}
            </a>
        </li>
        """)

    # Render HTML
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ViewHoster</title>
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
                display: flex;
                align-items: center;
            }}
            li img {{
                border-radius: 4px;
            }}
            li a {{
                text-decoration: none;
                color: #6200ea;
                font-weight: bold;
                display: flex;
                align-items: center;
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
            <h1>ViewHoster</h1>
        </header>
        <ul>
            {''.join(file_links)}
        </ul>
        <footer>
            <p>Access this page from your phone using the server's IP and port.</p>
        </footer>
    </body>
    </html>
    """