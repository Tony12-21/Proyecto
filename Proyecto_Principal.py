dinero = 100
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
    print("Puedes seguir jugando")