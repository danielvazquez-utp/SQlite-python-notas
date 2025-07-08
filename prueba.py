import sqlite_functions as sq

def __main__():
    
    conexion = sq.connect_db('ejemplo.db')
    consulta = sq.fetch_data(conexion, 'empleados')
    for fila in consulta:
        print(fila)