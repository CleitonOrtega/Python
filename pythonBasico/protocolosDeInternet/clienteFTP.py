from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario = input("Digite o nome de usuario: ")

senha = input("Digite a senha de usuario: ")

ftp.login(usuario,senha)

print("Diretorio atual de trabalho: ", ftp.pwd())

ftp.cwd('pub')

print("Diretorio corrente: ", ftp.pwd())

print(ftp.retrlines('LIST'))

ftp.quit()