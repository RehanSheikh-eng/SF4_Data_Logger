import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest
import uuid
# Import Services
from app.services.firebase_service import FirebaseService
from app.services.image_generation_service import ImageGenerationService


image_generation_service = ImageGenerationService()
firebase_service = FirebaseService()

image_generation_bp = Blueprint('image-generation', __name__)

@image_generation_bp.route('/api/image-generation', methods=['POST'])
def image_generation():
    data = request.get_json()
    print(data)
    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    id = data.get('id', '')
    image_prompt = data.get('image_prompt', '')

    print(image_prompt)

    try:
        # Generate image from image prompt
        image_filename = image_generation_service.generate_image(image_prompt)


        # Upload the generated image to Firebase Storage
        with open(image_filename, "rb") as image_file:
            image_url = firebase_service.upload_to_storage(f"{id}.png", image_file)


        # Save the image URL to Firestore in the document with the given id in the 'stories' collection
        firebase_service.save_to_firestore(collection_name='stories', unique_id=id, data={'image': image_url})

        return jsonify({'image': image_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
