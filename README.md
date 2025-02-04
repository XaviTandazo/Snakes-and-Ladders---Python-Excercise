# 🎲 Backend de Snakes and Ladders

## Características
- Cada jugador comienza en la casilla **1**.
- En cada turno, un jugador tira un dado (1-6) y avanza esa cantidad de espacios.
- El juego termina cuando un jugador alcanza o supera la casilla **100**.


## 🛠 Instalación y Ejecución
### 1️⃣ Clonar el repositorio
```bash
 git clone https://github.com/tu-usuario/tu-repositorio.git
 cd tu-repositorio
```

### 2️⃣ Ejecutar el juego
Asegúrate de tener **Python 3** instalado y luego ejecuta:
```bash
python main.py
```

## Pruebas Implementadas
El juego ha sido desarrollado siguiendo **User Stories (US)** con pruebas automatizadas mediante `assert`.

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

## 📌 Estructura del Código
```
📂 
│── main.py          # Archivo principal para ejecutar el juego
│── tablero.py       # Contiene la lógica del tablero y los jugadores
│── dado.py          # Clase que simula el lanzamiento de un dado
│── tests.py         # Pruebas automatizadas con assert
│── README.md        
```

**Autor:** [Xavier Sebastián Tandazo Cobo]

