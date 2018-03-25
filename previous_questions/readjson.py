import json
from collections import OrderedDict
			
class Solution(object):
	def __init__(self):
		self.commands = []
		self.db = []
		self.parse_input()

	def parse_input(self):
		"""parse the input from stdin for commands"""
		for line in iter(raw_input, ''):
			split_line = line.split(' ')
			json = ' '.join(split_line[1:])	
			command = (split_line[0], json)
			self.commands.append(command)

	def add_db(self, data):
		"""store json as dictionaries into db"""
		json_object = json.loads(data, object_pairs_hook=OrderedDict)
		self.db.append(json_object)

	def in_dict(self, query, dic):
		"""search through dict, for query"""
		found = True
		for q in query.keys():
			if isinstance(query[q], list):
				for num in query[q]:
					found = found and num in dic[q]
			elif isinstance(query[q], dict):
				found = found and indict(query[q], dic[q])
			else:
				found = found and str(query[q]) == str(dic[q])

		return found


	def get_db(self, query):
		"""parse query, search db, print result"""
		ans = []
		if query is None or len(self.db) == 0:
			return 
		query = json.loads(query)
		for data in self.db:
			if in_dict(query, data):
				ans.append(json.dumps(data, separators=(',', ':')))
		for a in ans:
			print a



	def delete_db(self, data):
		"""parse fields of input and delete db data"""
		found = True 
		delete = []
		query = json.loads(data)
		for data in self.db:
			if indict(query, data):
				delete.append(data)
		for d in delete:
			self.db.remove(d)

	def run(self):
		"""call appropriate get and add functions"""
		for command in self.commands:
			if command[0] == 'add':
				self.add_db(command[1])
			elif command[0] == 'get':
				self.get_db(command[1])
			elif command[0] == 'delete':
				self.delete_db(command[1])

	def print_db(self):
		for data in self.db:
			print "data: " + str(data) + '\n'

def flattenDictionary(d):
	"""flatten a layered dictionary"""
	res = {} 
	for k in d.keys():
		if isinstance(d[k], dict):
			res.update(flattenDictionary(d[k]))
		else:
			res.update({k:d[k]})
	return res


def indict(query, dic):
	found = True
	for q in query.keys():
		if isinstance(query[q], list):
			for num in query[q]:
				found = found and num in dic[q]
		elif isinstance(query[q], dict):
			found = found and indict(query[q], dic[q])
		else:
			found = found and str(query[q]) == str(dic[q])

	return found

if __name__ == "__main__":
	sol = Solution()
	sol.run()

	# d1 = {"id":3,"last":"Black","first":"Jim","location":{"city":"Spokane","state":"WA","postalCode":"99207"}}
	# q1 = {"location":{"state":"WA"}}
	# d2 = {"type":"list","list":[4,5,6,7]}
	# q2 = {"type":"list","list":[3,4]}
	# print indict(q1, d1)
	# print indict(q2, d2)




