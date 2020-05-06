from trie import trie
import pickle
import sys
import numpy as np
import os
import dict

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
        if(len(word)==0):
            self.current_node = np.random.choice(self.current_node.children)
            return word + self.current_node.val
        last_char = word[-1]
        if(last_char in [child.val for child in self.current_node.children]):
            self.current_node = [child for child in self.current_node.children if child.val == last_char][0]
            if len(self.current_node.children) == 0 or self.current_node.isend:
                self.stop()
            else:
                self.current_node = np.random.choice(self.current_node.children) 
                print("Move : ", self.current_node.val)
                word = word + self.current_node.val
        else:
            self.get_show()
        return word

    def show(self, pref):
        self.vocab_tree.words_with(pref)

    def get_show(self):
        global done
        print("Show")
        word_ = input("~> ")
        if dict.check(word_):
            print("You're right; didn't think of that one :) ")
        else:
            print("I knew you were bluffing ;) ")
        done = True

    def stop_response(self, word):
        if not (dict.check(word)):
            print("No bluffing.")

    def stop(self):
        global done
        print("STOP\n ")
        done = True
        
    
def main():
    global done 
    done = False
    bot = player(load_model('player_vocab.pickle'))
    word = ""
    print("WORD BUILDING")
    while not done:
        
        print(word)
        ch = (input('>> '))
        if ch.lower() == 'stop':
            bot.stop_response(word)
            done = True
            break
        elif ch.lower() == 'exit()':
            sys.exit()
        elif ch.lower() == 'show':
            bot.show(word)
            done = True
            break
        elif len(ch) > 1:
            print("Invalid command\n")
            continue
        word = word + ch
        word = bot.play(word)
    input("Enter any char to continue\n")
        
if __name__ == "__main__":
    while True:
        os.system("clear")
        main()