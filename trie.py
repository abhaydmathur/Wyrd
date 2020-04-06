# Module for prefix     trees
import pickle
import re

class node(object):
    def __init__(self, val):
        self.val = val
        self.children = []
        self.isend = False

    def add_child(self,child):
        self.children.append(child)

    def get_val(self):
        return self.val

class trie(object):
    def __init__(self):
        self.root = node(None)
    
    def add(self, word):
        word = word.lower()
        curr = self.root
        for i, a in enumerate(word):
            if a not in [child.val for child in curr.children]:
                curr.children.append(node(a))
                curr = curr.children[-1]
            else:
                for j, val in enumerate([child.val for child in curr.children]):
                    if val == a:
                        curr = curr.children[j]
                        break   
            if i == len(word) - 1:
                curr.isend = True
        return None


    def print_(self, start_node): #simply printing all the letters in the vocab for now
        for child in start_node.children:
            self.print_(child)
        if start_node.val!=None : print(start_node.val) 

    def print_vocab(self, node, first=False, word = ""): # printing all the words in the vocabulary
        # We need a designation for where the word ends as well.
        if first:
            print("My vocab presently contains:")
        # Base Case:
        if len(node.children)==0:
            print(word)
        else:
            if node.isend == True:
                print(word)
            for child in node.children: 
                self.print_vocab(child, first = False, word = word+child.val)
    
    def search_word(self, word):
        pass

    def words_with(self, pre):
        # finding the 
        curr = self.root
        for char in pre:
            for i, a in enumerate([node.val for node in curr.children]):
                if a == char:
                    curr = curr.children[i]
                    break
        self.print_vocab(curr,  False, pre)

    def clear(self):
        for child in self.root.children:
            self.root.children.remove(child)
    
    def purge_errors(self):
        for child in self.root.children:
            if child.isend:
                if child.val not in ['i', 'a']: child.isend = False

def clean(string):
    for word in string:
        if len(word) == 1:
            string.remove(word)
    return string



if __name__ == '__mai__':
    tree = trie()
    tree.add("abhay")
    tree.add("abate")
    tree.add("absolutely")
    tree.add("habit")
    print("Vocab - ")
    tree.print_vocab(tree.root)
    print("words with ab -")
    tree.words_with("ab")

if __name__ == "__main__":
    vocab = trie()
    text = open("Where_eagles_dare.txt", "r+")
    text = text.read()
    words = re.split(r'\W+', text)
    for word in words:
        vocab.add(word)
    vocab.purge_errors()
    vocab.print_vocab(vocab.root, True)
    vocab.clear()
    print("vocab cleared")