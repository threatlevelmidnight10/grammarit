from grammarit.utils.utils import tokenize
import random

class MarkovAutoComplete:
    def __init__(self, text):
        self.tree = dict()
        self.new_tree = dict()
        self.tokens = []

    # one hot encode
    def _init_chain(self, text, factor=1.0):
        #tokenize txt
        tokens = tokenize(text)
        self.tokens = tokens
        for a,b in [(tokens[i], tokens[i+1]) for i in range(0,len(tokens)-1)]:
            if a not in self.tree:
                self.tree[a] = dict()
            if b not in self.tree[a]:
                self.tree[a][b] = factor
            else:
                self.tree[a][b] *= self.tree[a][b] * factor

    #randomize weights to chain
    def randomize_weights(self):
        for root, child in self.tree.items():
            if not isinstance(child, dict):
                continue
            subtree_size = len(child)
            for c in child:
                self.tree[root][c]  = (random.random()) * (self.tree[root][c]/subtree_size)

        #sort the vals
        for k, v in self.tree.items():
            if isinstance(v, dict):
                self.new_tree[k] = [(key,val) for key,val in v.items()]
                self.new_tree[k].sort()

    # autocomplete function
    def autocomplete(self, length=3):
        last_word = self.tokens[-1]
        sentence = ''
        for i in range(0,3):
            if last_word in self.new_tree:
                for word in self.new_tree[last_word]:
                    sentence += word[0]
                    last_word = word[0]
            else:
                break
        return sentence

    def train(self, text):
        chain  = self._init_chain(text)
        self.randomize_weights()