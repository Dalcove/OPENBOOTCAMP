import sqlite3

connex = sqlite3.connect('alumnos.db')

connex.execute('''CREATE TABLE Alumnos
                 (id INTEGER PRIMARY KEY,
                  nombre TEXT,
                  apellido TEXT);''')
                 
connex.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (1, 'Juan', 'García')")
connex.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (2, 'María', 'López')")
connex.execute("INSERT INTO Alumnos (id, nombre, apellido) VALUES (3, 'Pedro', 'Martínez')")

resultado = connex.execute("SELECT * FROM Alumnos WHERE nombre='Juan'").fetchone()

if resultado is not None:
    print(f"ID: {resultado[0]}, Nombre: {resultado[1]}, Apellido: {resultado[2]}")
else:
    print("No se encontró ningún alumno con ese nombre.")

connex.close()
