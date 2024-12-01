import os
from flask import Blueprint, send_from_directory, jsonify, request

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
            <button onclick="extractText('{file}')">Extract Text</button>
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
        <script>
            function extractText(filename) {{
                fetch(`/extract_text/${{filename}}`)
                    .then(response => response.json())
                    .then(data => {{
                        if (data.error) {{
                            alert("Error extracting text: " + data.error);
                        }} else {{
                            const textModal = document.createElement("div");
                            textModal.style.position = "fixed";
                            textModal.style.top = "50%";
                            textModal.style.left = "50%";
                            textModal.style.transform = "translate(-50%, -50%)";
                            textModal.style.padding = "20px";
                            textModal.style.backgroundColor = "white";
                            textModal.style.border = "1px solid #ccc";
                            textModal.style.boxShadow = "0 4px 8px rgba(0,0,0,0.2)";
                            textModal.innerHTML = `
                                <h3>Extracted Text for ${{filename}}</h3>
                                <pre>${{data.text}}</pre>
                                <button onclick="document.body.removeChild(this.parentNode)">Close</button>
                            `;
                            document.body.appendChild(textModal);
                        }}
                    }})
                    .catch(error => {{
                        console.error("Error fetching extracted text:", error);
                        alert("Failed to extract text.");
                    }});
            }}
        </script>
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