import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest
import uuid
import librosa

from app.services.transcription_service import TranscriptionService
from app.services.firebase_service import FirebaseService
from app.services.story_generation_service import StoryGeneratorService
from app.services.image_prompt_service import ImagePromptService
from app.services.image_generation_service import ImageGenerationService
from app.services.audio_processing_service import AudioProcessingService


image_generation_service = ImageGenerationService()
image_prompt_service = ImagePromptService()
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

    # Generate a unique ID for the new story
    unique_id = str(uuid.uuid4())

    # Process the audio file
    processed_audio = audio_processing_service.process_audio(filename, method='fb')

    # Save the processed audio as a new file
    processed_filename = f"{unique_id}_processed.wav"
    librosa.output.write_wav(processed_filename, processed_audio, sr)

    # Transcribe the processed audio to text
    transcription_response = transcription_service.transcribe(processed_filename)
    print(f"Transcription Service Response: {transcription_response}")

    # Generate a story from the transcription
    story_response = story_generation_service.generate_story(transcription_response)
    print(f"Story Sercive Response {story_response}")

    # Generate an image prompt from the story response
    image_prompt = image_prompt_service.generate_image_prompt(story_response)
    print(f"Image Service Repsone: {image_prompt}")

    # Generate image from image prompt
    image_filename = image_generation_service.generate_image(transcription_response)

    # Upload the generated image to Firebase Storage
    with open(image_filename, "rb") as image_file:
        image_url = firebase_service.upload_to_storage(f"{unique_id}.png", image_file)

    # Save the transcript, story, and image URL to Firestore
    firebase_service.save_to_firestore(collection_name='stories', unique_id=unique_id, data={
        "id": unique_id,
        "transcription": transcription_response,
        "story": story_response,
        "image_prompt": image_prompt,
        "image": image_url,
    })

    # Delete the local image file once it's been uploaded to Firebase Storage
    os.remove(image_filename)

    # Delete the local audio files once it's been uploaded to Firebase Storage
    os.remove(filename)
    os.remove(processed_filename)

    return jsonify({
        "id": unique_id,
        "transcription": transcription_response,
        "story": story_response,
        "image_prompt": image_prompt,
        "image": image_url,
    })

