from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, END, messagebox
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de SQLAlchemy
Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

engine = create_engine('sqlite:///tasks.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Funciones
def refresh_task_list():
    task_listbox.delete(0, END)
    tasks = session.query(Task).all()
    for task in tasks:
        status = "[✓]" if task.completed else "[ ]"
        task_listbox.insert(END, f"{task.id} {status} {task.title}")

def add_task():
    title = title_entry.get()
    description = description_entry.get()
    if not title.strip():
        messagebox.showerror("Error", "El título no puede estar vacío.")
        return
    task = Task(title=title, description=description)
    session.add(task)
    session.commit()
    title_entry.delete(0, END)
    description_entry.delete(0, END)
    refresh_task_list()
    messagebox.showinfo("Éxito", "Tarea añadida.")

def mark_task_completed():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        task_id = int(selected_task.split()[0])
        task = session.query(Task).get(task_id)
        if task:
            task.completed = True
            session.commit()
            refresh_task_list()
            messagebox.showinfo("Éxito", "Tarea marcada como completada.")
    except Exception:
        messagebox.showerror("Error", "Por favor selecciona una tarea válida.")

def delete_completed_tasks():
    completed_tasks = session.query(Task).filter(Task.completed == True).all()
    for task in completed_tasks:
        session.delete(task)
    session.commit()
    refresh_task_list()
    messagebox.showinfo("Éxito", "Tareas completadas eliminadas.")

# Configuración de la ventana principal
root = Tk()
root.title("Gestión de Tareas")


Label(root, text="Título:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
title_entry = Entry(root, width=40)
title_entry.grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
description_entry = Entry(root, width=40)
description_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = Button(root, text="Agregar Tarea", command=add_task)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

task_listbox = Listbox(root, width=60, height=15)
task_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

scrollbar = Scrollbar(root, orient="vertical", command=task_listbox.yview)
scrollbar.grid(row=3, column=2, sticky="ns")
task_listbox.config(yscrollcommand=scrollbar.set)

mark_completed_button = Button(root, text="Marcar como Completada", command=mark_task_completed)
mark_completed_button.grid(row=4, column=0, padx=5, pady=5)

delete_button = Button(root, text="Eliminar Tareas Completadas", command=delete_completed_tasks)
delete_button.grid(row=4, column=1, padx=5, pady=5)

refresh_task_list()


root.mainloop()
