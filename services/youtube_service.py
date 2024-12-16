from datetime import datetime, timedelta
from repositories.video_repository import VideoRepository
from config import Config
import requests
from flask import current_app
from extensions import db
from flask import Flask
from models.video import Video

class YouTubeService:
    def __init__(self):
        self.current_api_key_index = 0
        self.last_fetch_time = datetime.utcnow() - timedelta(hours=1)

    def get_current_api_key(self):
        return Config.YOUTUBE_API_KEYS[self.current_api_key_index]

    def rotate_api_key(self):
        self.current_api_key_index = (self.current_api_key_index + 1) % len(Config.YOUTUBE_API_KEYS)

    def fetch_latest_videos(self):
        app = Flask(__name__)
        app.config.from_object(Config)
        db.init_app(app)
        with app.app_context():
            db.create_all()
            url = "https://www.googleapis.com/youtube/v3/search"
            params = {
                "part": "snippet",
                "q": Config.SEARCH_QUERY,
                "type": "video",
                "order": "date",
                "publishedAfter": self.last_fetch_time.isoformat("T") + "Z",
                "key": self.get_current_api_key()
            }

            try:
                response = requests.get(url, params=params)
                if response.status_code == 403:
                    self.rotate_api_key()
                    return

                data = response.json()
                items = data.get("items", [])
                print(f"{Config.SEARCH_QUERY} - {len(items)}")
                for item in items:
                    snippet = item["snippet"]
                    video_id = item["id"]["videoId"]

                    if not VideoRepository.video_exists(video_id):
                        video = Video(
                            video_id=video_id,
                            title=snippet["title"],
                            description=snippet.get("description"),
                            publish_date_time=datetime.strptime(snippet["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"),
                            thumbnails=snippet["thumbnails"]["default"]["url"]
                        )
                        db.session.add(video)

                db.session.commit()
                self.last_fetch_time = datetime.utcnow()

            except Exception as e:
                print(f"Error fetching videos: {e}")
