[Proyecto_Principal.py](https://github.com/user-attachments/files/34895336/Proyecto_Principal.py)
## Contexto

El Blackjack es un juego de cartas en el que el objetivo es conseguir una puntuación lo más cercana posible a 21 sin superar este número. El jugador compite contra el dealer, y quien tenga la puntuación más alta sin pasarse de 21 gana.

Las cartas del 2 al 10 tienen su valor original, mientras que J, Q y K valen 10 puntos. El As puede valer 1 u 11, dependiendo de cuál sea más conveniente para el jugador.

Durante el juego, el jugador puede decidir entre pedir otra carta o quedarse con sus cartas actuales. Si la puntuación del jugador supera 21, pierde automáticamente. Cuando el jugador para de hacer acciones, el dealer juega y finalmente se comparan las puntuaciones para determinar al ganador.

Creo que es un proyecto interesante ya que este me ayudaría mucho con mis habilidades de python en el sentido que no suena demasiado complejo pero tambien tiene muchas variables y cosas en las que me podría ayudar. Personalmente tambien me sentiría más motivado a hacerlo por que me gusta mucho el blackjack pero no soy tan fan de la parte de apostar.

## Algoritmo
[Algoritmo Proyecto Blackjack.pdf](https://github.com/user-attachments/files/31629829/Algoritmo.Proyecto.Blackjack.pdf)

## Avance 2 Codigo

import random

dinero = 100
apuesta = 0
puntos = 0
historial = []


def bienvenida():
    nombre = input("Como te llamas?: ")
    nombre = nombre.strip().title()

    print("Bienvenido a Blackjack", nombre)
    print("Dinero disponible:", dinero)

    return nombre


def apostar(dinero):

    apuesta = int(input("Cuanto vas a apostar?: "))

    while apuesta > dinero or apuesta <= 0:
        print("Apuesta no valida")
        apuesta = int(input("Cuanto vas a apostar?: "))

    dinero = dinero - apuesta

    print("Dinero restante:", dinero)

    return dinero, apuesta


def cartas():

    cartas_jugador = [random.randint(1, 11), random.randint(1, 11)]

    puntos = cartas_jugador[0] + cartas_jugador[1]

    return cartas_jugador, puntos


nombre = bienvenida()

seguir = "si"

while seguir == "si" and dinero > 0:

    dinero, apuesta = apostar(dinero)

    cartas_jugador, puntos = cartas()

    print("Tus cartas son:", cartas_jugador)
    print("Tus puntos son:", puntos)

    if puntos == 21:
        print("Blackjack")
        resultado = "Blackjack"

    elif puntos > 21:
        print("Te pasaste de 21")
        resultado = "Perdiste"

    else:
        print("Puedes seguir jugando")
        resultado = "Puedes continuar"

    # Guardar resultados en una matriz
    historial.append([nombre, cartas_jugador[0], cartas_jugador[1], apuesta, puntos, resultado])

    seguir = input("Quieres jugar otra ronda? (si/no): ").lower().strip()


print("\nHistorial de partidas:")

for partida in historial:
    print(partida)

print("Gracias por jugar Blackjack")
print("Dinero final:", dinero)
