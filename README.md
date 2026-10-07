# Sistema de Gestión de Tareas con API y Base de Datos

Proyecto desarrollado en Flask y SQLite para la materia Programación sobre Redes de la Tecnicatura Superior en Desarrollo de Software del IFTS 29.

Para acceder al repositorio completo del proyecto haciendo clic en el siguiente enlace:
[Repositorio en GitHub - PFO2](https://github.com/emilianog4/PFO2---EMILIANO-GUTIERREZ)

## Requisitos Previos

- Python 3.x instalado.
- Librería Flask (`pip install Flask`).

## Instrucciones de Ejecución

1. Clonar o descargar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el servidor con el siguiente comando:

   ```bash
   python servidor.py


   ```

## Endpoints

Disponibles para Probar usando por ej Postman o Thunder Client

- POST /registro: Envía un JSON con {"usuario": "tu_nombre", "contraseña": "tu_contraseña"}.
  ![POST registro](<img/POST registro.png>)

- POST /login: Envía un JSON con {"usuario": "tu_nombre", "contraseña": "tu_contraseña"}.
  ![POST login](<img/POST login.png>)
- GET /tareas: Muestra la página HTML de bienvenida en el navegador.
  ![GET tareas](<img/GET tareas.png>)
- **¿Por qué hashear contraseñas?**
  - _Respuesta:_ Las contraseñas nunca deben guardarse en texto plano en la base de datos. Si un atacante logra acceder a la base de datos, vería las contraseñas reales de todos los usuarios, comprometiendo su seguridad en otros servicios. Al aplicar un _hash_ (una función matemática unidireccional con herramientas como Werkzeug), se almacena una cadena codificada imposible de revertir a su forma original, protegiendo la privacidad de los usuarios incluso ante vulnerabilidades de filtración de datos.

- **Ventajas de usar SQLite en este proyecto:**
  - _Respuesta:_ SQLite es una base de datos liviana basada en un único archivo local (`database.db`), lo que significa que no requiere instalar ni configurar servidores complejos (como MySQL o PostgreSQL). Es ideal para proyectos académicos, prototipos y aplicaciones de menor escala porque es rápida, fácil de integrar con Python mediante su librería nativa `sqlite3`, y facilita la portabilidad de todo el proyecto.

---
