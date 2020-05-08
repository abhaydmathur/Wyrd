from trie import trie
import pickle
import sys
import numpy as np
import os
import dict

def clrscr():
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system('cls')

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
            self.get_show(word)
        return word

    def show(self, pref):
        self.vocab_tree.words_with(pref)
        

    def get_show(self, word):
        global done, user_score
        print("Show")
        word_ = input("~> ")
        if not word in word_ or len(word_) < 4 :
            print(f"What? We're talking about something that starts with {word.upper()}, of length greater or equal to 4.")
            self.get_show(word)
            return
        elif dict.check(word_):
            print("You're right; didn't think of that one :) ")
            self.score -= 1
            self.vocab_tree.add(word_)
        else:
            print("I knew you were bluffing ;) ")
            user_score -= 1
        done = True

    def stop_response(self, word):
        global user_score
        if not (dict.check(word)):
            print("No bluffing.")
            user_score -= 1
            return
        self.score -= 1

    def stop(self):
        global done, user_score
        print("STOP\n ")
        user_score -= 1
        done = True
        
    
def main(bot_):
    global done, user_score
    done = False
    word = ""
    bot = player(load_model('player_vocab.pickle'))
    bot.score = bot_.score
    while not done:
        
        print(word)
        ch = (input('>> '))
        if ch.lower() == 'stop':
            bot.stop_response(word)
            done = True
            break
        elif ch.lower() == 'exit()':
            os._exit(1)
        elif ch.lower() == 'show':
            if len(word):
                bot.show(word)
                user_score -= 1
                done = True
                break
            else:
                print("Atleast make a move.")
                continue
        elif len(ch) > 1:
            print("Invalid command\n")
            continue
        word = word + ch.lower()
        word = bot.play(word)
    input("Enter any char to continue\n")
    return bot
        
if __name__ == "__main__":
    print('\33]0;Wyrd\a', end='', flush=True)
    user_score = 0
    bot = player(load_model('player_vocab.pickle'))
    while True:
        clrscr()
        print("WORD BUILDING")
        print(f"Your Score : {user_score} ||  Bot's score : {bot.score}")
        bot  = main(bot)
    
    
    obj_file = open("player_vocab.pickle", 'wb')
    pickle.dump(player, obj_file)
    obj_file.close()