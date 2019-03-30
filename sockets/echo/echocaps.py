#Joao Pedro de Barros Barbosa
#117210327

import socket
import sys

port = int(sys.argv[1] if len(sys.argv) > 1 else 9090)
host_ip = socket.gethostbyname(socket.gethostname())

with socket.socket() as s:
    s.bind(("", port))
    s.listen()
    
    print("Listening to {}:{}".format(host_ip, port))
    
    connection, addres = s.accept()
    
    with connection:
        while True:
            message = connection.recv(4096).decode().strip()
            if not message: break
            connection.send((message.upper() + "\n").encode())