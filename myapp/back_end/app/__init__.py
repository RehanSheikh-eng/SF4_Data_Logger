from flask import Flask
from .routes.audio_upload_route import audio_upload_bp
from .routes.story_generation_route import story_bp
from .routes.image_prompt_route import image_prompt_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(audio_upload_bp)
    app.register_blueprint(story_bp)
    app.register_blueprint(image_prompt_bp)
    return app
