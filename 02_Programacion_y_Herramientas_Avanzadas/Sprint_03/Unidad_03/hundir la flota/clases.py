# Vamos a establecer las diferentes clases

import numpy as np

class Barco:

    listabarcos = {}
    orientación= ["N","S","E","O"]

    def __init__(self, nombre, tamaño, cantidad):
        self.nombre = nombre
        self.tamaño = tamaño
        self.cantidad = cantidad
        self.impactos = 0
        
# tenemos los siguientes barcos
# 4 barcos de 1 posición de eslora = Destructor
# 3 barcos de 2 posiciones de eslora = Submarino
# 2 barcos de 3 posiciones de eslora =Acorazado
# 1 barco de 4 posiciones de eslora = Portaaviones
    
    def posicioninicial(self.cantidad):
        coordenadas=[]
        for i in range(self.cantidad):
            fila=np.random.randint(0,10)
            columna=np.random.randint(0,10)
            coordenadas.append((fila,columna))
        return coordenadas

destructor = Barco("Destructor", 1, 4)
Submarino = Barco("Submarino", 2, 3)
Acorazado = Barco("Acorazado", 3, 2)
Portaaviones = Barco("Portaaviones", 4, 1)        



