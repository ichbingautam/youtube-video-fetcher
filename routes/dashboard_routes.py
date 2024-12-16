from flask import Blueprint, render_template, request
from models.video import Video
from sqlalchemy import or_

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
def view_dashboard():
    # Filters and sorting
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', 'publish_date_time')
    sort_order = request.args.get('order', 'desc')

    query = Video.query
    if search_query:
        query = query.filter(or_(
            Video.title.ilike(f"%{search_query}%"),
            Video.description.ilike(f"%{search_query}%")
        ))

    if sort_order == 'desc':
        query = query.order_by(getattr(Video, sort_by).desc())
    else:
        query = query.order_by(getattr(Video, sort_by).asc())

    # Pagination
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    videos = query.paginate(page=page, per_page=page_size, error_out=False)

    return render_template('dashboard.html', videos=videos, search_query=search_query, sort_by=sort_by, sort_order=sort_order)
