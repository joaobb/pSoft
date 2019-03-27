import socket
import sys
from threading import Thread
import os

connections = {}

def newClient(connection):
    connection.send(("=== Welcome to LilChat! ===\nPlease enter a nickname: ").encode())
    nickName = connection.recv(2048).decode('utf-8').strip()
    connections[connection] = nickName
    connection.send("> ".encode())
    
    while True:
        message = connection.recv(4096).decode('utf-8').strip()
        if message == ":bye": 
            connection.send("You have been disconnected.\n".encode())
            print("{} - has been disconnected.".format(nickName))
            
            connection.close()
            del connections[connection]

            for con in connections:
                con.send(("{} has been disconnected\n".format(nickName)).encode())
            exit()
            
        if message:
            print("{} says: {}".format(nickName, message))
            for con in connections:
                if not (con == connection):
                    con.send(("{}: {}\n> ".format(nickName, message)).encode())
                else: con.send("> ".encode())

def serverControl(socket, port, host_ip):
    print("=== PRESS :h FOR HELP ===")
    while True:
        command = input()

        if command == ":terminate":
            os.system("sudo lsof -i :{} & ".format(port))
            for con in connections:
                con.send("Closing the server... cya\n".encode())
            
            socket.close()
            print("Closing every program connected to port %i" % port)
            #Check if it works without sudo access
            if connections:
                os.system("lsof -n -i4TCP:%i | tr -s ' ' | cut -d' ' -f2 | grep -E [[:digit:]] | xargs kill" % port)
            exit()

        elif command[:6] == ":send ":
            for con in connections:
                con.send("SERVER SAYS: {}\n".format(command[6:]).encode())
        
        elif command == ":h":
            print('\033[1m' + "\n=== LilChat HELPER === \n\nnc {} {} ".format(host_ip, port) + '\033[0m' + " - Connects to this miniChat server from another terminal.")
            print('\033[1m' + "\nOPTIONS:\n   :send [message]" + '\033[0m' + " - Send a message for every client connected.")
            print('\033[1m' + "        :terminate" + '\033[0m' + " - Closes the server and every client connected.")
            print('\033[1m' + "                :h" + '\033[0m' + " - Shows server manager options.\n")
        else:
            print("=== Entered command is invalid ===")

port = int(sys.argv[1] if len(sys.argv) > 1 else 9090)
host_ip = socket.gethostbyname(socket.gethostname())

with socket.socket() as s:
    Thread(target=serverControl, args=(s,port,host_ip,)).start()

    s.bind((host_ip, port))
    s.listen()
    print("Listening to {} {}".format(host_ip, port))
    
    while True:
        connection, address = s.accept()
        print("{}:{} connected to the server".format(address[0], address[1]))
        Thread(target=newClient, args=(connection,)).start()
        