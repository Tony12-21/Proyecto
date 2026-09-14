dinero = 100
apuesta = #input
puntos = 0


def bienvenida():
    print("Bienvenido a Blackjack")
    print("Dinero disponible:", dinero)


def apostar(dinero,apuesta):

    apuesta = int(input("Cuanto vas a apostar?: "))
    dinero = dinero - apuesta

    print("Dinero restante:", dinero)

def cartas(Puntos):
    carta1 = #valor de carta random del 1-11
    carta2 = #valor de carta random del 1-11
    puntos = carta1 + carta2

bienvenida()
apostar()
cartas()

print("Tus puntos son:", puntos)

if puntos == 21:
    print("Blackjack")

elif puntos > 21:
    print("Te pasaste de 21")

else:
    print("Puedes seguir jugando")