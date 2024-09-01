from flask import Blueprint, current_app, jsonify

from app.auth.jwt_handler import get_user_from_token
from .models import Post


posts = Blueprint('posts', __name__)

@posts.route('/', methods=['GET'])
def get_posts():
    logger = current_app.logger

    user_id = get_user_from_token()
    if not user_id:
        return jsonify({"error": "Invalid or missing token"}), 401
    logger.debug(f"%s called /post", user_id)
    
    posts_list = [{"title": "Post 1"}, {"title": "Post 2"}]
    # posts = Post.query.all()
    # posts_list = [{"id": post.id, "title": post.title, "content": post.content, "user_id": post.user_id} for post in posts]
    return jsonify(posts_list)
