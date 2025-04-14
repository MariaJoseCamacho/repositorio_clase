import sqlite3
import pandas as pd

conexion = sqlite3.connect("proveedores.db")
cursor = conexion.cursor()

# Tabla proveedor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Proveedor (
        id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        direccion TEXT,
        ciudad TEXT,
        provincia TEXT)
''')
# Tabla categoría
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categoria (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL)
''')

#Tabla pieza
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pieza (
        id_pieza INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        marca TEXT,
        modelo_compatible TEXT,
        color TEXT,
        precio FLOAT,
        id_categoria INTEGER,
        FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria))
''')

# Tabla almacen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Stock (
        id_stock INTEGER PRIMARY KEY AUTOINCREMENT,
        id_proveedor INTEGER,
        id_pieza INTEGER,
        fecha DATE NOT NULL,
        cantidad INTEGER NOT NULL,
        ubicacion TEXT,
        FOREIGN KEY (id_proveedor) REFERENCES Proveedor(id_proveedor),
        FOREIGN KEY (id_pieza) REFERENCES Pieza(id_pieza))
''')

# Introducimos los datos de las categorías
categorias = ['pantalla','bateria','camara','placabase', 'carcasa','altavoz','sensor']
cursor.executemany("INSERT OR IGNORE INTO Categoria (nombre) VALUES (?)", categorias)

# Introducimos los datos de los proveedores
proveedores = [
    ("MOV001", "Repuestos Mobile S.L.", "Calle Circuito 21", "Madrid", "Madrid"),
    ("MOV002", "iFixMovil", "Avenida Reparación 101", "Barcelona", "Barcelona"),
    ("MOV003", "ElectroRepuestos", "Calle Batería 5", "Valencia", "Valencia"),
    ("MOV004", "Piezas PhoneTech", "Polígono Smart 8", "Sevilla", "Sevilla"),
    ("MOV005", "Tecnorrecambios", "Ronda Electrónica 44", "Bilbao", "Vizcaya"),
    ("MOV006", "Recambios GSM", "Avenida Pantalla 17", "Zaragoza", "Zaragoza"),
    ("MOV007", "Mundo Móvil", "Calle Antena 30", "Granada", "Andalucía")
]
cursor.executemany('''
    INSERT INTO Proveedor (codigo_proveedor, nombre, direccion, ciudad, provincia)
    VALUES (?, ?, ?, ?, ?)''', proveedores)

# Introducimos los datos de las piezas
piezas = [
    ("Pantalla OLED", "Apple", "iPhone 13", "Negro", 189.99, 1),
    ("Batería Li-Ion", "Samsung", "Galaxy S21", "N/A", 49.90, 2),
    ("Cámara trasera 12MP", "Xiaomi", "Redmi Note 11", "Negro", 29.99, 3),
    ("Placa base 128GB", "Apple", "iPhone 12", "N/A", 289.00, 4),
    ("Carcasa trasera", "Samsung", "Galaxy A52", "Azul", 19.95, 5),
    ("Altavoz interno", "Huawei", "P30", "Negro", 9.95, 6),
    ("Sensor de pantalla", "Realme", "Realme 8", "N/A", 4.75, 7)
]
cursor.executemany('''
    INSERT INTO Pieza (nombre, marca, modelo_compatible, color, precio, id_categoria)
    VALUES (?, ?, ?, ?, ?, ?)''', piezas)

# Introducimos nuestro stock actual
cursor.execute('''
    INSERT INTO Stock (id_proveedor, id_pieza, fecha, cantidad, ubicacion)
    VALUES (?, ?, ?, ?, ?)''', (1, 1, "2025-04-01", 8, "B2"))  

cursor.execute('''
    INSERT INTO Stock (id_proveedor, id_pieza, fecha, cantidad, ubicacion)
    VALUES (?, ?, ?, ?, ?)''', (2, 2, "2025-04-01", 12, "A1")) 

cursor.execute('''
    INSERT INTO Stock (id_proveedor, id_pieza, fecha, cantidad, ubicacion)
    VALUES (?, ?, ?, ?, ?)''', (3, 3, "2025-04-01", 20, "C3")) 

cursor.execute('''
    INSERT INTO Stock (id_proveedor, id_pieza, fecha, cantidad, ubicacion)
    VALUES (?, ?, ?, ?, ?)''', (4, 4, "2025-04-01", 4, "B3"))  

cursor.execute('''
    INSERT INTO Stock (id_proveedor, id_pieza, fecha, cantidad, ubicacion)
    VALUES (?, ?, ?, ?, ?)''', (5, 5, "2025-04-01", 10, "A2")) 

cursor.execute('''
    INSERT INTO Stock (id_proveedor, id_pieza, fecha, cantidad, ubicacion)
    VALUES (?, ?, ?, ?, ?)''', (6, 6, "2025-04-01", 18, "D4")) 

cursor.execute('''
    INSERT INTO Stock (id_proveedor, id_pieza, fecha, cantidad, ubicacion)
    VALUES (?, ?, ?, ?, ?)''', (7, 7, "2025-04-01", 30, "E5")) 


conexion.commit()
conexion.close()

def sql_query(query):
    cursor.execute(query)
    Lista = cursor.fetchall()
    names = [description[0] for description in cursor.description]
    return pd.DataFrame(Lista, columns=names)

query='''Select * From proveedor'''
sql_query(query)