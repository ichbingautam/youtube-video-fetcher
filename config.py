class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://@localhost/video_store'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YOUTUBE_API_KEYS = ["YOUR_API_KEY_1", "YOUR_API_KEY_2"]
    SEARCH_QUERY = "cricket"
    FETCH_INTERVAL = 10  # in seconds
