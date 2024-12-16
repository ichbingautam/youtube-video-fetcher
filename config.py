class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://@localhost/video_store'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YOUTUBE_API_KEYS = ["AIzaSyBbREvAFn2YUvw_jaSWTfwppG1fDBGnJpA", "AIzaSyDA_9GoT7awMwQEbt5J-rGYdmkxZ_jEAmk"]
    SEARCH_QUERY = "Javascript"
    FETCH_INTERVAL = 10  # in seconds
