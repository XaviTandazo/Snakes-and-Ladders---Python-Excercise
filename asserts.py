from tablero import Tablero
from jugador import Jugador
from dado import Dado

# Pruebas manuales de las historias de usuario
jugador_test =Jugador("Test")
    
#Debe iniciar en 1
assert jugador_test.posicion == 1, "no inicia en 1"
#Debe llegar a 4 y a 9
jugador_test.mover(3)
assert jugador_test.posicion == 4, "no llegó a 4"
jugador_test.mover(5)
assert jugador_test.posicion == 9, "no llegó a 9"

#Ganar el juego
jugador_test.posicion = 97
jugador_test.mover(3)

#jugar_turno debe retornar True
assert jugador_test.ha_ganado(), "no se cambió a true"

#No se debe mover porque se pasa de 100
jugador_test.posicion = 97
jugador_test.mover(4)
assert jugador_test.posicion == 97, "se pasó de 100"