#HAY DOS FUNCIONES QUE MODIFICAN EL TIPO DE DATO DE UNA VARIABLE NUMERICA

num1 = 42
num2 = 69.99

print("El valor de num1 original es: ")
print(num1)
print("El valor de num2 original es: ")
print(num2)

#LA FUNCION FLOAT TRANSFORMA A UN INT EN UN FLOAT
print("El tipo original de num1 es: ")
print(type(num1))
print("Su tipo tras usar float es: ")
print(type(float(num1)))
print("El valor de num1 modificado es: ")
print(float(num1))

# LA FUNCI'ON INT VUELVE A UN FLOAT EN INT (LO HACE SIN APROXIMAR)
print("El tipo original de num2 es: ")
print(type(num2))
print("Su tipo tras usar float es: ")
print(type(int(num2)))
print("El valor de num2 modificado es: ")
print(int(num2))