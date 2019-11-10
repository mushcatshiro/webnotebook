# # define model
# csv query
# define output
import pandas as pd
import json
import random
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
# import os

# Please change the csv file path in below variable
# csv_name = "/Users/tangpayne/Documents/WebApplication/MAMP/projects/webnotebook/storage.csv" #Payne
csv_name = "/home/mushcat/webnotebook/storage.csv" # Mushcat

def postSearching(rowList = None, dfLen = None, df = None):
    if rowList is None:
        rowList = range(dfLen)
    returnValue = []
    for row_num in rowList:
        my_dict ={key:value for key, value in zip(df.columns.to_list(), df.loc[row_num, :])}
        returnValue.append(my_dict)
    return returnValue

class kPost:
    """docstring for kPost"""

    def createRow(self, input_):
        # missing postId and userId solution
        # required to test out resource
        data = json.dumps(input_)
        df = pd.read_json(data)
        df.to_csv(csv_name, mode="a", index=False, header=False)
        return "complete"

    def readRow(self, title=None, total=None):
        df = pd.read_csv(csv_name, dtype=str)
        # search by title return list of row numbers
        if title is not None:
            rowList = df.index[df["title"] == str(title)].tolist()
            return postSearching(rowList=rowList, df = df)
        elif total is not None:
            dfLen = len(df)
            if dfLen < total:
                return postSearching(dfLen = dfLen, df = df)
            returnPostList = random.choices(range(dfLen), k = total)
            return postSearching(rowList = returnPostList, df = df)
        else:
            return "error"

    def updateRow(self, input_):
        postId = input_[0]['postId']
        data = json.dumps(input_)
        df = pd.read_json(data)
        storageDf = pd.read_csv(csv_name)
        targetIndex = storageDf[storageDf['postId'] == int(postId)].index
        storageDf.drop(targetIndex, inplace=True)
        storageDf = storageDf.append(df)
        storageDf.reset_index()
        storageDf.to_csv(csv_name, index=False)
        return 'complete'

    def deleteRow(self, title):
        df = pd.read_csv(csv_name)
        targetIndex = df[df['title'] == title].index
        df.drop(targetIndex, inplace=True)
        df.to_csv(csv_name, index=False)
        return 'complete'

    def display_userPost(self, userId):
        df = pd.read_csv(csv_name, dtype=str)
        # search by title return list of row numbers
        rowList = df.index[df["userId"] == str(userId)].tolist()
        returnValue = []
        return postSearching(rowList = rowList, df = df)

    def to_json(self):
        json_post = {
            'url': url_for('api.get_post', id=self.id),
            'title' : title,
            'content': content,
            'relatedId' : relatedId,
            'resource' : resource,
            'author_url': url_for('api.get_user', id=self.author_id)
        }
        return json_post

class Permission:
    """docstring for Permission"""
    READ = 0
    WRITE = 4
    ADMIN = 8

class Role(db.Model):
    """docstring for Role"""
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic') # 'user' refers to the class name, backref is the psuedo column name use to link user to role

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    @staticmethod
    def insert_roles():
        roles = {'validatedUser': [Permission.READ, Permission.WRITE], 'Administrator': [Permission.READ, Permission.WRITE, Permission.ADMIN], }
        
        default_role = 'validatedUser'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    def __repr__(self):
        return '<Role %r>' % self.name
        


class User(UserMixin, db.Model):
    """docstring for User"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    userName = db.Column(db.String(8), unique = True, index = True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 'roles' refers to the table name

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role_id is None:
            if self.role_id is None:
                self.role_id = Role.query.filter_by(default=True).first()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = User.query.get(data.get('reset'))
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
        return True

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)


    def to_json(self):
        json_user = {
            'url': url_for('api.get_user', id=self.id),
            'username': self.userName,
            'member_since': self.member_since,
            'last_seen': self.last_seen,
            'posts_url': url_for('api.get_user_posts', id=self.id),
            'followed_posts_url': url_for('api.get_user_followed_posts', id=self.id),
            'post_count': self.posts.count()
        }
        return json_user

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def __repr__(self):
        return '<User %r>' % self.userName

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return False

def test_kPost(**kwargs):
    # new = kPost()
    # result = new.create_row(input_=input_)
    # result = new.read_row('electron')
    # result = new.update_row(input_)
    # result = new.delete_row('electron')

    new = user()
    result = new.display_userPost(1)

    # print(result)

