import socket 
from _thread import *
import pickle
from wyrd_proc import Proc
from server_utils import get_server_address as gsa

max_players = 2

server = gsa()
port = 4061

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(max_players)

print("Waiting for a connection, Server Started.")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId): # TODO : procId?
    global idCount, games 
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else: # TODO
                    if data == None:
                        game.something()
                    elif data == None:
                        game.somethingelse()
                    
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break
    
    print("Lost Connection")
    try:
        del games[gameId]
        print("Closing shell", gameId)
    except:
        pass
    
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to : ", addr)

    idCount += 1
    p = 0
    gameId = (idCount-1)//max_players
    
    if idCount such that this is the first player:
        games[gameId] = Proc(gameId,max_players)
        print("Creating a new game")
    else:
        games[gameId].something = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))