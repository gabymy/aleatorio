import random


def adivina_el_numero(x):
    print("======================")
    print("Bienvenido(a) al Juego")
    print("======================")
    print("Adivina el numero que estoy pensando.....")

    num_aleatorio = random.randint(1, x)
    prediccion = 0

    while prediccion != num_aleatorio:
        prediccion = int(input(f"adivina un numero entre 1 y {x}: "))

        if prediccion < num_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeño")
        elif prediccion > num_aleatorio:
            print("Intenta otra vez. Este nmero fue muy alto.")

    print(f"felicitaciones!!!! ADIVINASTE!!!")


adivina_el_numero(10)
