#CLASE TABLERO
#En este archivo se encuentra la clase del tablero de juego
from dado import Dado
from jugador import Jugador 

class Tablero:
    def __init__(self):
        self.jugadores = [] #Array de jugadores
        self.dado = Dado()

    def agregar_jugador(self, nombre):
        self.jugadores.append(Jugador(nombre)) #Agregar jugadores al array

    def jugar_turno(self, jugador): #Simula un turno de un jugador
        tirada = self.dado.tirar() #Tira dado
        print(f"{jugador.nombre} tiró el dado. Número: {tirada}.")
        jugador.mover(tirada) #Se mueve segun el numero q salga en el dado
        print(f"{jugador.nombre} se mueve a casilla {jugador.posicion}.\n")
        if jugador.ha_ganado(): #Condicional si el jugador gana con la funcion de la clase Jugador
            print(f"{jugador.nombre} ha ganado.\n")
            return True  #El juego termina
        else: 
            return False  
