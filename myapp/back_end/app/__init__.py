from flask import Flask
from .routes.transcribe_route import transcribe_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(transcribe_blueprint)

    return app
