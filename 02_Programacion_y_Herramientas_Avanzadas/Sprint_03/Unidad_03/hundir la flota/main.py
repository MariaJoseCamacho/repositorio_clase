
from variables import stockbarcos, mensajeinicial, mensajebarco, mensajederrota, mensajefinal, mensajerrorbarco, mensajestart, mensajeturno, mensajevictoria, tableroCPU, tablerojp
from clases import Barco, Tablero, Acorazado, Destructor, Submarino, Portaaviones
import numpy as np
import random


def iniciarjuego():
    print(mensajeinicial)
    nombrejp = input("Nombre de jugador:")

    tablerojp = Tablero.creatablero(10)
    print(tablerojp)
    print("#"*40)
    tableroCPU= Tablero.creatablero(10)
    print(tableroCPU)

    print(f"Bienvenido {nombrejp} vamos a colocar tus barcos")
    print("#" *40)

    print(f"Tenemos 4 Destructores")
    print("#"*40)
    for i in range(4):
        tablerojp=Tablero.colocabarco(Destructor, tablerojp)
        print(tablerojp)
    
    



iniciarjuego()
