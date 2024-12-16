from flask import Blueprint, request, jsonify
from models.video import Video
from sqlalchemy.sql import func

video_bp = Blueprint('videos', __name__)

@video_bp.route('/api/videos', methods=['GET'])
def get_videos():
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 100, type=int)
    videos = Video.query.order_by(Video.publish_date_time.desc()).paginate(page=page, per_page=page_size, error_out=False).items
    result = [{
        "id": video.video_id,
        "title": video.title,
        "description": video.description,
        "publish_date_time": video.publish_date_time,
        "thumbnails": video.thumbnails
    } for video in videos]

    return jsonify(result)

@video_bp.route('/api/videos/search', methods=['GET'])
def search_videos():
    query = request.args.get('query', '', type=str)
    page = request.args.get('page', 1, type=int)
    page_size = request.args.get('page_size', 10, type=int)
    pagination = Video.query.order_by(Video.publish_date_time.desc()).paginate(
        page=page, per_page=page_size, error_out=False
    )
    videos = pagination.items

    result = [{
        "id": video.video_id,
        "title": video.title,
        "description": video.description,
        "publish_date_time": video.publish_date_time,
        "thumbnails": video.thumbnails
    } for video in videos]

    return jsonify(result)