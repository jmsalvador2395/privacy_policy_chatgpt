import re
class Directive:
	def __init__(self):
		self.options = [
			'no_con',
			'with_con',
		]
	
	def get_options(self):
		return self.options

	def gen_no_con(self, question_list):
		text = ', '.join(question_list[:-1])
		text += f' and {question_list[-1]}'

		# remove all punctuation and add question mark at the end
		text = re.sub('[\?\.]', '', text)
		text += '?'

		return text

	def gen_with_con(self, question_list):
		text = 'based off the given documents, please answer the following questions:\n\n'
		for i, q in enumerate(question_list):
			text += f'{i+1}) {q}\n'

		# remove all punctuation and add question mark at the end
		text = re.sub('[\.]', '?', text)

		return text

	def gen_text(self, question_list, option):
		if option not in self.options:
			option_text = '[' + '.'.join(self.options) + ']'
			raise KeyError(
				f'the given option ("{option}") is not in the list of valid options.' +
				f'the valid options are:' +
				option_text
			)

		if option == 'no_con':
			return self.gen_no_con(question_list)
		elif option == 'with_con':
			return self.gen_with_con(question_list)
