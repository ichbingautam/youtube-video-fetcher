from models.video import Video

class VideoRepository:
    @staticmethod
    def get_all_videos(page, page_size, order_by='publish_date_time', order='desc'):
        query = Video.query
        if order == 'desc':
            query = query.order_by(getattr(Video, order_by).desc())
        else:
            query = query.order_by(getattr(Video, order_by).asc())
        return query.paginate(page, page_size, False).items

    @staticmethod
    def search_videos(query, page, page_size):
        return Video.query.filter(
            func.to_tsvector('english', Video.title + ' ' + (Video.description or '')).op('@@')(
                func.plainto_tsquery('english', query)
            )
        ).order_by(Video.publish_date_time.desc()).paginate(page, page_size, False).items

    @staticmethod
    def insert_video(video_data):
        video = Video(**video_data)
        db.session.add(video)
        db.session.commit()

    @staticmethod
    def video_exists(video_id):
        return Video.query.filter_by(video_id=video_id).first() is not None
