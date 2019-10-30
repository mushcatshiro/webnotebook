from flask import jsonify, request, current_app, url_for
from . import api
from ..model import kPost, user

@api.route('/userId/<int:userId>')
def get_userPost(userId):
    user_ = user() 
    userPost = user_.display_userPost(userId=userId)
    return jsonify(userPost)