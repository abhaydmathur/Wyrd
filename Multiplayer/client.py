import sys
sys.path.append("..")

from network import Network
import pickle
import os
import dict

def main():
    run = True
    n = Network()
    player = int(n.getP())

    while run:
        # TODO : Play the game
        try:
            game = n.send("""info""")
        except:
            pass
    # pass

if __name__=="__main__":
    #TODO: loop main()
    pass