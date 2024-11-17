from flask import Flask
from flask_cors import CORS
from routes.photos import photo_routes
from models.photo_model import initialize_sqlite

# Create Flask App
app = Flask(__name__)
CORS(app)

# Initialize SQLite database if configured
initialize_sqlite()

# Register Blueprints
app.register_blueprint(photo_routes)

@app.route("/")
def home():
    return "Welcome to the Gallery Management System API!"


if __name__ == "__main__":
    app.run(debug=True)
