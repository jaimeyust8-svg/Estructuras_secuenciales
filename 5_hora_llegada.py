#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
#Escribir un programa que determine la hora de llegada a la ciudad B.

HH = float(input('Hora de salida: '))
MM = float(input('Minutos de salida: '))
SS = float(input('Segundos de salida: '))

T = float(input('Tiempo en llegar a la otra ciudad en sgundos: '))

salida_segundos = HH*3600 + MM*60 + SS

llegada = salida_segundos + T

hora_llegada = llegada//3600
minutos_llegada = (llegada%3600)//60
segundos_llegada = llegada%60

print('Llego a las',hora_llegada,'h',minutos_llegada,'m',segundos_llegada,'s')
