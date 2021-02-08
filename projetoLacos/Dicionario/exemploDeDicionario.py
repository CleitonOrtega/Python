usuarios = {}
print(usuarios)

usuarios= {
    "Chaves" : ["Chaves do 8","24/12/2017","Recep_01"],
    "Quico" : ["Quico das Flores","20/12/2017","Raiox_03"]
}
print(usuarios)

usuarios["Florinda"] = ["Dona florinda","24/12/2017","Raiox_01"]
print(usuarios)

print(usuarios.get("Quico"))