[Proyecto_Principal.py](https://github.com/user-attachments/files/31895160/Proyecto_Principal.py)# Juego de Blackjack
## Contexto

El Blackjack es un juego de cartas en el que el objetivo es conseguir una puntuación lo más cercana posible a 21 sin superar este número. El jugador compite contra el dealer, y quien tenga la puntuación más alta sin pasarse de 21 gana.

Las cartas del 2 al 10 tienen su valor original, mientras que J, Q y K valen 10 puntos. El As puede valer 1 u 11, dependiendo de cuál sea más conveniente para el jugador.

Durante el juego, el jugador puede decidir entre pedir otra carta o quedarse con sus cartas actuales. Si la puntuación del jugador supera 21, pierde automáticamente. Cuando el jugador para de hacer acciones, el dealer juega y finalmente se comparan las puntuaciones para determinar al ganador.

Creo que es un proyecto interesante ya que este me ayudaría mucho con mis habilidades de python en el sentido que no suena demasiado complejo pero tambien tiene muchas variables y cosas en las que me podría ayudar. Personalmente tambien me sentiría más motivado a hacerlo por que me gusta mucho el blackjack pero no soy tan fan de la parte de apostar.

## Algoritmo
[Algoritmo Proyecto Blackjack.pdf](https://github.com/user-attachments/files/31629829/Algoritmo.Proyecto.Blackjack.pdf)

## Codigo
[Uploaddinero = 100
apuesta = 10
puntos = 0

print("Bienvenido al Blackjack")
print("Dinero disponible:", dinero)

apuesta = int(input("Cuanto vas a apostar?: "))

dinero = dinero - apuesta

print("Apostaste:", apuesta)
print("Dinero restante:", dinero)

carta1 = int(input("Introduce el valor de tu primera carta: "))
carta2 = int(input("Introduce el valor de tu segunda carta: "))

puntos = carta1 + carta2

print("Tus puntos son:", puntos)

if puntos == 21:
    print("¡Blackjack!")
elif puntos > 21:
    print("Te pasaste de 21")
else:
    print("Puedes seguir jugando")ing Proyecto_Principal.py…]()
