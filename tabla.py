# Aplicación con Tkinter y SQLite para la gestión de usuarios
# importación de librerías y modulos necesarios
import tkinter as tk
from sqlite_functions import connect_db, insert_data, fetch_data, close_connection, fetch_data_with_condition, update_data
from crypt_functions import generate_password_hash
# función para autenticar al usuario
def authenticate_user(username, password):
    db_name = 'inventario.db'
    table_name = 'usuario'
    
    # Conectar a la base de datos
    conn = connect_db(db_name)
    
    # Recuperar los datos del usuario
    conditions = f"nombreUsuario = '{username}' AND contrasena = '{password}'"
    user_data = fetch_data_with_condition(conn, table_name, conditions)
    user = user_data[0] if user_data else None
    print(f"Datos del usuario: {user}")
    
    # Cerrar la conexión
    close_connection(conn)
    
    return user is not None

# función para borrar un usuario
def delete_user(user_id, window):
    pass

# función para actualizar un usuario en una ventana usando un formulario usando TopLevel
def update_user(user_id, window):
    # ocultar la ventana principal
    window.withdraw()

    # Crear una ventana TopLevel para actualizar el usuario
    update_window = tk.Toplevel(window)
    update_window.title("Actualizar Usuario")
    
    # Etiquetas y campos de entrada
    tk.Label(update_window, text="ID Usuario").grid(row=0, column=0)
    user_id_entry = tk.Entry(update_window)
    user_id_entry.grid(row=0, column=1)
    user_id_entry.insert(0, user_id)  # Rellenar con el ID del usuario
    
    tk.Label(update_window, text="Nuevo Nombre Usuario").grid(row=1, column=0)
    username_entry = tk.Entry(update_window)
    username_entry.grid(row=1, column=1)
    
    tk.Label(update_window, text="Nueva Contraseña").grid(row=2, column=0)
    password_entry = tk.Entry(update_window, show='*')
    password_entry.grid(row=2, column=1)

    #etiqueta para mostrar el mensaje de éxito
    success_label = tk.Label(update_window, text="", fg="green")
    success_label.grid(row=4, columnspan=2)
    
    # Función para manejar la actualización del usuario
    def update():
        user_id = user_id_entry.get()
        new_username = username_entry.get()
        new_password = password_entry.get()
        print(f"Actualizando usuario {user_id} a {new_username} con contraseña {new_password}")
        # Aquí se llamaría a la función de actualización en la base de datos
        db_name = 'inventario.db'
        table_name = 'usuario'
        conn = connect_db(db_name)
        hashed_password = generate_password_hash(new_password)
        set_clause = f"nombreUsuario = '{new_username}', contrasena = '{hashed_password}'"
        where_clause = f"idUsuario = {user_id}"
        update_data(conn, table_name, set_clause, where_clause)
        close_connection(conn)
        # mensaje de éxito
        success_label.config(text="Usuario actualizado correctamente")
        update_window.destroy()  # Cerrar la ventana después de actualizar
        # actualizar la tabla de usuarios
        users_table()
    
    # Botón de actualización
    update_button = tk.Button(update_window, text="Actualizar", command=update)
    update_button.grid(row=3, columnspan=2)

# creación de la ventana con la tabla de usuarios registrados
def users_table():
    db_name = 'inventario.db'
    table_name = 'usuario'
    
    # Conectar a la base de datos
    conn = connect_db(db_name)
    
    # Recuperar los datos de la tabla
    users_data = fetch_data(conn, table_name)
    
    # Cerrar la conexión
    close_connection(conn)
    
    # Crear una ventana para mostrar los usuarios
    window = tk.Tk()
    window.title("Usuarios Registrados")
    
    # Crear etiquetas para los encabezados de la tabla
    tk.Label(window, bg="black", foreground="white", width=20, height=2, text="ID").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(window, bg="black", foreground="white", width=20, height=2, text="Nombre Usuario").grid(row=0, column=1, padx=5, pady=5)
    tk.Label(window, bg="black", foreground="white", width=80, height=2, text="Contraseña").grid(row=0, column=2, padx=5, pady=5)
    tk.Label(window, bg="black", foreground="white", width=30, height=2, text="Opciones").grid(row=0, column=3, padx=5, pady=5)
    
    # Mostrar los datos de los usuarios en la tabla
    counter = 0
    for i, user in enumerate(users_data):
        if counter % 2 == 0:
            bg_color = "lightblue"
        else:
            bg_color = "white"
        tk.Label(window, bg=bg_color, width=20, height=2, text=user[0]).grid(row=i+1, column=0, padx=2, pady=2)
        tk.Label(window, bg=bg_color, width=20, height=2, text=user[1]).grid(row=i+1, column=1, padx=2, pady=2)
        tk.Label(window, bg=bg_color, width=80, height=2, text=user[2]).grid(row=i+1, column=2, padx=2, pady=2)
        
        # frame para los 2 botones de opciones
        options_frame = tk.Frame(window, bg=bg_color)
        options_frame.grid(row=i+1, column=3, padx=2, pady=2)
        # Botón para eliminar el usuario
        delete_button = tk.Button(options_frame, text="Eliminar", command=lambda user_id=user[0]: delete_user(user_id, window))
        delete_button.pack(side=tk.LEFT, padx=2, pady=2)
        # Botón para actualizar el usuario
        update_button = tk.Button(options_frame, text="Actualizar", command=lambda user_id=user[0]: update_user(user_id, window))
        update_button.pack(side=tk.LEFT, padx=2, pady=2)

        counter += 1
    
    window.mainloop()

# mostrar la tabla de usuarios registrados
if __name__ == "__main__":
    users_table()