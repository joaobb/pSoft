# coding: utf-8

import socket, sys, os
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('google.com', 80))
print ('O IP Público do Servidor é: {}'.format(s.getsockname()[0]))

print ('O IP Local do Servidor é: {}'.format(socket.gethostbyname(socket.gethostname())))

porta = int(sys.argv[1] if len(sys.argv) > 1 else 9090)

s = socket.socket()
s.bind(('', porta))

s.listen(10)
print("Aguardando conexão com a porta {}".format(porta))

vrp = {}
header = {}
corpo = {}

response = ""

def parse_request(mensagem):
	global response
	
	protocolo = "HTTP/1.1"
	code = 200
	status = "OK"
	mime_type = "text/html"
	charset = "charset=utf-8"
	corpo_response = "Este é o conteúdo do recurso '/' neste servidor.<hr><h1>Directory Listing</h1><ul>"
	
	for p, _, files in os.walk(os.path.abspath(os.getcwd())):
		for file in files:
			caminho = os.path.join(p,file).split('/httpserver/',1)[-1]
			corpo_response += "<li><a href='" + caminho + "'>" + caminho + "</a></li>"

	corpo_response += "</ul>"


	try:
		mensagem = mensagem.decode().split("\r\n")

		splitted = mensagem[0].split()
		
		vrp["verbo"] = splitted[0]
		vrp["recurso"] = splitted[1]
		vrp["protocolo"] = splitted[2]

		myfile = vrp["recurso"].split('?')[0] # After the "?
		
		try:
			if (myfile != '/'):
				myfile = myfile.lstrip('/')
				file = open(myfile,'rb') # open file , r => read , b => byte format
				corpo_response = file.read()
				corpo_response = corpo_response.decode()
				file.close()

				if (myfile.endswith(".jpg")):
					mime_type = 'image/jpg'
				elif (myfile.endswith(".css")):
					mime_type = 'text/css'
				elif (myfile.endswith(".html")):
					mime_type = 'text/html'
				else:
					mime_type = 'text/plain'
	 
		except:
			code = 404
			status = "Not Found"
			corpo_response = "<html><body><center><h3>Error 404: Página não encontrada</h3><p>Python HTTP Server</p></center></body></html>"
		
		if vrp["verbo"] != "GET":
			code = 405
			status = "Method Not Allowed"
			corpo_response = "<html><body><center><h3>Error 405: Método Não suportado</h3><p>Python HTTP Server</p></center></body></html>"

		for i in range(1,len(mensagem)-1):
			if mensagem[i]:
				dp = mensagem[i].find(":")
				chave = mensagem[i][:dp] 
				valor = mensagem[i][dp+2:].strip()

				header[chave] = valor

		corpo["corpo"] = mensagem[-2]
		

		response = "{} {} {}\nContent-Type: {};{}\nStatus: {} {}\n\n{}\n".format(protocolo, code, status, mime_type, charset, code, status, corpo_response).encode()

	except:
		print ("Erro no parse de sua request")

while 1:
	
	conexao, endereco = s.accept()
	print("Conectado em: {}:{}".format(endereco[0],endereco[1]))

	mensagem = conexao.recv(4096)
	parse_request(mensagem)
	conexao.send(response)
	conexao.close()

s.close()
