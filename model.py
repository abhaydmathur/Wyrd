# Also, I won't be using many libraries and want to keep it that way unless absolutely necessary


import pickle
import re
import numpy as np
import sys

from trie import trie

# Building the player model

player = trie()

with open('Resources/booklist.txt') as booklist:
    books = booklist.readlines()
    for book in books:
        fil = open("Resources/" + book[:-1] )
        text = fil.read()
        words = re.split(r'\W+', text)
        words = np.unique(np.array(words))
        n_block = 30
        done = "["
        rem = (n_block)*"~"
        block = int(len(words)/n_block)
        for i, word in enumerate(words):
            print(f"\rReading from {book[:-1]} : {done}{rem}] : {i*100/(len(words)):0.2f}% ", end = "")
            if(i%block == 0):
                # Progress Bar
                done += "="
                rem = rem[1:]
                sys.stdout.flush()
            player.add(word)
            if(i == len(words)-1) : print(f"\rReading from {book[:-1]} : {done}{rem}] : 100% ", end = "")
        print()
        player.purge_errors()

print('Vocab updated.')
obj_file = open("Resources/player_vocab.pickle", 'wb')
pickle.dump(player, obj_file)
obj_file.close()