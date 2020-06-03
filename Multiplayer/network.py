import socket
from server_utils import get_server_address as gsa
import pickle

class Network:
    def __init__(self, address = None):
        self.client = socket.socket(socket.AP_INET, socket.SOCK_STREAM)
        
        if address in None:
            self.server = gsa()
        else:
            self.server = address

        self.port = 4061
        self.addr = (self.server,self.port)
        sefl.p = self.connect()
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
        
    def self.getP(self):
        return self.p 
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)