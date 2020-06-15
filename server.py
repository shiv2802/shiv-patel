from _socket import  *
import  time
from  threading import  Thread

class clienthandel(Thread):
    def __init__(self, client ):
        Thread.__init__(self)
        self_client = client

    def run(self):
        self._client.send(bytes(c_time() + "have"))
        self._client.close()

HOST = "localhost"
PORT = 15201
BUFERSIZE =1024

ADRRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADRRESS)
server.listen(5)
while True:
    print("waiting")
    client,  address = server._accept()
    print("contecton " + address)
    handel = clienthandel(client)
    handel.start()