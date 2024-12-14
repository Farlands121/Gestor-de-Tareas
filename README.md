

# Gestor de Tareas
Un gestor de tareas interactivo diseñado para facilitar la organización de tareas diarias. Esta aplicación permite agregar, listar, completar y eliminar tareas de manera sencilla. Además, utiliza una base de datos SQLite para garantizar la persistencia de datos.

# Características
Agregar Tareas: Crea tareas con un título y una descripción personalizada.
Listar Tareas: Visualiza todas las tareas (pendientes o completadas) en una lista interactiva.
Marcar como Completada: Cambia el estado de las tareas a "completadas" con un solo clic.
Eliminar Tareas Completadas: Limpia tu lista eliminando todas las tareas completadas.
Persistencia de Datos: Las tareas se almacenan en una base de datos SQLite para que no se pierdan al cerrar la aplicación.
Interfaz Gráfica: Interactúa con una ventana gráfica diseñada con Tkinter para facilitar el uso.
# Requisitos Previos
Python 3.8 o superior: Asegúrate de tener Python instalado en tu sistema. Descargar Python
Módulos de Python:
SQLAlchemy: Manejo de la base de datos.
Tkinter: Interfaz gráfica (incluido por defecto en Python).

# Estructura del Proyecto
gestor-de-tareas/

│
├── app_gui.py        # Archivo principal con la interfaz gráfica

├── tasks.db          # Base de datos SQLite (se genera automáticamente)

├── README.md         # Documentación del proyecto

# Cómo Usar
Agregar Tareas: Introduce un título y una descripción, luego haz clic en "Agregar Tarea".

Listar Tareas: Las tareas aparecerán en una lista, indicando su estado (pendiente o completada).

Marcar como Completada: Selecciona una tarea de la lista y haz clic en "Marcar como Completada".

Eliminar Completadas: Haz clic en "Eliminar Tareas Completadas" para limpiar la lista.
