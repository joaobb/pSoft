import socket
import sys
import os

port = int(sys.argv[1] if len(sys.argv) > 1 else 9090)

def parse_request(mensagem):
    meth_path_protV = {}
    mensagem = mensagem.decode('utf-8').split("\r\n")
    mppBrute = mensagem[0].split()

    methods = ["GET"]
    path = ["/"]

    print(splitted)

    meth_path_protV["method"] = mppBrute[0]
    meth_path_protV["path"] = mppBrute[1]
    meth_path_protV["prot_vers"] = mppBrute[2]

    if meth_path_protV["method"] is not in methods:
        status_code = 405
        status = "Method Not Allowed"
        response_body = """<html><head><title>405 Method Not Allowed</title></head><body><h1>Method Not Allowed</h1>
<p>The method {} is not allowed on this server.</p>
</body></html>
""".format(meth_path_protV["path"])

    elif meth_path_protV["path"] is not in path:
        status_code = 404
        status = "Not Found"
        response_body = """<html><head><title>404 Not Found</title></head><body><h1>Not Found</h1>
<p>The requested URL {} was not found on this server.</p>
</body></html>
""".format(meth_path_protV["path"])

    else:
        status_code = 200
        status = "OK"
    respose = "HTTP/1.1 "

with socket.socket() as s:
    host_ip = socket.gethostbyname(socket.gethostname())
    print("=== TO CONNECT TO THE SERVER ACCESS {}:{}".format(host_ip, port))

    s.bind(("", port))
    s.listen()

    while True:
        connection, address = s.accept()
        print("{} has connected to the server".format(address[0]))
        request = connection.recv(4096)
        parse_request(request)