#Matriz (Variable especial que puede contener mas de un valor a la vez)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print(thislist)

vegetallist = ['tomate', "papa", "coliflor", "zanahoria", "cebolla"]
print(len(vegetallist))

paises = ["El Salvador", "Guatemala", "Costa Rica", 
"Panama", "Honduras", "Nicaragua" ]
print(len(paises))
print(paises)

listas = [3, 4, 5, 6, 7, 8, 3, 3, 3,]
print(listas)
print(len(listas))
print('\n')

#Agregar elementos a la lista [] = lista
thislist.append("Jocote")
thislist.append("fresa")
print(thislist)
print('\n')
#Agregar una lista vacia
emptyList = []
print(emptyList)
emptyList.append("Objeto nuevo")
print(emptyList)
print('\n')
#diferentes tipos de variable en una lista aun un lista dentro de una lista
list4 = ["abe", 34, True, 10, "male"]
print(type(list4[0]))
print(type(list4[1]))
print(type(list4[2]))
print(type(list4[0]))

list5 = ["el salvador", "mango", 0]
list5.append(list4)
print(list5)
print('\n')

#Acceso a items de la lista
frutas = ["papaya", "jocote", "fresa", "melon", "uva"]
print(frutas[3])
print(frutas[-2])
print('\n')

#desempacar objetos de la lista
fruta1, fruta2, *sobran = frutas
print(fruta1)
print(fruta2)
print(sobran)

numTest = [1,2,3,4,5,6,7,8,9,10,11,12,13]
n1, n2, *nVarios, nPenultimo, nUltimo = numTest #accesar a la informacion puntual
print(n1)
print(n2)
print(nVarios)
print(nPenultimo)
print(nUltimo)

numTest2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]
nInicio, *ncentrales, nUltimo  = numTest2
print(nInicio)
print(2*ncentrales)
print(nUltimo)
print('\n')

#Slicing podemos imprimir en base a indices al igual que los de corte
frutas = ["papaya", "jocote", "fresa", "melon", "uva"]
todoFruta = frutas[2:4]
print(todoFruta)
pruebaFrutas = frutas[0:]
print(pruebaFrutas)
slice1 = frutas[1:3]
print(slice1)
slice2 = frutas[2:4]
print(slice2)
print("fresa" in frutas)
print("melon" in frutas)
frutas = ["manzana", "banana", "naranja", "pera", "uva", "kiwi", "sandía", "mango", "melón", "fresa","papaya", "piña", "cereza", "limón", "granada", "frambuesa", "mandarina", "durazno", "coco", "ciruela"]

for fruta in frutas:
    if fruta == 'papaya':
        print('si hay')
    else:
        print('no hay')
print('\n')
#Insertar elementos en una lista
frutas.insert(3,"jocote")
print ('jocote' in frutas)
print(frutas)
print('\n')
#Eliminar elementos de una lista
frutas.remove("banana")
print(frutas)
print ('banana' in frutas)
print('\n')
#eliminar con una lista metodo pop()
print(frutas)
print(len(frutas))
frutas.pop(0)
print(frutas)
print(len(frutas))
print('\n')
#Eliminar con metodo del()
del frutas [4:9]
print(frutas)
print(len(frutas))
del frutas[:]
print(frutas)
print(len(frutas))
print('\n')
#limpiar items de listas metodo clear
frutas = ["manzana", "banana", "naranja", "pera", "uva", "kiwi", "sandía", "mango", "melón", "fresa","papaya", "piña", "cereza", "limón", "granada", "frambuesa", "mandarina", "durazno", "coco", "ciruela"]
frutas.clear()
frutas.append("limon")
print(frutas)
print('\n')
#Copiar listas
#Convinar una lista
frutas.extend(paises)
print(frutas)
print('\n')
#Contando elementos de una lista metodo extend
frutas.append(1)
frutas.append(1)
frutas.append(1)
print(frutas.count(1))
print(frutas)
print('\n')
#Cambiar orientacion de una lista metodo reverse
frutas.reverse()
print(frutas)
print('\n')
#Ordenar lalista por orden Alfabetico, modifica lalista a ese orden
print(paises)
paises.sort()
print(paises)
print('\n')

#Tuplas python (es inmutable, lista fija) puedes poner elementos del mismo valor representados asi ()
miPrimeraTuple = ("manzana", "coco", "fresa", "uva", "cereza")
print(miPrimeraTuple)
print(type(miPrimeraTuple))
print(miPrimeraTuple[2])
#Si se puede hacer slicing (sub conjuntos de tuples)
tl11 = miPrimeraTuple[0:3]
print(tl11)
#Cambiando tuples a listas
segundaTuple = list(miPrimeraTuple)
print(type(segundaTuple))
print(segundaTuple)
#agregar siendo ya una lista
segundaTuple.append("papaya")
print(segundaTuple)
#Cambiando lista a Tuple
terceraTuple = tuple(segundaTuple)
print(type(terceraTuple))
print(terceraTuple)
#Unir Tuplas
cuartaTuple = miPrimeraTuple + terceraTuple
print(type(cuartaTuple))
print(cuartaTuple)
#Borra tuplas al usar del
del cuartaTuple
print('\n')

#set o conjuntos (elementos bien definidos, sin dobles estos e eliminan) representado asi {}
animales = {"gato", "perro", "aguila", "rana", "elefante", "leon", "rana"}
print(animales)
print(len(animales)) #Borra elementos repetidos, tengo 7 y identifica 6
#Agregar elementos en los Sets con el metodo (.add) o varios con el metodo (.update)
animales.add("escorpion")
print(animales)
animales2 = ("bayena", "tigre", "pantera")
animales.update(animales2)
print(animales)
animales.add("hipopotamo")
print(animales)
#Eliminar elementos en un set
animales.remove("hipopotamo")
print(animales)
animales.pop()
print(animales)
animales.clear()
animales.add("Gato")
print(animales)
#Union de conguntos
animales3 = {"pajaro", "Koala"}
animales4 = animales.union(animales3)
print(animales4)
#convertir list a set
list11 = [1, 2, 3, 4, 5, 6, 7]
Set1 = set(list11)
print(type(list11))
print('\n')

#Dictionary o diccionarios orden de (clave : valor)
myfamily = {
    "childl" : {
    "name" : "Emil",
    "year": 2004
    },
    "child2" : {
    "name" : "Tobias",
    "year" : 2007
    },
    "child3" : {
    "name" : "Linus",
    "year" : 2011
    }
}
print(myfamily["child2"])
myfamily["City"] = "Soya"
print(myfamily)
myfamily.pop ("City")
print(myfamily)

