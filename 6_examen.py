# Escribir un programa para calcular la nota final de un examen, considerando que:

#Cada respuesta correcta suma 5 puntos.
#Cada respuesta incorrecta suma -1 puntos.
#Cada respuesta en blanco suma 0 puntos.
#Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.

aciertos = float(input('Respuestas correctas:'))
fallos = float(input('Respuestas incorrectas:'))
blanco = float(input('Respuestas en blanco:'))

respuestas = (aciertos + fallos + blanco)*5

puntos_aciertos = aciertos*5
puntos_fallos = fallos*(-1)
puntos_blanco = blanco * 0

nota_previa = puntos_aciertos +puntos_fallos + puntos_blanco

nota_final = (nota_previa/respuestas)*10


print('La nota final es de:', nota_final)

