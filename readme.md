# Word Building 

Rules of the game:</br>
    1. Build words letter by letter. The objective is to manipulate moves such that the 
    last alphabet is entered by the opponent or one of the opponents</br>
    2. If at any point in time a sequence has been created which does not form a prefix to any word in our
    vocabulary, then the current player asks the previous player to disclose the word they're trying to form.</br>
    If the answer is a valid word as per the rules, the current player loses a point and vice versa.
</br></br>
We are simply using prefix trees at the moment for the model's vocabulary.

### Commands:
#### show 
Returns the list of possible words in the current context from the vocabulary.
#### stop 
Checks whether a word has been formed; scores accordingly
#### exit()
Does what one might think it does.

### Scoring
-1 per penalty.<br>

Pro tip: Simply press Enter to let the bot start.





