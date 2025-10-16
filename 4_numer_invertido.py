#Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

number = int(input('¿Dame un número de dos cifras?'))

unidad_1 = abs(number)//10  #Calcula la primera unidad
unidad_2 = abs(number)%10   #Calcula la segunda unidad

numero_invertido = unidad_2*10 + unidad_1

print(numero_invertido)