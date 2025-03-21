
from variables import stockbarcos, mensajeinicial, mensajebarco, mensajederrota, mensajefinal, mensajerrorbarco, mensajestart, mensajeturno, mensajevictoria, tableroCPU, tablerojp
from clases import Barco, Tablero, Acorazado, Destructor, Submarino, Portaaviones
import numpy as np
import random


def iniciarjuego():
    print(mensajeinicial)
    nombrejp = input("Nombre de jugador:")
    print(tablerojp, "\n", "#"*40,"\n",  tableroCPU)
    print(f"Bienvenido {nombrejp} vamos a colocar tus barcos")
    print("#" *40)
    print(f"Tenemos 4 Destructores")
    for i in range(4):
        tablerojp = colocabarco(Destructor, tablerojp)
        return tablerojp
    



iniciarjuego()
