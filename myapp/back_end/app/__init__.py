from flask import Flask
from .routes.transcribe_route import transcribe_blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.register_blueprint(transcribe_blueprint)

    return CORS(app)
