#Joao Pedro de Barros Barbosa
#117210327

import socket
import sys
import os

port = int(sys.argv[1] if len(sys.argv) > 1 else 9090)

def parse_request(mensagem):
    try:
        mensagem = mensagem.decode('utf-8').split("\r\n")
        mppRaw = mensagem[0].split()

        #Every method available on the server
        methods = ["GET"]
        #Every accessible path on the server
        paths = ["/"] + os.listdir()
        
        method = mppRaw[0]
        path = mppRaw[1]
        prot_vers = mppRaw[2]

        headers = {}
        for head in range(1, len(mensagem) - 2):
            spl_head = mensagem[head].split(':', 1) 
            headers[spl_head[0]] = spl_head[1]

        if path != "/":
            path = path[1:]
                
        if method not in methods:
            status_code = 405
            status = "Method Not Allowed"
            response_body = """<html><head><title>405 Method Not Allowed</title></head><body><h1>Method Not Allowed</h1>
        <p>The method {} is not allowed on this server.</p>
        </body></html>
        """.format(method)

        elif path not in paths:
            status_code = 404
            status = "Not Found"
            response_body = """<html><head><title>404 Not Found</title></head><body><h1>Not Found</h1>
        <p>The requested URL {} was not found on this server.</p>
        </body></html>
        """.format(path)

        else:
            status_code = 200
            status = "OK"
            if path == "/":
                response_body = """<html><head><title>{}</title></head><body><h1>Este é o conteúdo do recurso {} neste servidor.</h1></body></html>""".format(path, path)
            else:
                file = open(path, "r")
                response_body = """<html><head><title>{}</title></head><body><p>{}</p></body></html>""".format(path, file.read())
                file.close()

        mime_type = "text/html" if (path.endswith(".html") or path == "/" or status_code != 200) else "text/plain"
        charset = "utf-8"

        response = "{} {} {}\nHost: {}\nContent-Type: {}; charset={}\n\n{}".format(prot_vers, status_code, status, headers['Host'], mime_type, charset, response_body)
        return response
    except:
        print("=== Error while parsing request ===")
        return ("""<html><head><title>ERROR</title></head><body><h1>ERROR WHILE PARSING THE REQUEST</h1></body></html>""")

with socket.socket() as s:
    host_ip = socket.gethostbyname(socket.gethostname())
    print("=== TO CONNECT TO THE SERVER ACCESS {}:{} ===".format(host_ip, port))

    s.bind(("", port))
    s.listen()

    while True:
        connection, address = s.accept()
        with connection:
            print("{} has connected to the server".format(address[0]))
            request = connection.recv(4096)
            connection.send(parse_request(request).encode())
            connection.close()

s.close()