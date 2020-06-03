import os

def get_server_address(mode = "local"):
    if mode == "local":
        address = os.popen("hostname -I")
    else:
        address = os.popen("hostname ")