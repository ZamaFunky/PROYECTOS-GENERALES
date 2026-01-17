print("Hola mundo con python")
#LISTAS
a=[]
print(a)
a=["Q:3", "Whats urname?","chetos"]
print(a)
print(a[1])

#MODIFICAR LISTAS
a[0]="Prissma"
print(a)
a.append("kuason")
print(a)
a.insert(1,"Like")#AGREGA UN ELEMENTO EN LA POSICION 1
print(a)

#BORRAR UN ELEMENTO DE LA LISTA
a.pop()#DElimina el ultimo elemento de la lista
print(a)
a.remove("chetos")#Borra el elemento que pasamos como parametro
print(a)
a.clear()#Borra todos los elementos, pero no la lista
print(a)

#FUNCIONES
a=["OLA","Nice","OLA","Prisma"]
print(a)
#CONTAR UN ELEMENTO DE LA LISTA
print(a.count("Prissma"))
#CONTAR TODOS LOS ELEMENTOS DE LA LISTA
print(len(a))
#CONTAR LA POSICION QUE ESTA UN ELEMENTO
print(a.index("OLA"))
#ORDENAR DATOS NUMERICOS
a=[8,5,3,10]
a.sort()
print(a)