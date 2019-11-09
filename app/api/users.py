from flask import jsonify, request, current_app, url_for
from . import api
from .. import db
from ..model import User, kPost

# @api.route('/users/<int:id>')
# def get_user(id):
#     user = User.query.get_or_404(id)
#     return jsonify(user.to_json())


@api.route('/register', methods=['POST'])
def new_user():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)    # missing arguments
    if User.query.filter_by(userName=username).first() is not None or User.query.filter_by(email=email).first() is not None:
        abort(400)    # existing user
    user = User(userName=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return (jsonify('success!'))

