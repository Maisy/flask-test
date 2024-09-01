from flask import request
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "your_secret_key"  # 토큰 서명을 위한 비밀 키

def create_token(user_id):
    """사용자 ID로 JWT 토큰을 생성"""
    payload = {
        'user_id': user_id,
        'exp': datetime.now(tz=timezone.utc) + timedelta(hours=1)  # 토큰 유효 기간 설정 (예: 1시간)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_token(token):
    """토큰에서 사용자 정보를 추출"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None  # 토큰이 만료된 경우
    except jwt.InvalidTokenError:
        return None  # 토큰이 유효하지 않은 경우

def get_user_from_token():
    """요청 헤더에서 JWT 토큰을 추출하고, 사용자 정보를 반환"""
    auth_header = request.headers.get('Authorization')
    if auth_header:
        try:
            # "Bearer <token>" 형식으로 토큰이 전달됨
            token = auth_header.split(" ")[1]
        except IndexError:
            return None
        user_id = decode_token(token)
        return user_id
    return None