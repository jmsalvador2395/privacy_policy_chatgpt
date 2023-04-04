
class Scenario:
	def __init__(self, doc_type, context):

		self.doc_type = doc_type
		self.context = context
		self.options = [
			'no_con',
			'some_con',
			'most_con',
			'full_con',
		]

	def get_options(self):
		return self.options
		
	def ordinal(self, n):
		if 11 <= (n % 100) <= 13:
			suffix = 'th'
		else:
			suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
		return str(n) + suffix	

	def gen_no_con(self, ref_documents):
		text = ''
		for i, d in enumerate(ref_documents):
			text += f'{self.doc_type["singular"]} {i+1}:\n--\n{d}\n--\n\n'

		return text

	def gen_some_con(self, ref_documents):
		text = f'I have {len(ref_documents)} {self.doc_type["plural"]} I would like you to look at\n'
		for i, d in enumerate(ref_documents):
			text += f'The {self.ordinal(i+1)} {self.doc_type["singular"]} is:\n--\n{d}\n--\n\n'

		return text

	def gen_most_con(self, ref_documents):
		text = \
			f'I have been given {len(ref_documents)} {self.doc_type["plural"]}. ' + \
			self.context + \
			'here are the documents:\n'

		for i, d in enumerate(ref_documents):
			text += f'The {self.ordinal(i+1)} {self.doc_type["singular"]} is:\n--\n{d}\n--\n\n'

		return text


	def gen_full_con(self, ref_documents):
		text = \
			f'I have been given {len(ref_documents)} {self.doc_type["plural"]}. ' + \
			self.context + \
			f' The "--" sequence is used to denote the beginning and end of a particular {self.doc_type["singular"]}. ' + \
			'here are the documents:\n'

		for i, d in enumerate(ref_documents):
			text += f'The {self.ordinal(i+1)} {self.doc_type["singular"]} is:\n--\n{d}\n--\n\n'

		return text


	def gen_text(self, ref_documents, option):
		
		# check for invalid option
		if option not in self.options:
			option_text = '[' + '.'.join(self.options) + ']'
			raise KeyError(
				f'the given option ("{option}") is not in the list of valid options.' +
				f'the valid options are:' +
				option_text
			)
		
		if option == 'no_con':
			return self.gen_no_con(ref_documents)
		elif option == 'some_con':
			return self.gen_some_con(ref_documents)
		elif option == 'most_con':
			return self.gen_most_con(ref_documents)
		elif option == 'full_con':
			return self.gen_full_con(ref_documents)
