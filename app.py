from flask import Flask
import sqlite3
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

app = Flask(__name__)

# Crear base de datos
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    password_hash TEXT NOT NULL
)
""")

# Usuarios requeridos
usuarios = [
    (
        "guerson_bustamante",
        generate_password_hash("clave123")
    ),
    (
        "admin",
        generate_password_hash("admin123")
    )
]

# Verificar si ya existen usuarios
cursor.execute(
    "SELECT COUNT(*) FROM usuarios"
)

cantidad = cursor.fetchone()[0]

if cantidad == 0:
    cursor.executemany(
        """
        INSERT INTO usuarios
        (usuario,password_hash)
        VALUES (?,?)
        """,
        usuarios
    )

conexion.commit()

# Validar usuario 1
cursor.execute(
    """
    SELECT password_hash
    FROM usuarios
    WHERE usuario=?
    """,
    ("guerson_bustamante",)
)

hash_guardado = cursor.fetchone()[0]

if check_password_hash(
        hash_guardado,
        "clave123"):

    print(
        "Usuario Guerson validado correctamente"
    )

# Validar usuario 2
cursor.execute(
    """
    SELECT password_hash
    FROM usuarios
    WHERE usuario=?
    """,
    ("admin",)
)

hash_guardado = cursor.fetchone()[0]

if check_password_hash(
        hash_guardado,
        "admin123"):

    print(
        "Usuario admin validado correctamente"
    )

conexion.close()

@app.route("/")
def inicio():

    return """
    <h1>Actividad 3 DevNet</h1>

    <p>Servidor Flask funcionando</p>

    <p>Puerto 5800 habilitado</p>

    <p>Usuarios almacenados en SQLite</p>

    <p>Contraseñas almacenadas mediante hash</p>
    """

app.run(
    host="0.0.0.0",
    port=5800
)