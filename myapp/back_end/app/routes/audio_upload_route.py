import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest
from app.services.transcription_service import TranscriptionService
from app.services.firebase_service import FirebaseService
from app.services.story_generation_service import StoryGeneratorService
#from your_text_to_speech_module import TextToSpeechService
#text_to_speech_service = TextToSpeechService()

story_generation_service = StoryGeneratorService()
transcription_service = TranscriptionService()
firebase_service = FirebaseService()

audio_upload_bp = Blueprint('audio_upload', __name__)

@audio_upload_bp.route('/api/audio-upload', methods=['POST'])
def audio_upload():
    if 'file' not in request.files:
        raise BadRequest("File not present in request")
    file = request.files['file']
    if file.filename == '':
        raise BadRequest("File name is not present in request")
    if not file:
        raise BadRequest("File is not present in request")

    filename = secure_filename(file.filename)
    file.save(filename)

    # Transcribe the audio to text
    transcription_response = transcription_service.transcribe(filename, preprocess_audio=False)
    print(transcription_response)

    # Generate a story from the transcription
    story_response = story_generation_service.generate_story(transcription_response)

    # Convert the story text to speech
    #tts_response = text_to_speech_service.generate_speech(story_response)

    # Save the transcript and story to Firestore
    firebase_service.save_to_firestore('stories', filename, {
        "transcription": transcription_response,
        "story": story_response,
    })


    # Save the tts_response to Firebase Storage
    #firebase_service.upload_to_storage(f"{filename}_tts.wav", tts_response)

    # Delete the local file once it's been uploaded to Firebase Storage
    os.remove(filename)

    # Return the generated story and text-to-speech responses
    # return jsonify({
    #     "transcription": transcription_response,
    #     "story": story_response,
    #     "tts": f"{filename}_tts.wav"
    # })
    return jsonify({
        "transcription": transcription_response,
        "story": story_response,
    })
