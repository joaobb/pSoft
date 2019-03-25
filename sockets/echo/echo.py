import socket
import sys

# porta default 9090 (ou o que vier na linha de comando)
porta = int(sys.argv[1] if len(sys.argv) > 1 else 9090)

with socket.socket() as s:
    s.bind(('localhost', porta))
    s.listen()

    print('Aguardando conexões na porta %s...' % porta)
    conexao, endereco = s.accept()
    with conexao:
        print('Conexão estabelecida de %s:%s' % endereco)
        while True:
            print('Aguardando mensagem de %s:%s' % endereco)
            mensagem = conexao.recv(4096)
            print('Mensagem: %s' % mensagem)
            if not mensagem: break
            conexao.sendall(mensagem)
