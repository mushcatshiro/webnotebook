# # define model
# csv query
# define output
import pandas as pd
import json
import os


class kPost:
	"""docstring for kPost"""

	def create_row(self, input_):
		# missing postId and userId solution
		# required to test out resource
		data = json.dumps(input_)
		df = pd.read_json(data)
		df.to_csv("../storage.csv", mode="a", index=False, header=False)
		return "complete"

	def read_row(self, title):
		df = pd.read_csv("../storage.csv")
		# search by title return list of row numbers
		rowList = df.index[df["title"].str.contains(title) == True].tolist()
		returnValue = []
		for row_num in rowList:
			my_dict ={key:value for key, value in zip(df.columns.to_list(), df.loc[row_num, :])}
			returnValue.append(my_dict)
		return returnValue

	def update_row(self, input_):
		postId = input_[0]['postId']
		data = json.dumps(input_)
		df = pd.read_json(data)
		storageDf = pd.read_csv('../storage.csv')
		targetIndex = storageDf[storageDf['postId'] == int(postId)].index
		storageDf.drop(targetIndex, inplace=True)
		storageDf = storageDf.append(df)
		storageDf.reset_index()
		storageDf.to_csv("../storage.csv", index=False)
		return 'complete'

	def delete_row(self, title):
		df = pd.read_csv('../storage.csv')
		targetIndex = df[df['title'] == title].index
		df.drop(targetIndex, inplace=True)
		df.to_csv("../storage.csv", index=False)
		return 'complete'

def test_kPost(**kwargs):
	new = kPost()
	# result = new.create_row(input_=input_)
	# result = new.read_row('electron')
	# result = new.update_row(input_)
	# result = new.delete_row('electron')

	# print(result)

class user:
	"""docstring for UserPost"""
	def __init__(self):
		pass

	def display_userPost(self, userId):
		df = pd.read_csv("/home/mushcat/webnotebook/storage.csv", dtype=str)
		# search by title return list of row numbers
		rowList = df.index[df["userId"] == str(userId)].tolist()
		returnValue = []
		for row_num in rowList:
			my_dict ={key:value for key, value in zip(df.columns.to_list(), df.loc[row_num, :])}
			returnValue.append(my_dict)
		return returnValue

def test_user():
	new = user()
	result = new.display_userPost(1)
	print(result)

		
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
test_user()
# print(os.getcwd())