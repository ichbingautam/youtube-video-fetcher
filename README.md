# YouTube Video Fetcher API

This project provides a scalable API for fetching and searching YouTube videos based on a predefined search query. Videos are fetched continuously in the background using the YouTube Data API v3 and stored in a database. The API offers endpoints to retrieve stored videos and perform optimized searches.

## Features

- **Fetch Latest Videos**: Continuously fetch the latest videos from YouTube for a predefined search query.
- **Pagination**: Get video data in paginated responses.
- **Search API**: Search videos by title or description with support for partial matches.
- **Multiple API Keys**: Automatically rotate between API keys when quota is exhausted.
- **Optimized Search**: Uses PostgreSQL full-text search for fast and efficient queries.
- **Dockerized**: Ready to run in a containerized environment.
- **Scalable**: Designed to handle high-frequency updates and searches.

## Dashboard
 <img width="1728" alt="Screenshot 2024-12-16 at 4 39 45 PM" src="https://github.com/user-attachments/assets/7f09f4aa-f0a2-4df9-854f-e023e2363bb4" />


## Project Structure

```
project_root/
|-- app.py                 # Application entry point
|-- config.py              # Configuration settings
|-- models/
|   |-- video.py           # Database models
|-- repositories/
|   |-- video_repository.py    # API handlers
|-- routes/
|   |-- dashboard_routes.py    # Dashboard route handlers
|   |-- video_routes.py        # API route handlers
|-- services/
|   |-- youtube_service.py # YouTube API integration
|-- templates/
|   |-- base.html            # Initial HTML page
|   |-- dashboard.html       # Dashboard page with table view for videos
|-- utils/
|   |-- scheduler.py       # Background job scheduler
|-- Dockerfile             # Docker configuration
|-- requirements.txt       # Python dependencies
|-- README.md              # Project documentation
```

## Endpoints

### 1. Get Videos

**GET** `/api/videos`

Retrieve stored videos in reverse chronological order.

#### Query Parameters
- `page` (int): Page number (default: 1)
- `page_size` (int): Number of videos per page (default: 10)

#### Response
```json
[
  {
    "id": "VIDEO_ID",
    "title": "Video Title",
    "description": "Video Description",
    "publish_date_time": "2024-12-16T10:00:00Z",
    "thumbnails": "THUMBNAIL_URL"
  }
]
```

### 2. Search Videos

**GET** `/api/videos/search`

Search stored videos by title or description.

#### Query Parameters
- `query` (string): Search term
- `page` (int): Page number (default: 1)
- `page_size` (int): Number of videos per page (default: 10)

#### Response
Same as the `Get Videos` response format.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Docker (optional for containerized setup)
- PostgreSQL (recommended for production)

### Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ichbingautam/youtube-video-fetcher.git
   cd youtube-video-fetcher
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Database**:
   ```bash
   flask db upgrade
   ```

4. **Run the Application**:
   ```bash
   python3 app.py
   ```

5. **Access the API**:
   Open [http://localhost:5011](http://localhost:5011) in your browser or API client.

### Dockerized Setup

1. **Build Docker Image**:
   ```bash
   docker build -t youtube-api-fetcher .
   ```

2. **Run Docker Container**:
   ```bash
   docker run -p 5011:5011 youtube-api-fetcher
   ```

3. **Access the API**:
   Open [http://localhost:5011](http://localhost:5011) in your browser or API client.

## Configuration

Update the `config.py` file to customize settings:
- `SQLALCHEMY_DATABASE_URI`: Database connection string
- `YOUTUBE_API_KEYS`: List of YouTube Data API keys
- `SEARCH_QUERY`: Search term for fetching videos
- `FETCH_INTERVAL`: Interval (in seconds) between fetch operations

## Bonus Features

- **Multiple API Keys**: Automatically switches between available API keys when quota is exhausted.
- **Optimized Search**: Supports partial matches using PostgreSQL full-text search.
- **Scalability**: Designed to handle high-frequency updates and concurrent queries.

## Dependencies

- Flask
- Flask-SQLAlchemy
- APScheduler
- Requests
- psycopg2-binary (for PostgreSQL)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
