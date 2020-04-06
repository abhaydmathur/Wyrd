# Also, I won't be using many libraries and want to keep it that way unless absolutely necessary


import pickle
import re

from trie import trie

# Building the player model

player = trie()

fil = open("Where_eagles_dare.txt", "r")
text = fil.read()
words = re.split(r'\W+', text)
for word in words:
    player.add(word)
player.purge_errors()

print('The model has updated its vocab after reading the file.')
obj_file = open("player_vocab.pickle", 'wb')

obj_file.write(pickle.dumps(player))
obj_file.close()

