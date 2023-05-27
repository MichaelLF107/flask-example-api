from flask import Flask, request
from database import db
from user import get_all_users, get_user, create_user
from post import get_all_posts, get_post, create_post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:docker@localhost/postgres'

@app.route('/user/<id>', methods=['GET'])
def user_get(id):
    return get_user(id)

@app.route('/user', methods=['POST'])
def user_post():
    return create_user(request.json)

@app.route('/users', methods=['GET'])
def all_users():
    return get_all_users()

@app.route('/post/<id>', methods=['GET'])
def posts_get(id):
    return get_post(id)

@app.route('/post', methods=['POST'])
def posts_post():
    return create_post(request.json)

@app.route('/posts', methods=['GET'])
def all_posts():
    return get_all_posts()

if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)
        db.create_all()
        app.run(debug=True)