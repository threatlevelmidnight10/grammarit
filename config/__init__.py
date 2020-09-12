import configparser


SETUPS = """
[ALL]
default_corpus=./tests/default_corpus.txt
"""


def get(key):
	parser = configparser.ConfigParser()
	parser.read_string(SETUPS)
	return parser['ALL'][key]
