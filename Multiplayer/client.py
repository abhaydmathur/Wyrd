from network import Network
import pickle

def main():
    run = True
    n = Network()
    player = int(n.getP())

    while run:
        # TODO : Play the game
        try:
            game = n.send("""info""")

if __name__=="__main__":
    #TODO: loop main()