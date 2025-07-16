# Módulo con funciones para manejar una base de datos SQLite
import sqlite3
def connect_db(db_name):
    """Conecta a la base de datos SQLite y devuelve la conexión."""
    return sqlite3.connect(db_name)

def create_table(conn, table_name, columns):
    """Crea una tabla en la base de datos."""
    cursor = conn.cursor()
    columns_with_types = ', '.join(f"{col} {dtype}" for col, dtype in columns.items())
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})')
    conn.commit()
    
def insert_data(conn, table_name, data):
    """Inserta datos en una tabla de la base de datos."""
    cursor = conn.cursor()
    placeholders = ', '.join(['?' for _ in data[0]])
    cursor.executemany(f'INSERT INTO {table_name} VALUES ({placeholders})', data)
    conn.commit()
    
def fetch_data(conn, table_name):
    """Recupera todos los datos de una tabla."""
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table_name}')
    return cursor.fetchall()

def fetch_data_with_condition(conn, table_name, condition):
    """Recupera datos de una tabla con una condición específica."""
    cursor = conn.cursor()
    print(f'SELECT * FROM {table_name} WHERE {condition}')
    cursor.execute(f'SELECT * FROM {table_name} WHERE {condition}')
    return cursor.fetchall()

def close_connection(conn):
    """Cierra la conexión a la base de datos."""
    conn.close()
    
def delete_table(conn, table_name):
    """Elimina una tabla de la base de datos."""
    cursor = conn.cursor()
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    conn.commit()
    
def update_data(conn, table_name, set_clause, where_clause):
    """Actualiza datos en una tabla de la base de datos."""
    cursor = conn.cursor()
    cursor.execute(f'UPDATE {table_name} SET {set_clause} WHERE {where_clause}')
    conn.commit()
    
def count_rows(conn, table_name):
    """Cuenta el número de filas en una tabla."""
    cursor = conn.cursor()
    cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
    return cursor.fetchone()[0]

def delete_row(conn, table_name, where_clause):
    """Elimina una fila de una tabla de la base de datos."""
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {table_name} WHERE {where_clause}')
    conn.commit()
    
def create_index(conn, table_name, index_name, column_name):
    """Crea un índice en una columna de una tabla."""
    cursor = conn.cursor()
    cursor.execute(f'CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({column_name})')
    conn.commit()
    
def drop_index(conn, index_name):
    """Elimina un índice de la base de datos."""
    cursor = conn.cursor()
    cursor.execute(f'DROP INDEX IF EXISTS {index_name}')
    conn.commit()
    
def max_index(conn, table_name, column_name):
    """Obtiene el valor máximo de una columna en una tabla."""
    cursor = conn.cursor()
    cursor.execute(f'SELECT MAX({column_name}) FROM {table_name}')
    return cursor.fetchone()[0]

