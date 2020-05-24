import os
import datetime
import pickle

class AmazeFileSearch:

	def __init__(self):
		"""
		Timer setup and runs the run, lol!
		"""
		start = datetime.datetime.now()
		self.run()
		end = datetime.datetime.now()
		print("The total execution time is ", (end-start).total_seconds()% 86400, "sec")

	def run(self):
		"""
		Our run function sets up the dictionary and
		this also handles input and output function,
		until you want them to be abstracted out!
		"""
		self.dict_setup()
		yo_input =self.input_handler()
		self.output_handler(yo_input)

	def dict_setup(self):
		"""
		This function handles dictionary itself.
		If dictionary exists then we use it else,
		we create a new one!(Time consuming brughh!)
		"""
		list_of_files = self.get_files_list()
		self.big_dictionary = self.get_dict()

		if not self.big_dictionary:
			self.big_dictionary=dict()
			self.initialize_dict(list_of_files)
			self.save_dict(self.big_dictionary)

	def get_files_list(self):
		"""
		Lets get out files in given folder
		"""
		list_of_files = os.listdir(os.getcwd()+"/dictionary")
		return list_of_files

	def get_dict(self):
		"""
		If dict exists return dict else return None
		"""
		if os.path.exists("data.pkl"):
			a_file = open("data.pkl", "rb")
			output = pickle.load(a_file)
			a_file.close()
			return output
		return None

	def save_dict(self, mydict):
		"""
		Saving the dict for saving time
		"""
		a_file = open("data.pkl", "wb")
		pickle.dump(mydict, a_file)
		a_file.close()

	def initialize_dict(self, list_of_files):
		"""
		Creating the dictionary for first time
		"""
		for file in list_of_files:
			with open(os.getcwd()+"/dictionary/"+str(file), "r+", encoding = 'utf-8') as read_file:
				file_name = os.path.basename(read_file.name)
				temp_set = set()
				list_of_lines = read_file.read().splitlines()
				for line in list_of_lines:
					temp_set.add(line)
				self.big_dictionary[file_name] = temp_set

	def input_handler(self):
		"""
		Takes input and returns it
		"""
		print("Input: ")
		yo_input = eval(input())
		return yo_input

	def output_handler(self, yo_input):
		"""
		runs the search and outputs the result
		"""
		print("Output: ")
		startF = datetime.datetime.now()
		for ele in yo_input:
			found = self.lets_search(ele)
			if len(found):
				print(ele + " is available in " + " and ".join(found)+".")
			else:
				print(ele + " not found! or check input!")
		endF = datetime.datetime.now()
		print("The test case execution time is ",
              (endF - startF).total_seconds()% 86400, "sec")

	def lets_search(self, ele):
		"""
		heart of the search
		"""
		output = []
		for key in self.big_dictionary:
			if ele in self.big_dictionary[key]:
				output.append(key)
		return output

afs = AmazeFileSearch()