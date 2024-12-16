from flask import Flask
from extensions import db
from routes.video_routes import video_bp
from utils.scheduler import scheduler
from config import Config
from routes.dashboard_routes import dashboard_bp


# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(dashboard_bp)


def create_app():
    app.register_blueprint(video_bp)
    scheduler.start()
    with app.app_context():
        db.create_all()
    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5011, debug=True)