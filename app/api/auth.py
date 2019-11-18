from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from ..model import User
from . import api
from .errors import unauthorized, forbidden

auth = HTTPBasicAuth()


# @auth.verify_password
# def verify_password(userName_or_token, password):
#     if userName_or_token == '':
#         return False
#     if password == '':
#         g.current_user = User.verify_auth_token(userName_or_token)
#         g.token_used = True
#         return g.current_user is not None
#     user = User.query.filter_by(userName=userName_or_token.lower()).first()
#     if not user:
#         return False
#     g.current_user = user
#     g.token_used = False
#     return user.verify_password(password)

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(userName=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')

# @api.before_request
# @auth.login_required
# def before_request():
#     if not g.user.is_anonymous:# and not g.current_user.confirmed:
#         return forbidden('Unconfirmed account')

@api.route('/tokens/', methods=['POST', 'GET'])
@auth.login_required
def get_token():
    # if g.token_used: # g.current_user.is_anonymous or 
    #     return unauthorized('Invalid credentials')
    return jsonify({'token': g.user.generate_auth_token(expiration=3600), 'expiration': 3600})
