from flask import Flask
from .routes.audio_upload_route import audio_upload_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(audio_upload_bp)

    return app
