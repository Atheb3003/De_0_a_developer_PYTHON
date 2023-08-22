"""Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion> (FORMULA DE ECUACIONES DE SEGUNDO GRADO)”"""
a = int(input("Introduzca el valor de a: "))
b = int(input("Introduzca el valor de b: "))
c = int(input("Introduzca el valor de c: "))

raiz = b**2 - 4*a*c

if raiz < 0:
    print("La ecuación no tiene solución real.")
else:
    sol_1 = (-b + (raiz ** 0.5)) / (2 * a)
    sol_2 = (-b - (raiz ** 0.5)) / (2 * a)

    if sol_1 == sol_2:
            print("La ecuacion tiene una unica solucion. La solucion es = ", sol_1)
    else:
            print("La ecuacion tiene dos soluciones.")
            print("La primera solucion es = ", sol_1)
            print("La segunda solucion es = ", sol_2)

