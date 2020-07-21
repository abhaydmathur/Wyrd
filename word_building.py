from trie import trie
import pickle
import sys
import numpy as np
import time
import os
import dict
import speech.stt as stt
import speech.tts as tts
def win_title(title):
    if os.name == 'posix':
        print(f'\33]0;{title}\a', end='', flush=True)
    else:
        os.system(f"title {title}")

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
    
    def reset(self):
        self.current_node = self.vocab_tree.root

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

    def show_response(self, pref):
        global words_played, user_score
        words = self.vocab_tree.get_words_with(pref)
        valid_words = [word for word in words if word not in words_played]
        if not len(valid_words):
            print("Oops.")
            user_score += 1
            self.score -= 1
            return
        print(valid_words[0])
        words_played.append(valid_words[0])
        

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
        global user_score, words_played
        if not(dict.check(word)) or len(word) < 4 or word in words_played:
            print("Nope. Real words with length >= 4 only.")
            user_score -= 1
            return False
        
        self.vocab_tree.add(word)
        self.score -= 1
        return True

    def stop(self):
        global done, user_score
        print("STOP\n ")
        user_score -= 1
        done = True
        
    
def main(bot):
    global done, user_score, bored, words_played
    done = False
    word = ""
    bot.reset()
    while not done:
        
        print(word)
        ch = (input('>> '))
        if ch.lower() == 'stop':
            done = bot.stop_response(word)
            if done : break
        elif ch.lower() == 'exit()':
            bored = False
            break
        elif ch.lower() == 'show':
            if len(word):
                bot.show_response(word)
                user_score -= 1
                done = True
                break
            else:
                print("Atleast make a move.")
                continue
        elif  len(ch) != 1 and len(word)>0:
            print("Invalid command\n")
            continue
        else:
            word = word + ch.lower()
            word = bot.play(word)
            tts.play_response(word[-1])
    if bored:
        input("Enter any char to continue\n")
    words_played.append(word)
    return bot
        

def main():
    words_played = []
    win_title("Wyrd")
    user_score = 0
    bot = player(load_model('Resources/player_vocab.pickle'))
    bored = True
    while bored:
        clrscr()
        print("WORD BUILDING")
        print(f"Your Score : {user_score} ||  Bot's score : {bot.score}")
        bot  = main(bot)
    obj_file = open("Resources/player_vocab.pickle", 'wb')
    pickle.dump(bot.vocab_tree, obj_file)
    obj_file.close()

if __name__ == "__main__":
    main()