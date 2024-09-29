from flask import Blueprint
from flask_restx import Api, Resource, fields
from .services import get_user_list, get_user_by_id, add_user

# Blueprint 생성
user_blueprint = Blueprint('user', __name__)

# Blueprint에 Flask-RESTx API 바인딩
api = Api(user_blueprint, version="1.0", title="User API", description="User related operations")

# 모델 정의
user_model = api.model('User', {
    'id': fields.Integer(readonly=True, description="The user's unique identifier"),
    'name': fields.String(required=True, description="The user's name"),
})

# User 리소스 클래스
@api.route('/users')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """사용자 목록 조회"""
        return get_user_list()  # 비즈니스 로직 호출

    @api.expect(user_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """새로운 사용자 추가"""
        new_user = api.payload
        return add_user(new_user), 201  # 비즈니스 로직 호출

# 단일 사용자 조회
@api.route('/users/<int:id>')
class User(Resource):
    @api.marshal_with(user_model)
    def get(self, id):
        """사용자 ID로 사용자 조회"""
        user = get_user_by_id(id)  # 비즈니스 로직 호출
        if user is not None:
            return user
        api.abort(404, "User not found")
