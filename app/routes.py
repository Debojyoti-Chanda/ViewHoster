import os
from flask import Blueprint, send_from_directory

from app.utils import screenshot_dir

routes = Blueprint("routes", __name__)

@routes.route("/screenshots/<filename>")
def serve_screenshot(filename):
    return send_from_directory(screenshot_dir, filename)

@routes.route("/")
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
