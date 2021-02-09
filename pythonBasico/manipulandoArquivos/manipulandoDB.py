baseDados = []
with open("car.data", "r") as arquivo:
    for registro in arquivo.readlines():
        baseDados.append(registro.split(","))

print(baseDados)

print(baseDados[0][0] + " e "+ baseDados[0][2])