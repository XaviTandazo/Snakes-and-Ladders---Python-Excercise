#CLASE DADO
#En este archivo se encuentra la clase del dado
import random

class Dado:
    def tirar(self):
        return random.randint(1,6) #El rango de los número es 6, para simular las posibilidades en un dado de 6 caras.