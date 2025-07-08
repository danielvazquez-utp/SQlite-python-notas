# Ejemplo de una aplicación con Sqlite3

# importando las librerías necesarias
import sqlite3

# Conectando a la base de datos
conexion = sqlite3.connect('ejemplo.db')
# Creando un cursor para ejecutar comandos SQL
cursor = conexion.cursor()
# Creando una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        salario REAL NOT NULL
    )
''')
# Insertando datos en la tabla
# cursor.execute('''
#     INSERT INTO empleados (nombre, salario) VALUES
#     ('Juan', 30000),
#     ('Ana', 35000),
#     ('Luis', 40000)
# ''')
# Guardando los cambios
conexion.commit()
# Consultando datos de la tabla
cursor.execute('SELECT * FROM empleados')
resultados = cursor.fetchall()
# Mostrando los resultados
for fila in resultados:
    print(f'ID: {fila[0]}, Nombre: {fila[1]}, Salario: {fila[2]}')
# Cerrando la conexión
conexion.close()
