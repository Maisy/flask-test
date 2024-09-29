from flask import Flask

from app.mq_worker.worker import start_workers

from .config import Config
from .extensions import db
from .auth.routes import auth as auth_blueprint
from .posts.routes import posts as posts_blueprint
from .users.routes import user_blueprint
from .messages.routes import messages as messages_blueprint



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    log = Config.setup_logger()
    log.info("start flask app~~~~~~~~~~~~~~")
    app.logger = log

    # 확장 초기화
    db.init_app(app)

    # 블루프린트 등록
    app.register_blueprint(user_blueprint, url_prefix="/api")
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(posts_blueprint, url_prefix='/posts')
    app.register_blueprint(messages_blueprint, url_prefix='/messages')

    start_workers()


    return app
