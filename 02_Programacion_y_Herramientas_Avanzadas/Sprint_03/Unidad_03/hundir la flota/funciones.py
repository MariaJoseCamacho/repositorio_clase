import numpy as np
import random

def disparar(tablero,xy):
    xy = input ("¿Donde quieres disparar? Recuerda que tienes que facilitarnos dos coordenadas, la 'x'  y la 'y'.")
    if tablero[x][y]=="O":
        tablero[x][y]= "X"
    elif tablero[x][y]=="X":
        print(f"Nooooo, aquí ya habías disparado")
    else:
        tablero[x][y]="-"
        print("Has disparado al agua")

def comprobartablero(tablero):
       
    if tablero!="O":
        return f"¡¡¡Has ganado!!!"
    





