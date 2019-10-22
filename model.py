# define model
# csv query
# define output
import pandas as pd
import json

class node(object):
	"""docstring for node"""
	def __init__(self):
		self.ret_val = None

	def create_row(self, input_):
		data = json.dumps(input_)
		df = pd.read_json(data)
		df.to_csv("storage.csv", mode="a", index=False, header=False)
			# df = df.append(item)
		# df.to_csv(df, index = False)
		return "complete"

	def read_row(self, keyword):
		df = pd.read_csv("storage.csv")
		# search by title return list of row numbers
		row_list = df.index[df["title"].str.contains(keyword) == True].tolist()
		self.ret_val = []
		for row_num in row_list:
			my_dict ={key:value for key, value in zip(df.columns.to_list(), df.loc[row_num, :])}
			self.ret_val.append(my_dict)
		return self.ret_val

	def update_row(self, input_):
		pass

	def delete_row(self, input_):
		pass

def test(**kwargs):
	new = node()
	# display = new.read_row("electron")
	result = new.create_row(input_=input_)

	print(result)

"""
{
	"id": 1
	# basically index showed for model visualization purpose
	"title": "proton"
	"description": "The electron is a subatomic particle, symbol e− or β−, whose electric charge is negative one elementary charge"
	"related_id": [1]
	# self referencing, always to be ignored/ skip 0
}
"""

input_ = [{"title": "neutron", "description": "The neutron is a subatomic particle, symbol n or n0, with no net electric charge and a mass slightly greater than that of a proton", "related_id": "1,2,3"}]

test(input_=input_)
