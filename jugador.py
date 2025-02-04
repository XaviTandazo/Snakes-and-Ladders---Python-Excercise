#CLASE JUGADOR
#En este archivo se encuentra la clase del jugador

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = 1  #Todos comienzan en la primer casilla

    def mover(self, espacios):
        nueva_posicion = self.posicion + espacios #Movimiento de la ficha
        if nueva_posicion <= 100:
            self.posicion = nueva_posicion
        else: print(f"Necesitas {100 - self.posicion} para ganar")

    def ha_ganado(self):
        return self.posicion >= 100 #Verificacion si el jugador gana