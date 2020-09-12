from PyDictionary import PyDictionary

class Synonym():
	"""
		Helps with better wording
	"""

	def __init__(self, input_word):
		self.dictionary = PyDictionary()
		self.input_word = input_word

	def get_synonyms(self, limit=10):
		"""
			Lists down synonyms
		"""
		word = self.input_word
		return self.dictionary.synonym(word)
