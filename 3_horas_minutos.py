#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

minutos = float(input('Recibe una cantidad de minutos'))

horas = minutos//60
minutos_restantes = minutos%60

print('Quedan',horas,'Horas y', minutos_restantes,'minutos')