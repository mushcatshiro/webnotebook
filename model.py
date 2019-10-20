# define model
# csv query
# define output
import pandas as pd

class node(object):
	"""docstring for node"""
	def __init__(self, keyword):
		self.keyword = keyword
		self.ret_val = None

	def get_row(self):
		df = pd.read_csv('stoarge.csv')
		# search by title return list of row numbers
		row_list = df.index[df['animal'].str.contains('ro') == True].tolist()
		self.ret_val = []
		for row_num in row_list:
			my_dict ={key:value for key, value in zip(df.columns.to_list(), df.[row_num, :])}
			self.ret_val.append(my_dict)



"""
{
	'id': 1
	# hidden from user for model visualization purpose
	'Title': 'proton'
	'description': 'The electron is a subatomic particle, symbol e− or β−, whose electric charge is negative one elementary charge'
	'related_id': [1]
	# self referencing, always to be ignored/ skip 0
}
"""