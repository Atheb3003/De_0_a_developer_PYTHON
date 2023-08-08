#Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:
cadena = "Te quiero solo como amigo"

#• Imprima los tres últimos caracteres.
print(len(cadena)) #PARA SABER EL NUMERO DE CARACTERES QUE TIENE LA CADENA

print(cadena[22 : ])

"""OTRA OPCION SERIA"""
print(cadena[-3 : ]) 
#Aqui le estoy diciendo que empiece por el tgercer caracter empezando por el final y que termine en el final

#• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
print(cadena[: : 2])
#CON ESTE COMANDO LE DIGO QUE IMPRIMA CADA DOS CARACTERES

#• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
print(cadena[: : -1])
"""CON ESTE COMANDO LE ESTOY DICIENDO QUE ME IMRPIMA EL CARCATER ANTERIOR CADA VEZ, AL SER 
EL PRIMER CARACTER EL MENOR LE DA LA VUELTA A LA CADENA Y COMIENZA POR EL FINAL"""

#• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
print(cadena + cadena[: : -1])