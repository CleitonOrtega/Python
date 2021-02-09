#Para incrementar uma nova linha no arquivo use a notação "a"
#with open("primeiroManipulado.txt", "a") as arquivo:
#    arquivo.write("\nAdicionando a segunda linha")

#Para ler oque esta no arquivo
with open("primeiroManipulado.txt", "r") as arquivo:

#Para ler linha a linha do que esta no arquivo
    for linha in arquivo.readlines():
        print(linha)

#Para ler todo o arquivo
    conteudo = arquivo.read()
    print(conteudo)