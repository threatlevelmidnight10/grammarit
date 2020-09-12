import re


def tokenize(text):
    tokens =  [word.lower() for word in text.split()]
    tokens = filter_tokens(tokens)
    return tokens

def filter_tokens(tokens):
    # one more filter pass to remove unneccessary symbols
    return tokens