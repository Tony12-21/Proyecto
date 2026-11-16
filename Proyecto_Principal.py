
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