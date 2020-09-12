from grammarit.models.auto_complete.markov_auto_complete import MarkovAutoComplete
from grammarit.src.grammar.parse import *

read_input = input("Enter the input:\n")

autocomplete = MarkovAutoComplete(read_input)
print(autocomplete.autocomplete(read_input))

print(Parser(autocomplete.autocomplete((read_input)[read_input])).get_corrections())
