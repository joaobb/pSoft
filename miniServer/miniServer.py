import socket
import sys
from threading import Thread

connections = {}

port = int(sys.argv[1] if len(sys.argv) > 1 else 9090)
host_ip = socket.gethostbyname(socket.gethostname())
print("Hosts ip is: %s\n" % host_ip)

def newClient(connection):
    connection.send("=== Welcome to the chat! ===\nPlease enter a nickname: ".encode())
    nick = connection.recv(2048)
    connections[connection] = nick

    while True:
        message = connection.recv(4096).decode('utf-8').strip()
        if message == ":bye": 
            connection.send("You have been disconnected.\n".encode())
            print("{} - has been disconnected.".format(nick))

            for con in connections:
                if con != connection:
                    connection.send(("{} has been disconnected".format(nick)).encode())
            break
        if message:
            print("{} says: {}".format(nick, message))
            for con in connections:
                if con != connection:
                    con.send((message + "\n").encode())

with socket.socket() as s:
    s.bind((host_ip, port))
    s.listen()
    print("Listening to gate {}".format(port))
    
    while True:
        connection, address = s.accept()
        with connection:
            print("{}:{} connected to the server".format(address[0], address[1]))
            Thread(target=newClient, args=(connection,)).start()
        

    #with connection:
    #    print("We have connected to %s:%s" % address) 

