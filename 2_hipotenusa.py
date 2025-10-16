#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

c1 = float(input("¿Cuánto mide el primer cateto? "))
c2 = float(input('¿Cuanto mide el segundo cateto?'))

from math import sqrt

h = sqrt((c1**2)+(c2**2))


print('La raiz cuadrada es',h)