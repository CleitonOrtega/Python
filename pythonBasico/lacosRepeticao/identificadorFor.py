tabuada=int(input("Digite o numero para imprimir a tabuada dele: "))
print("__________ Tabuada do numero",tabuada,"__________")
for valor in range(1,11,1):
    print(str(tabuada) + " X " + str(valor) + " = " + str((tabuada*valor)))