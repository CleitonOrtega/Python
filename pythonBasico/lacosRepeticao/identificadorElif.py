nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
doencaInfectocontagiosa=input("Suspeita de doença infectocontagiosa?: ").upper()
if  doencaInfectocontagiosa=="SIM":
    print("O paciente ", nome ," deve ser direcionado a sala de espera reservada!")
elif idade >= 65:
    print("O paciente ", nome ," Possui atendimento prioritario!")
else:
    print("O paciente ", nome , " não possui atendimento prioritario!")