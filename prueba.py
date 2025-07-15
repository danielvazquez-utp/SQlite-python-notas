# Ejemplo de aplicación de las funciones de sqlite_functions.py
from sqlite_functions import connect_db, create_table, insert_data, fetch_data, close_connection, delete_table, update_data, count_rows, delete_row, create_index
# Definición de la base de datos y tabla
db_name = 'example.db'
table_name = 'users'
columns = {
    'id': 'INTEGER PRIMARY KEY',
    'name': 'TEXT NOT NULL',
    'age': 'INTEGER'
}
# Conectar a la base de datos
conn = connect_db(db_name)
# Crear la tabla
create_table(conn, table_name, columns)
# Insertar datos en la tabla
data = [
    (1, 'Alice', 30),
    (2, 'Bob', 25),
    (3, 'Charlie', 35)
]
insert_data(conn, table_name, data)
# Recuperar y mostrar los datos
fetched_data = fetch_data(conn, table_name)
print("Datos recuperados:", fetched_data)
# Actualizar datos en la tabla
update_data(conn, table_name, "age = 31", "name = 'Alice'")
# Contar filas en la tabla
row_count = count_rows(conn, table_name)
print("Número de filas en la tabla:", row_count)
# # Eliminar una fila de la tabla
# delete_row(conn, table_name, "name = 'Bob'")
# # Recuperar y mostrar los datos actualizados
# fetched_data = fetch_data(conn, table_name)
# print("Datos después de la eliminación:", fetched_data)
# # Crear un índice en la columna 'name'
# create_index(conn, table_name, 'idx_name', 'name')
# # Recuperar y mostrar los datos con el índice
# fetched_data = fetch_data(conn, table_name)
# print("Datos con índice:", fetched_data)
# # Eliminar la tabla
# delete_table(conn, table_name)
# # Cerrar la conexión a la base de datos
close_connection(conn)