from itertools import product

from prompt_eng.scenarios import Scenario
from prompt_eng.directives import Directive

class Prompt:
	
	def __init__(self, questions, doc_type, context):
		self.questions = questions

		self.scen = Scenario(doc_type, context)
		self.direc = Directive()


	def gen_prompts(self, ref_documents):
		prompts = {}
		for scen, direc in product(self.scen.get_options(), self.direc.get_options()):
			scen_text = self.scen.gen_text(
				ref_documents,
				option=scen
			)
			direc_text = self.direc.gen_text(
				self.questions, 
				option=direc
			)
			prompts[f'scen={scen},direc={direc}'] = scen_text + direc_text


		return prompts



