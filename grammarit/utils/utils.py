import re
import json
import os


def tokenize(text):
    tokens =  [word.lower() for word in text.split()]
    tokens = filter_tokens(tokens)
    return tokens

def filter_tokens(tokens):
    # one more filter pass to remove unneccessary symbols
    return tokens


def get_algo_configuration():
    configuration_data = json.loads(open("grammarit/config/config.json", "r").read())
    algo_config_file = configuration_data["algo_config"]
    algo_configuration = json.loads(open("grammarit/config/algo_config/{}".format(algo_config_file), "r").read())
    return algo_configuration