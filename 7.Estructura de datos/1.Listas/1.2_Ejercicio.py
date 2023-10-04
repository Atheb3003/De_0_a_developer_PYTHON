"""En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]"""
list = [20, 50, "Curso", 'Python', 3.14]

print(list)

list[0] = input("Introduzca un dato a la lista que sustituira el primer lugar: ")
list [1] = input("Introduzca un dato a la lista que sustituira el segundo lugar: ")

print(list)