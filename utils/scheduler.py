from apscheduler.schedulers.background import BackgroundScheduler
from services.youtube_service import YouTubeService
from config import Config

# Initialize scheduler
scheduler = BackgroundScheduler()

# Add job to the scheduler
scheduler.add_job(YouTubeService().fetch_latest_videos, 'interval', seconds=Config.FETCH_INTERVAL)

