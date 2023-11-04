"""Con el siguiente diccionario, debes crear un programa que pregunte al usuario 
por un número; el programa debe imprimir el jugador al que hace referencia ese número"""

diccionario_jugadores = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"
}

player_num = int(input("Introduce a football player's number: "))

if player_num in diccionario_jugadores:
    print("The surname of the player with the number", player_num, "is", diccionario_jugadores.get(player_num))
else:
    print("ERROR!! That number is not in the data base, TRY AGAIN")