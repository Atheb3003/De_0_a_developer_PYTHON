"""Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas"""
vocal = input("Introduca una vocal en minuscula: ")
consonante = input("Introduca una consonante en mayuscula: ")

if len(vocal) == 1 and len(consonante) == 1:
    if vocal in "aeiou" and vocal.isalpha () and consonante.isupper() and consonante not in "AEIOU":
        vocal = vocal.upper()
        consonante = consonante.lower()
        print("{}{}".format(vocal, consonante))
    else:
        print("Hubo un error, introduzca de nuevo los datos de manera correcta.")
