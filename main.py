from tablero import Tablero
from jugador import Jugador
from dado import Dado

if __name__ == "__main__":
    tablero = Tablero()

    num_jugadores = int(input("Ingrese el número de jugadores: "))
    
    for i in range(1, num_jugadores + 1):
        nombre = input(f"Nombre del jugador {i}: ")
        tablero.agregar_jugador(nombre)

    juego_terminado = False
    j = 1

    while not juego_terminado: #Mientras juego_terminado no sea True, este proceso se repite.
        print (f"Turno {j}: ")
        for jugador in tablero.jugadores: #Cada jugador obtiene su turno en orden
            juego_terminado = tablero.jugar_turno(jugador)
            if juego_terminado:
                break
            else: j = j+1