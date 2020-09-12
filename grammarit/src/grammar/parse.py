from spellchecker import SpellChecker


class Parser():
	"""Naive spell cheker using spellchecker package in python
	"""
	def __init__(self, sentence):
		self.spellchecker = SpellChecker('en')
		self.sentence = sentence

	def get_corrections(self):
		words = self.sentence.split()
		wrong_words = self.spellchecker.unknown(words)
		corrections = {}
		for word in wrong_words:
			corrections[word] = self.spellchecker.correction(word)

		return corrections
