# Also, I won't be using many libraries and want to keep it that way unless absolutely necessary


import pickle
import re

from trie import trie

# Building the player model

player = trie()

with open('Resources/booklist.txt') as booklist:
    books = booklist.readlines()
    for book in books:
        fil = open("Resources/" + book[:-1] )#+ ".txt", "r")
        text = fil.read()
        words = re.split(r'\W+', text)
        for word in words:
            player.add(word)
        player.purge_errors()

print('The model has updated its vocab after reading the file.')
obj_file = open("player_vocab.pickle", 'wb')

pickle.dump(player, obj_file)
obj_file.close()