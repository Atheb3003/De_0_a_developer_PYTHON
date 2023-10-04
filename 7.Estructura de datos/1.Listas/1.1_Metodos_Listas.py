lista = [1, 2, 3, 4, 5, 4, 3, 2, 1, 75, 0]

print(lista)

lista.append(6) 
#.append(d) AGREGA DATOS A UNA LISTA AL FINAL DE ESTA

lista.insert(2, 2.5)
#.inster(x, d) AGREGA DATOS A UNA LISTA EN UNA POSICION EN ESPECIFICO (X = posicion, d = dato)

print(lista.count(1))
#.count(X) CUENTA LA CANTIDAD QUE HAY DE UN DATO ESPECIFICO (X)

print(lista.index(3))
#.index(X) BUSCA EN LA LISTA DONDE SE ENCUENTRA EL DATO (X) Y DEVUELVE SU POSICION EN EL ARRAY. SI HAY MAS DE UN DATO IGUAL UNICAMENTE DEVUELVE LA POISICION DEL PRIMERO QUE SE ENCUENTRE

print(lista.sort())
#.sort() ORDENA LA LISTA DE MANERA ASCENDENTE

print(lista.reverse())
#.reverse() ORDENA LA LISTA DE MANERA DESCENDENTE

lista.pop()
#.pop() ELIMINA EL ULTIMO VALOR DE LA LISTA

lista.remove(75)
#.remove(X) ELIMINA UN DATO EN ESPECIFICO (X) DE LA LISTA

print(lista)