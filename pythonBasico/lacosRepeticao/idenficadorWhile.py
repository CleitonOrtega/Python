numero=int(input("Digite um numero: "))
print("Os numeros que faltam para chegar em 100 são: ")
while numero <= 100:
    print("\t" + str(numero))
    numero = numero + 1
print('Laço encerrado...')