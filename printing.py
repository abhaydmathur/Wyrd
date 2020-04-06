from trie import trie

tree = trie()

tree.add("The")
tree.add("There")
tree.add("their")
tree.add("two")

tree.print_vocab(tree.root)