from extensions import db
from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.sql import func

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    publish_date_time = db.Column(db.DateTime, nullable=False)
    thumbnails = db.Column(db.Text, nullable=True)
    search_vector = db.Column(TSVECTOR, nullable=True)

    __table_args__ = (
        db.Index('ix_video_search_vector', 'search_vector', postgresql_using='gin'),
    )

@db.event.listens_for(Video, 'before_insert')
def update_search_vector(mapper, connection, target):
    target.search_vector = func.to_tsvector('english', target.title + ' ' + (target.description or ''))

@db.event.listens_for(Video, 'before_update')
def update_search_vector_on_update(mapper, connection, target):
    target.search_vector = func.to_tsvector('english', target.title + ' ' + (target.description or ''))