from models import Post, User
from database import db

def get_all_posts():
    post = Post.query.all()
    output = []
    for post in post:
        user = User.query.filter_by(id=post.user_id).first()
        output.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'user': user.name,
            'email': user.email
        })
    return output

def get_post(id):
    post = Post.query.filter_by(id=id).first()
    user = User.query.filter_by(id=post.user_id).first()
    return {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'user': user.name,
        'email': user.email
    }

def create_post(data):
    post = Post(**data)
    db.session.add(post)
    db.session.commit()
    return {'message': 'post created'}
