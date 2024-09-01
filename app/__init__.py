from flask import Flask

from .config import Config
from .extensions import db
from .auth.routes import auth as auth_blueprint
from .posts.routes import posts as posts_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    logger = Config.setup_logger()
    logger.info("start flask app~~~~~~~~~~~~~~")
    app.logger = logger

    # 확장 초기화
    db.init_app(app)

    # 블루프린트 등록
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(posts_blueprint, url_prefix='/posts')

    return app
