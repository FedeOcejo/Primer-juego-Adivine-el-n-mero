import random
numero = random.randint(0,99)
respuesta = int (input ('introduce un numero entre 0 y 99'))
intentos= 0

while respuesta != numero:
    if respuesta < numero:
            print ("Muy Pequeño")
            intentos = intentos + 1
            respuesta = int (input ('introduce un numero entre o y 99'))
    if respuesta > numero:
            print ("Muy Grande")
            intentos = intentos + 1
            respuesta = int (input ('introduce un numero entre o y 99'))
    if respuesta == numero:
            print ("Felicidades")
            intentos = intentos + 1
            print ("Lo has conseguido en" ,intentos, "intentos")