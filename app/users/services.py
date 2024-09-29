# 사용자 목록을 처리하는 비즈니스 로직을 이곳에 정의합니다.

users = []

def get_user_list():
    """모든 사용자 목록을 반환"""
    return users

def get_user_by_id(user_id):
    """사용자 ID로 사용자 검색"""
    return next((user for user in users if user['id'] == user_id), None)

def add_user(new_user_data):
    """새로운 사용자 추가"""
    new_user_data['id'] = len(users) + 1
    users.append(new_user_data)
    return new_user_data
