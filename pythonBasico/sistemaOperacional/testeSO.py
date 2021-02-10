#import platform
import getpass
#from datetime import datetime

#print("Nome da Maquinha.....:", platform.node())
#print("Arquitetura..........:", platform.architecture())
#print("Sistema Operacional..:", platform.system())
#print("Versão do SO.........:", platform.release())
#print("Versão do Processador:",platform.processor())
#print("Versão do Python.....:", platform.python_version())

#print(datetime.now())

usuario = getpass.getuser()
senha = getpass.getpass("Digite a senha:")

if usuario == 'C.Ortega' and senha == 'oi':
    print("Bem vindo!")
else:
    print("Usuario/Senha incorreto(s)")
