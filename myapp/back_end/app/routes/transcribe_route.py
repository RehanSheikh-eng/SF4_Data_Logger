from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from app.services.transcription_service import TranscriptionService

transcribe_blueprint = Blueprint('transcribe', __name__)

@transcribe_blueprint.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        raise BadRequest("File not present in request")
    file = request.files['file']
    if file.filename == '':
        raise BadRequest("File name is not present in request")
    if not file:
        raise BadRequest("File is not present in request")
    file.save(file.filename)

    firebase_url = upload_file(filename)

    response = transcription_service.transcribe(filename, preprocess_audio=False)
    response['firebase_url'] = firebase_url
    service = TranscriptionService()
    response = service.transcribe(file.filename)
    return response
