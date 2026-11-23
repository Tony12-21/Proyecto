import random
import archivos

dinero = 100
apuesta = 0
puntos = 0
historial = []


def apostar(dinero):

    apuesta = int(input("Cuanto vas a apostar?: "))

    while apuesta > dinero or apuesta <= 0:
        print("Apuesta no valida")
        apuesta = int(input("Cuanto vas a apostar?: "))

    dinero = dinero - apuesta

    print("Dinero restante:", dinero)

    return dinero, apuesta


def cartas():

    carta = random.randint(1, 11)

    return carta


def dealer():

    cartas_dealer = [cartas(), cartas()]
    puntos_dealer = sum(cartas_dealer)

    while puntos_dealer < 17:
        nueva_carta = cartas()
        cartas_dealer.append(nueva_carta)
        puntos_dealer = sum(cartas_dealer)

    return cartas_dealer, puntos_dealer


seguir = "si"

while seguir == "si" and dinero > 0:

    dinero, apuesta = apostar(dinero)

    cartas_jugador = [cartas(), cartas()]
    puntos = sum(cartas_jugador)

    print("Tus cartas son:", cartas_jugador)
    print("Tus puntos son:", puntos)

    # Turno del jugador
    while puntos < 21:

        pedir = input("Quieres otra carta? (si/no): ").lower().strip()

        if pedir == "si":
            nueva_carta = cartas()
            cartas_jugador.append(nueva_carta)
            puntos = sum(cartas_jugador)

            print("Nueva carta:", nueva_carta)
            print("Tus puntos son:", puntos)

        else:
            break

    # Turno del dealer
    if puntos <= 21:

        cartas_dealer, puntos_dealer = dealer()

        print("\nCartas del dealer:", cartas_dealer)
        print("Puntos del dealer:", puntos_dealer)

    else:
        cartas_dealer = []
        puntos_dealer = 0

    # Resultado de la partida
    if puntos > 21:
        print("Te pasaste de 21")
        resultado = "Perdiste"

    elif puntos_dealer > 21:
        print("El dealer se paso. Ganaste!")
        dinero = dinero + apuesta * 2
        resultado = "Ganaste"

    elif puntos > puntos_dealer:
        print("Ganaste!")
        dinero = dinero + apuesta * 2
        resultado = "Ganaste"

    elif puntos == puntos_dealer:
        print("Empate")
        dinero = dinero + apuesta
        resultado = "Empate"

    else:
        print("Perdiste")
        resultado = "Perdiste"

    print("Dinero disponible:", dinero)

    # Guardar resultados en una matriz
    partida = [cartas_jugador, puntos, cartas_dealer, puntos_dealer, apuesta, resultado, dinero]

    historial.append(partida)

    #Guardar partida en el archivo
    archivos.guardar_partida(partida)

    if dinero > 0:
        seguir = input("Quieres jugar otra ronda? (si/no): ").lower().strip()
    else:
        print("Te quedaste sin dinero")
        seguir = "no"


print("\nHistorial de partidas:")

archivos.leer_partidas()

print("Gracias por jugar Blackjack")
print("Dinero final:", dinero)
