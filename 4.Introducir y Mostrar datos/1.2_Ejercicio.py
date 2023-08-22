"""Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final"""

P1 = float(input("Introduzca la calificacion de la primera practica: "))
P2 = float(input("Introduzca la calificacion de la segunda practica: "))
P3 = float(input("Introduzca la calificacion de la tercera practica: "))
PP = ((P1 + P2 + P3)/3)
EP = float(input("Introduzca la calificacion del examen parcial: "))
EF = float(input("Introduzca la calificacion del examen final: "))

MED = ((PP + EF*3 + EP*2)/6)
print("Su nota media es igual a {}".format(MED))