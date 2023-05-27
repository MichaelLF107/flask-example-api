from models import User
from database import db

def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        output.append({'id': user.id, 'name': user.name, 'age': user.age, 'email': user.email, 'admin': user.admin})
    return output

def get_user(id):
    user = User.query.filter_by(id=id).first()
    return {'id': user.id, 'name': user.name, 'age': user.age, 'email': user.email, 'admin': user.admin}

def create_user(data):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return {'message': 'user created'}
