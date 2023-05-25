from flask import Blueprint, request, jsonify
from app.services.image_prompt_service import ImagePromptService

image_prompt_bp = Blueprint('image_prompt_bp', __name__)

image_prompt_service = ImagePromptService()

@image_prompt_bp.route('/api/image-prompt', methods=['POST'])
def image_prompt():
    data = request.get_json()
    print(data)
    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    image_context = data.get('image_context', '')
    try:
        response = image_prompt_service.generate_image_prompt(image_context)
        return jsonify({'image_prompt': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

