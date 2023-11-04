diccionario = {1 : 2, 2 : 3, 3 : 4, "nombre" : "paco"}

print(diccionario)

diccionario.pop("nombre") #ELIMINA EL ELEMENTO LIGADO A LA CLAVE QUE INTRODUZCAMOS EN ()
print(diccionario)

print(diccionario.get(2))#LLAMA AL VALOR DE LA LLAVE QUE INTRODUZCAMOS EN ()

diccionario.setdefault("apellido","Gomez") #AÑADE UNA NUEVA CLAVE CON SU VALOR, ES UNA MANERA DE AÑADIR ELEMENTOS AL DICCIONARIO CON METODOS
print(diccionario)

diccionario_2 = {"usuario" : "Pepito35", "contraseña" : "1234h"}
diccionario.update(diccionario_2) #FUSIONA DOS DICCIONARIOS
print(diccionario)

diccionario.copy() #GENERA UNA COPIA DEL DICCIONARIO
print(diccionario)

diccionario.clear()
print(diccionario) #ELIMINA TODO EL DICCIONARIO

