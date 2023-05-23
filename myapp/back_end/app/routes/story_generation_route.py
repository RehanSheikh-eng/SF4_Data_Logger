from flask import Blueprint, request, jsonify
from app.services.story_generation_service import StoryGeneratorService

story_bp = Blueprint('story_bp', __name__)

story_generator = StoryGeneratorService()

@story_bp.route('/api/story', methods=['POST'])
def story():
    data = request.get_json()
    print(data)
    if data is None:
        return jsonify({'error': 'No data provided'}), 400

    story_context = data.get('story_context', '')
    print(story_context)
    try:
        response = story_generator.generate_story(story_context)
        return jsonify({'story_text': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

