"""En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa 
que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario,
se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua",
 "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", 
 "Venezuela": "Caracas", "España": "Madrid"}"""

diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua",
 "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", 
 "Venezuela": "Caracas", "España": "Madrid"}

user = input("Introduce a country: ")
if user in diccionario:
    print("The capital city of", user, "is", diccionario.get(user))
else:
    print("ERROR, The name of the country is wrong or that country is not in the data base")