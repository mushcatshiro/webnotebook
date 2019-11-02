from flask import jsonify, request, current_app, url_for
from . import api
from ..model import kPost, user

@api.route('/post/<int:userId>', methods=['GET' ,'POST'])
def get_userPost(userId):
    user_ = user() 
    userPost = user_.display_userPost(userId=userId)
    return jsonify(userPost)

@api.route('/post/<title>', methods=['GET' ,'POST'])
def searchPost_bytitle(title):
    kPost_ = kPost() 
    returnPost = kPost_.readRow(title=title)
    return jsonify(returnPost)

@api.route('/posts/<int:num>', methods=['GET' ,'POST'])
@api.route('/posts/', methods=['GET' ,'POST'])
def searchPost(num = None):
    if num is None:
        num = 2
    kPost_ = kPost() 
    returnPost = kPost_.readRow(total=num)
    return jsonify(returnPost)

"""
@api.route('/createPost/', methods=['POST'])
def createPost():
    post = kPost.from_json(request.json)
    post.author = g.current_user
    # db.session.add(post)
    # db.session.commit()
    return jsonify(post.to_json()), 201, \
        {'Location': url_for('api.get_post', id=post.id)}
"""
