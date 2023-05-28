from flask import Blueprint, request, jsonify
from app.services.firebase_service import FirebaseService

get_stories_bp = Blueprint('get_stories_bp', __name__)
firebase_service = FirebaseService()

@get_stories_bp.route('/api/get-stories', methods=['GET'])
def get_stories():
    stories = firebase_service.get_all_from_collection('stories')
    return jsonify(stories), 200

@get_stories_bp.route('/api/get-stories/<story_id>', methods=['GET'])
def get_story(story_id):
    story = firebase_service.get_from_firestore('stories', story_id)
    if story is not None:
        return jsonify(story), 200
    else:
        return jsonify({"error": "Story not found"}), 404
