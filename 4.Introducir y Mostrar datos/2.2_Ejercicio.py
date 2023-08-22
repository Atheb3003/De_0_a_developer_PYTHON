"""Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>"""

nombre = input("Introduzca su nombre: ")
edad = int(input("Introduzca su edad: "))
sexo = input("¿Es hombre o mujer?: ")

print("Te llamas: {}\nTu edad es: {}\nEres: {}".format(nombre, edad, sexo))