# 🎲 EJERCICIO BAYTEQ: Snakes and Ladders
- El en el ejercicio no se menciona la necesidad de implementar serpientes o escaleras. Se asume que este proyecto sirve como un punto de partida para un posterior desarrollo fiel al concepto del juego.
- El proyecto sigue siendo un juego de tablero, pero sin las características antes mencionadas, puesto que se sigue al margen lo estipulado en el pdf.

## Características
- Cada jugador comienza en la casilla **1**.
- En cada turno, un jugador tira un dado (1-6) y avanza esa cantidad de espacios.
- El juego termina cuando un jugador alcanza o supera la casilla **100**.

## Pruebas Implementadas
### **US 1 - Mover la Ficha en el Tablero**
✅ **UAT1**: La ficha comienza en la casilla 1.

✅ **UAT2**: Si la ficha se mueve **3** espacios desde la casilla 1, termina en la casilla **4**.

✅ **UAT3**: Si la ficha se mueve **3** y luego **4** espacios, termina en la casilla **8**.

### **US 2 - Ganar el Juego**
✅ **UAT1**: Si la ficha está en la casilla **97** y avanza **3** espacios, llega a **100** y gana.

✅ **UAT2**: Si la ficha está en la casilla **97** y avanza **4** espacios, permanece en **97** y **no gana**.

### **US 3 - Movimiento con Dado**
✅ **UAT1**: El resultado del dado está entre **1 y 6**.

✅ **UAT2**: Si el dado muestra un **4**, la ficha avanza **4** espacios.

## 📌 Estructura y Clases del Código
```
📂 
│── main.py          # Archivo principal para ejecutar el juego
│── tablero.py       # Contiene la lógica del tablero y los jugadores
│── dado.py          # Clase que simula el lanzamiento de un dado
│── tests.py         # Pruebas automatizadas con assert
│── README.md        
```

Xavier Sebastián Tandazo Cobo

