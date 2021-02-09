def perguntar():
    return input("O que deseja realizar?\n"+
                 "<I> - Para Inserir um usuario\n"+
                 "<P> - Para Pesquisar um usuario\n"+
                 "<E> - Para Excluir um usuario\n"+
                 "<L> - Para Listar um usuario").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()]= [input("Digite seu nome: ").upper(),
                                                    input("Digite a última data de acesso: "),
                                                    input("Qual a útilma estação acessada: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd_Dicionario.txt", "a") as arquivo:
        for chave,valor in dicionario.items():
            arquivo.write(chave + " : " + str(valor))

def pesquisar(dicionario,nomePesquisa):
    print(dicionario.get(nomePesquisa))

def excluir(dicionario,nomeParaExcluir):
    if dicionario.get(nomeParaExcluir)[0] != nomeParaExcluir:
        print("O usuario "+ nomeParaExcluir +" não esta cadastrado!")
    else:
        print("Usuario: "+ nomeParaExcluir + " excluido com sucesso!")


def listar(dicionario):
    return print(dicionario)