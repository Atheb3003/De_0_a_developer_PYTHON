""" EL DEBANADO DE STRINGS (O SUBCADENA) CONSISTE EN DIVIDIR UNA CADENA
YA SEA POR FRAGMENTOS UNICOS O POR CONJUNTOS """

cadena = "Esto es una cadena"

"""LA FUNCION LEN NOS DA EL TAMAÑO DE UNA CADENA"""

print(len(cadena)) 

# Con los corchetes pordemos coger unicamente una parte o un conjunto de la cadena

# Ejemplo con una única parte
print(cadena[5])

# Ejemplo Para un conjunto
print(cadena[5 : 19])

# Si dejamos vacio cualquiiera de los dos numeros, python considera que le estamos indicando que comience en el principio o acabe en el final
print(cadena[ : 5])
print(cadena[10 : ])
