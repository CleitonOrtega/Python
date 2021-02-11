import socket

resp="S"

while (resp=='S'):
    url=input("Digite uma URL: ")
    ip=socket.gethostbyname(url)
    print("O link do site é: "+ url +" e o IP dele é: "+ip)
    resp=input("Digite <s> para ver outro IP: ").upper()