from flask import Blueprint, request, jsonify
from models.photo_model import get_all_photos, add_photo

photo_routes = Blueprint('photo_routes', __name__)

@photo_routes.route('/photos', methods=['GET'])
def list_photos():
    photos = get_all_photos()
    return jsonify(photos)

@photo_routes.route('/photos', methods=['POST'])
def upload_photo():
    data = request.json
    title = data.get('title')
    url = data.get('url')
    add_photo(title, url)
    return jsonify({'message': 'Photo uploaded successfully!'})
