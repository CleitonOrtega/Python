from Dicionario.funcoesDicionario import *

usuarios = {}
opcao = perguntar()
while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        inserir(usuarios)
    elif opcao == 'P':
        pesquisar(usuarios,input("Digite o nome a ser pesquisado: ").upper())
    elif opcao == 'E':
        excluir(usuarios,input("Digite o nome a ser excluido: ").upper())
    elif opcao == 'L':
        listar(usuarios)

    opcao = perguntar()