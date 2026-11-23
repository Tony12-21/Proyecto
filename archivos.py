def guardar_partida(partida):

    archivo = open("historial_blackjack.txt", "a")
    archivo.write(str(partida) + "\n")
    archivo.close()


def leer_partidas():

    try:
        archivo = open("historial_blackjack.txt", "r")
        print(archivo.read())
        archivo.close()

    except FileNotFoundError:
        print("Todavia no hay partidas guardadas")
