from socket import *

servidor = "127.0.0.1" #localHost
porta=43210

objSocket = socket(AF_INET,SOCK_STREAM)
objSocket.bind((servidor,porta))
objSocket.listen(2)

print("Aguardando cliente...")

while True:
    con,cliente = objSocket.accept()
    print("Conectado com: ",cliente)
    while True:
        msgRecebida = str(con.recv(1024))
        print("Recebemos: ",msgRecebida)
        msgEnviada = b'Bem-vindo'
        con.send(msgEnviada)
        break
    con.close()