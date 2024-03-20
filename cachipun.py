# correos yesseniamillar@gmail.com / ing.cfurrutia@gmail.com

import random
print('   ')
# Opciones del juego 
opciones = ["piedra", "papel", "tijera"]

# Jugador ingresa su opción
jugador = input("Humano, ingresa piedra, papel o tijera: ")

# Validación
if jugador != "piedra" and jugador != "papel" and jugador != "tijera":
    print("Opción inválida. Vuelva a ingresar una opción válida: piedra, papel o tijera")
    jugador = input("Humano, ingresa piedra, papel o tijera: ")

# Computadora ingresa su opción
computadora = random.choice(opciones)
print("La computadora ha elegido:", computadora)

# Comparación de opciones y determinación del Ganador El Hombre o la Computadora.
if jugador == computadora:
    print('Esto es un empate. Tu elijiste, La maquina aun no supera a su creador.')
elif (jugador == 'piedra' and computadora == 'tijera') or (jugador == 'papel' and computadora == 'piedra') or (jugador == 'tijera' and computadora == 'papel'):
    print('¡Humano, tú me ganaste!')
else:
    print('¡Humano, perdiste frente a la máquina!')
    
print('   ')



