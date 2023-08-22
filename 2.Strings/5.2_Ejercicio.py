#Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r
cadena = "Separado"
nueva_cadena= cadena.replace("", ",")


print(nueva_cadena)

#STRIP QUITA LAS , DEL COMIENZO Y EL FINAL DE LA CADENA
print(nueva_cadena.strip(","))