import os

def get_server_address(mode = "local"):
    if mode == "local" and os.name == "posix":
        address = os.popen("hostname -I").read()
    else:
        address = os.popen("hostname").read()
    address = address[:-2] # removing the \n
    return address