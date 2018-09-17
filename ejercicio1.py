import random

contador = 0
encontrado = 0
rando = random.randrange(5)

while contador < 10 and encontrado == 0:
    numero = int(input("Escriba un numero "))
    if numero < rando:
        print("El numero es menor")
    elif numero > rando:
        print("El numero es mayor")
    else:
        print("Has acertado el numero!")
        encontrado = 1


    contador += 1

print("Fin del programa")