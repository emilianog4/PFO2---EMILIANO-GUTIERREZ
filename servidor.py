from flask import Flask, request, jsonify, render_template_string
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Función para inicializar la base de datos SQLite
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
@app.route('/')
def home():
    return "Servidor activo. Usa /tareas, /registro o /login"

# 1. Registro de Usuarios
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contraseña')

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan datos (usuario o contraseña)"}), 400

    # Hashear la contraseña por seguridad (nunca en texto plano)
    hashed_password = generate_password_hash(contrasena)

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, hashed_password))
        conn.commit()
        conn.close()
        return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400

# 2. Inicio de Sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contraseña')

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan datos (usuario o contraseña)"}), 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT contrasena FROM usuarios WHERE usuario = ?", (usuario,))
    row = cursor.fetchone()
    conn.close()

    # Verificar si el usuario existe y si la contraseña coincide con el hash
    if row and check_password_hash(row[0], contrasena):
        return jsonify({"mensaje": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

# 3. Gestión de Tareas (HTML de Bienvenida)
@app.route('/tareas', methods=['GET'])
def tareas():
    html_bienvenida = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Bienvenido</title>
    </head>
    <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9;">
        <h1>¡Bienvenido al Sistema de Gestión de Tareas!</h1>
        <p>Has accedido exitosamente al sistema.</p>
    </body>
    </html>
    """
    return render_template_string(html_bienvenida), 200

if __name__ == '__main__':
    init_db()  # Crea la base de datos y la tabla al iniciar
    app.run(debug=True, port=5000)


