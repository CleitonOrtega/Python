from socket import *

servidor = "127.0.0.1" #localHost
porta=43210

objSocket = socket(AF_INET,SOCK_DGRAM)
objSocket.bind((servidor,porta))
print("Serfidor pronto...")

while True:
    dados, origem = objSocket.recvfrom(65535)
    print("Origem..........: ",origem)
    print("Dados recebidos.: ",dados.decode())
    resposta = input("Digite a resposta para o cliente: ")
    objSocket.sendto(resposta.encode(),origem)

objSocket.close()