
opcao=input("Digite o codigo do programa que deseja acessar (Vetor simples - 1 ou Multiplos vetores - 2): ")

while opcao=='1' or opcao=='2':
    if opcao=='1':
        inventario = []
        resposta = 'S'
        equipamentos = []
        valores = []
        seriais = []
        departamentos = []
        while resposta == 'S':
            inventario.append(input("Equipamento: "))
            inventario.append(float(input("Valor: ")))
            inventario.append(int(input("N° Serial: ")))
            inventario.append(input("Departamento: "))
            resposta = input("S para continuar no programa 1... Deseja continuar?: ").upper()
        for elemento in inventario:
            print(elemento)

    if opcao=='2':
        inventario = []
        resposta = 'S'
        equipamentos = []
        valores = []
        seriais = []
        departamentos = []

        while resposta == 'S':
            equipamentos.append(input("Equipamento: "))
            valores.append(float(input("Valor: ")))
            seriais.append(int(input("N° Serial: ")))
            departamentos.append(input("Departamento: "))
            resposta=input("Digite S para continuar no programa N° 2").upper()
        for indice in range (0,len(equipamentos)):
            print("\nEquipamento:\t",(indice+1))
            print("Nome........: ", equipamentos[indice])
            print("Valor.......: ", valores[indice])
            print("Serial......: ", seriais[indice])
            print("Departamento: ", departamentos[indice])

    opcao=input("\nDigite o codigo do programa que deseja acessar (Vetor simples - 1 ou Multiplos vetores - 2 ou qualquer caracter para sair do programa!): ")

print("Obrigado por utilizar meu programa tenha um bom dia!")









