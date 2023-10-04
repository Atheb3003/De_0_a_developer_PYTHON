#Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
num = int(input("Introduzca un numero para devolver su valor absoluto: "))
if num >= 0:
    print(num)
else:
    num = num * (-1)
    print(num)