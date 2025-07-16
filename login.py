# Aplicación con Tkinter y SQLite para la creación de un login
import tkinter as tk
from sqlite_functions import connect_db, insert_data, fetch_data, close_connection, fetch_data_with_condition
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
    
    # Cerrar la conexión
    close_connection(conn)
    
    return user is not None

# creación de la ventana de login
def create_login_window():
    window = tk.Tk()
    window.title("Login")
    
    # Etiquetas y campos de entrada
    tk.Label(window, text="Usuario").grid(row=0, column=0)
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1)
    
    tk.Label(window, text="Contraseña").grid(row=1, column=0)
    password_entry = tk.Entry(window, show='*')
    password_entry.grid(row=1, column=1)
    
    # Función para manejar el login
    def login():
        username = username_entry.get()
        password = generate_password_hash(password_entry.get())
        print(f"Intentando acceder con usuario: {username} y contraseña: {password}")
        if authenticate_user(username, password):
            print("¡Acceso concedido!")
        else:
            print("¡Acceso denegado!")
    
    # Botón de login
    login_button = tk.Button(window, text="Acceder", command=login)
    login_button.grid(row=2, columnspan=2)
    
    window.mainloop()

# Llamada a la función para crear la ventana de login
if __name__ == "__main__":
    create_login_window()