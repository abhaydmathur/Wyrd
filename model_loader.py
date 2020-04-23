from trie import trie
import pickle

obj_file = open('player_vocab.pickle', 'r')
print(pickle.loads(obj_file))