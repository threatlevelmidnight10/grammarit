from grammarit.models.auto_complete.markov_auto_complete import MarkovAutoComplete
from grammarit.src.grammar.parse import *


def process_input(read_input):

    autocomplete = MarkovAutoComplete(read_input)
    return autocomplete.autocomplete(read_input)
