from trie import trie
import pickle
import sys
import numpy as np

def load_model(file_name):
    obj_file = open(file_name, 'rb')
    tree = trie()
    tree = pickle.load(obj_file)
    return tree

class player(object):
    
    def __init__(self, vocab_tree):
        self.vocab_tree = vocab_tree
        self.current_node = self.vocab_tree.root
        self.score = 0
    
    def play(self, word):
        last_char = word[-1]
        if(last_char in [child.val for child in self.current_node.children]):
            self.current_node = [child for child in self.current_node.children if child.val == last_char][0]
            if len(self.current_node.children) == 0:
                self.stop()
            self.current_node = np.random.choice(self.current_node.children) 
            print("Move : ", self.current_node.val)
            word = word + self.current_node.val
        else:
            print("SHOW")
            self.show()
        return word

    def show(self):
        pass

    def stop(self):
        print("STOP")
        sys.exit()
        
    
def main():
    bot = player(load_model('player_vocab.pickle'))
    word = ""
    print("WORD BUILDING")
    while True:
        print(word)
        ch = (input('>> '))
        if ch.lower() == 'stop':
            break
        word = word + ch
        word = bot.play(word)

main()