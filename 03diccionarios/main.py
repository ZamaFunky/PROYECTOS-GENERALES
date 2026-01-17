#DICCIONARIO
#CREAR Y MOSTRAR DICIONARIOS
a={}
print(a)
#CLAVE - VALOR
a={
    "Nombre":"Yuki",
    "Edad":22,
    "Domicilio":"Av. La Palma 125",
    "Telefono:":"4426581542"
}
print(a)

#MODIFICAR UN VALOR DEL DICCIONARIO
a["Edad"]=23
print(a)
print(a["Nombre"])

#BORRAR UN ELEMENTO DEL DICCIONARIO
del a["Edad"]#BORRA EL ELEMENTO QUE PASAMOS COMO PARAMETRO
print(a)
a.pop("Nombre")#BORRA EL ELEMENTO QUE PASAMOS COMO PARAMETRO
print("Borra nombre ",a)
a.popitem()#BORRA EL ULTIMO ELEMENTO
print("Borra el ultimo elemento ",a)
#AGREGAR UN ELEMNTO AL DICCIONARIOA
a["Titulo"]="Ing. en Sistemas"
print(a)

a.keys()#ENTREGA LAS CLAVES
a.values()#ENTREGA LOS VALORES
a.items()#ENTREGA CLAVE - VALOR

#print(a.keys())
for clave in a.keys():
    print(clave)

for valor in a.values():
    print(valor)

for clave, valor in a.items():
    print(clave," - ", valor)

print("----------------------------------------------------------")

print("TRABAJO DE CLASE")

b = [
    {
        "Nombre": "Picasso",
        "Edad": 18,
        "Domicilio": "Av. La Palma 125",
        "Telefono": ["4426157858", "306781250", "24570900"]
    },
    {
        "Nombre": "Newton",
        "Edad": 22,
        "Domicilio": "Av. La Palma 125",
        "Telefono": ["4421581542"]
    },
    {
        "Nombre": "Einstein",
        "Edad": 22,
        "Domicilio": "Av. La Palma 125",
        "Telefono": ["4426581542", "4429998888"]
    }
]

print("LISTA ORIGINAL",b)

nuevo = {}

nuevo["Nombre"] = "Maru"
nuevo["Edad"] = 20
nuevo["Domicilio"] = "Av. La Palma 125"
nuevo["Telefono"] = ["4451253698"]

b.append(nuevo)

print("Modificado",b)


# AGREGAR UN ELEMENTO A NEWTON
b[1]["Telefono"].append("4426781542")
print(b[1])


# BORRAR EL ÚLTIMO ELEMENTO DEL ARREGLO
b.pop()
print("Ultimo elemnto eliminado",b)


# MODIFICAR LA EDAD DE EINSTEIN
b[2]["Edad"] = 30
print("Datos de Einstein",b[2])

# MOSTRAR EL SEGUNDO TELÉFONO DE EINSTEIN
print("Segundo telefono",b[2]["Telefono"][1])

print("----------------------------------------------------------")