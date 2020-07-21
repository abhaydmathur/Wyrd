from trie import trie
import word_building as wb

tree = wb.load_model("Resources/player_vocab.pickle")

tree.words_with("aa")