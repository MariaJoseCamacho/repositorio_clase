""" 
Vamos a establecer las diferentes clases
"""
import numpy as np
import random
class Barco:

    listabarcos = {}
    orientación= ["N","S","E","O"]

    def __init__(self, nombre, tamaño, cantidad):
        self.nombre = nombre
        self.tamaño = tamaño
        self.cantidad = cantidad
        self.impactos = 0
        self.posicion = self.posicioninicial()
        
# tenemos los siguientes barcos
# 4 barcos de 1 posición de eslora = Destructor
# 3 barcos de 2 posiciones de eslora = Submarino
# 2 barcos de 3 posiciones de eslora =Acorazado
# 1 barco de 4 posiciones de eslora = Portaaviones
    
    def posicioninicial(self):
        self.coordenadas=[]
        for i in range(self.cantidad):
            fila=np.random.randint(0,10)
            columna=np.random.randint(0,10)
            coordenada = (fila,columna)
            if coordenada not in self.posicion:
                self.coordenadas.append((coordenada))
        return self.coordenadas
    
    def coloca_barco(tablero, barco):
        nummaxfilas = tablero.shape[0]
        nummaxcolum = tablero.shape[1]
        tablerotemp = tablero.copy()
        for pieza in barco.cantidad:
            fila = barco.coordenadas[0]
            columna = barco.coordenadas[1]
            if fila<0 or fila>nummaxfilas:
                print(f"No puedo poner la pieza{pieza}, se sale del tablero")
                return False
            if columna>0 or columna>nummaxcolum:
                print(f"No puedo poner la pieza{pieza} porque sale del tablero")
                return False
            if tablero[pieza] == "0" or tablero[pieza]=="X":
                print(f"Hay otro barco en este sitio")
                return False
            tablerotemp[pieza]="O"
        return tablerotemp

destructor = Barco("Destructor", 1, 4)
Submarino = Barco("Submarino", 2, 3)
Acorazado = Barco("Acorazado", 3, 2)
Portaaviones = Barco("Portaaviones", 4, 1)      


class Tablero:

    def creatablero (lado=10):
        return np.full((lado, lado)," " )
    
    def colocabarcojp(barco):
        orientación= ["N","S","E","O"]
        colocar= posicioninicial()
        newori=np.random.choice(orientación)
        fila, columna = colocar[0]
        if newori == "N" and fila - (barco.cantidad - 1) >= 0:
            for i in range(barco.cantidad):
                if tablerojp[fila - i, columna] != " ":
                    return "Espacio ocupado, intenta de nuevo."
            for i in range(barco.cantidad):
                tablerojp[fila - i, columna] = "O"

        elif newori == "S" and fila + (barco.cantidad - 1) < 10:
            for i in range(barco.cantidad):
                if tablerojp[fila + i, columna] != " ":
                    return "Espacio ocupado, intenta de nuevo."
            for i in range(barco.cantidad):
                tablerojp[fila + i, columna] = "O"

        elif newori == "E" and columna + (barco.cantidad - 1) < 10:
            for i in range(barco.cantidad):
                if tablerojp[fila, columna + i] != " ":
                    return "Espacio ocupado, intenta de nuevo."
            for i in range(barco.cantidad):
                tablerojp[fila, columna + i] = "O"

        elif newori == "O" and columna - (barco.cantidad - 1) >= 0:
            for i in range(barco.cantidad):
                if tablerojp[fila, columna - i] != " ":
                    return "Espacio ocupado, intenta de nuevo."
            for i in range(barco.cantidad):
                tablerojp[fila, columna - i] = "O"

        return tablerojp

    def colocabarcoCPU(barco):
            orientación= ["N","S","E","O"]
            colocar= posicioninicial()
            newori=np.random.choice(orientación)
            fila, columna = colocar[0]
            if newori == "N" and fila - (barco.cantidad - 1) >= 0:
                for i in range(barco.cantidad):
                    if tableroCPU[fila - i, columna] != " ":
                        
                for i in range(barco.cantidad):
                    tableroCPU[fila - i, columna] = "O"
                    

            elif newori == "S" and fila + (barco.cantidad - 1) < 10:
                for i in range(barco.cantidad):
                    if tableroCPU[fila + i, columna] != " ":
                        
                for i in range(barco.cantidad):
                    tableroCPU[fila + i, columna] = "O"

            elif newori == "E" and columna + (barco.cantidad - 1) < 10:
                for i in range(barco.cantidad):
                    if tableroCPU[fila, columna + i] != " ":
                        
                for i in range(barco.cantidad):
                    tableroCPU[fila, columna + i] = "O"

            elif newori == "O" and columna - (barco.cantidad - 1) >= 0:
                for i in range(barco.cantidad):
                    if tableroCPU[fila, columna - i] != " ":
                        
                for i in range(barco.cantidad):
                    tableroCPU[fila, columna - i] = "O"
            

            return f"La CPU ha colocado sus barcos"

