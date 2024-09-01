import configparser
import os
import logging
from logging.handlers import RotatingFileHandler



class Config:
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), '..', 'config.ini'))

    SECRET_KEY = config.get('flask', 'secret_key')
    DEBUG = config.getboolean('flask', 'debug')
    PORT = config.getint('flask', 'port', fallback=5000)
    SQLALCHEMY_DATABASE_URI = config.get('database', 'sqlalchemy_database_uri')
    SQLALCHEMY_TRACK_MODIFICATIONS = config.getboolean('database', 'sqlalchemy_track_modifications')
    LOG_LEVEL_STR = config.get('logging', 'level', fallback='INFO')

    @staticmethod
    def setup_logger():
        log_level = getattr(logging, Config.LOG_LEVEL_STR.upper(), logging.INFO)
        
        # 로거 인스턴스 생성
        logger = logging.getLogger('my_flask_app')
        logger.setLevel(log_level)  # 로깅 레벨 설정

        # 콘솔 핸들러 설정
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # 파일 핸들러 설정 (로그 파일에 기록)
        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10000, backupCount=3)
        file_handler.setLevel(log_level)

        # 로그 형식 지정
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # 로거에 핸들러 추가
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        return logger
