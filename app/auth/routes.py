from flask import Blueprint, jsonify, request

from app.auth.jwt_handler import create_token

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not 'username' in data or not 'password' in data:
        return jsonify({"error": "Invalid input"}), 400

    username = data['username']
    password = data['password']

    if username == 'admin' and password == 'secret':
        return jsonify({"message": f"Welcome, {username}!"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@auth.route('/token/<user_id>', methods=['GET'])
def generate_user_token(user_id):
    token = create_token(user_id)
    return jsonify({"token": token})
