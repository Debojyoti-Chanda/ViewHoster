from app import create_app
from app.routes import routes

from app.scheduler import start_scheduler

app = create_app()

# Register routes
app.register_blueprint(routes)

if __name__ == "__main__":
    # Start scheduler in a separate thread
    start_scheduler()

    # Start Flask server
    print("Starting server...")
    app.run(host="0.0.0.0", port=8000)
