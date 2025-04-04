import sqlite3
conexion = sqlite3.connect("proveedores.db")
cursor = conexion.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Proveedor (
        id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo_proveedor TEXT UNIQUE NOT NULL,
        nombre TEXT NOT NULL,
        direccion TEXT,
        ciudad TEXT,
        provincia TEXT)
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categoria (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL)
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pieza (
        id_pieza INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        color TEXT,
        precio FLOAT,
        id_categoria INTEGER,
        FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria))
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Stock (
        id_suministro INTEGER PRIMARY KEY AUTOINCREMENT,
        id_proveedor INTEGER,
        id_pieza INTEGER,
        fecha DATE NOT NULL,
        cantidad INTEGER NOT NULL,
        FOREIGN KEY (id_proveedor) REFERENCES Proveedor(id_proveedor),
        FOREIGN KEY (id_pieza) REFERENCES Pieza(id_pieza))
''')