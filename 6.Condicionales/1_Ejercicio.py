#Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal
letra = str(input("Introduzca una letra: "))
letra = letra.lower()
if letra in ["a", "e", "i", "o", "u"]:
    print("Tu letra es una vocal")
else:
    print("Tu letra NO es una vocal")