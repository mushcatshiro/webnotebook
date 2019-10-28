# define model
# csv query
# define output
import pandas as pd
import json

class kPost(object):
	"""docstring for kPost"""
	def __init__(self):
		self.ret_val = None

	def create_row(self, input_):
		# missing postId and userId solution
		# required to test out resource
		data = json.dumps(input_)
		df = pd.read_json(data)
		df.to_csv("storage.csv", mode="a", index=False, header=False)
		return "complete"

	def read_row(self, title):
		df = pd.read_csv("storage.csv")
		# search by title return list of row numbers
		row_list = df.index[df["title"].str.contains(title) == True].tolist()
		self.ret_val = []
		for row_num in row_list:
			my_dict ={key:value for key, value in zip(df.columns.to_list(), df.loc[row_num, :])}
			self.ret_val.append(my_dict)
		return self.ret_val

	def update_row(self, input_):
		postId = input_[0]['postId']
		data = json.dumps(input_)
		df = pd.read_json(data)
		storageDf = pd.read_csv('storage.csv')
		targetIndex = storageDf[storageDf['postId'] == int(postId)].index
		storageDf.drop(targetIndex, inplace=True)
		storageDf = storageDf.append(df)
		storageDf.reset_index()
		storageDf.to_csv("storage.csv", index=False)
		return 'complete'

	def delete_row(self, title):
		df = pd.read_csv('storage.csv')
		targetIndex = df[df['title'] == title].index
		df.drop(targetIndex, inplace=True)
		df.to_csv("storage.csv", index=False)
		return 'complete'

def test_kPost(**kwargs):
	new = kPost()
	# result = new.create_row(input_=input_)
	# result = new.read_row('electron')
	# result = new.update_row(input_)
	# result = new.delete_row('electron')

	# print(result)

class userPost(kPost):
	"""docstring for UserPost"""
	def __init__(self):
		super(kPost, self).__init__()
		self.arg = None

	def display_userPost(self):
		result = kPost.read_row(self, title = 'electron')
		return result

def test_userPost():
	new = userPost()
	result = new.display_userPost()
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
"""

input_ = [{"postId": "3", "userId": "2", "title": "neutron", "content": "The neutron is a subatomic particle, symbol n or n0, with no net electric charge and a mass slightly greater than that of a proton", "relatedId": "1,2,3", "resource": "[]"}]

# test_kPost(input_= input_)
test_userPost()