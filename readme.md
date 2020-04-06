# Building a model to play word building to finally emulate a game with Vedaarth Bhaiya

"""
Author - @ Abhay Dayal Mathur

Rules of the game  (Word Building that I am trying to simulate):
    1. We just need to build words letter by letter. The objective is to manipulate moves such that the 
    last alphabet is entered by the opponent or one of the opponents
    2. If at any point in time a sequence has been created which does not form a prefix to any word in our
    vocabulary, then the current player asks the previous player to disclose the word they're trying to form.
    If the answer is a valid word as per the rules, the current player loses a point and vice versa...

We are simply using prefix trees at the moment for the model's vocabulary. Will try to emulate
humanoid memory wherein some words are more strongly recalled as compared to others by providing weights
as per frequency of usage in the games as well as the 
"""