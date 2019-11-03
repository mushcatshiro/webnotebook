# # define model
# csv query
# define output
import pandas as pd
import json
import random
# from . import db
from werkzeug.security import generate_password_hash, check_password_hash
# import os

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
		df.to_csv("/home/mushcat/webnotebook/storage.csv", mode="a", index=False, header=False)
		return "complete"

	def readRow(self, title=None, total=None):
		df = pd.read_csv("/home/mushcat/webnotebook/storage.csv", dtype=str)
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
		storageDf = pd.read_csv('/home/mushcat/webnotebook/storage.csv')
		targetIndex = storageDf[storageDf['postId'] == int(postId)].index
		storageDf.drop(targetIndex, inplace=True)
		storageDf = storageDf.append(df)
		storageDf.reset_index()
		storageDf.to_csv("/home/mushcat/webnotebook/storage.csv", index=False)
		return 'complete'

	def deleteRow(self, title):
		df = pd.read_csv('/home/mushcat/webnotebook/storage.csv')
		targetIndex = df[df['title'] == title].index
		df.drop(targetIndex, inplace=True)
		df.to_csv("/home/mushcat/webnotebook/storage.csv", index=False)
		return 'complete'

	def display_userPost(self, userId):
		df = pd.read_csv("/home/mushcat/webnotebook/storage.csv", dtype=str)
		# search by title return list of row numbers
		rowList = df.index[df["userId"] == str(userId)].tolist()
		returnValue = []
		return postSearching(rowList = rowList, df = df)

# class user(db.Model):
# 	"""docstring for user"""
# 	userId = db.Column(db.Integer, primary_key = True)
# 	userName = db.Column(db.String(8), unique = True, index = True)
# 	email = db.Column(db.String(64), unique=True, index=True)
# 	password_hash = db.Column(db.String(128))

# 	@property
# 	def password(self):
# 		raise AttributeError('password is not a readable attribute')

# 	@password.setter
# 	def password(self, password):
# 		self.password_hash = generate_password_hash(password)

# 	def verify_password(self, password):
# 		return check_password_hash(self.password_hash, password)

# 	@staticmethod
# 	def reset_password(token, new_password):
# 		s = Serializer(current_app.config['SECRET_KEY'])
# 		try:
# 			data = s.loads(token.encode('utf-8'))
# 		except:
# 			return False
# 		user = User.query.get(data.get('reset'))
# 		if user is None:
# 			return False
# 		user.password = new_password
# 		db.session.add(user)
# 		return True

def test_kPost(**kwargs):
	# new = kPost()
	# result = new.create_row(input_=input_)
	# result = new.read_row('electron')
	# result = new.update_row(input_)
	# result = new.delete_row('electron')

	new = user()
	result = new.display_userPost(1)

	# print(result)

		
"""
{
	"postId": 1
	"userId": 1
	"title": "proton"
	"content": "The electron is a subatomic particle, symbol e− or β−, whose electric charge is negative one elementary charge"
	"relatedId": [1]
	"resource": [{}]
	# to be designed
}


input_ = [{"postId": "3", "userId": "2", "title": "neutron", "content": "The neutron is a subatomic particle, symbol n or n0, with no net electric charge and a mass slightly greater than that of a proton", "relatedId": "1,2,3", "resource": "[]"}]
"""

# test_kPost(input_= input_)
# test_user()
# print(os.getcwd())