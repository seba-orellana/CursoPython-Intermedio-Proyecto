import sqlite3
from tkinter.messagebox import showerror, showinfo, askyesno


class Base():
    def __init__(self):
        self.con = sqlite3.connect("estudiantes_curso_2023.db")
        self.cursor = self.con.cursor()

    def tabla_existe(self):
        sql = "SELECT * FROM sqlite_master WHERE type='table'"
        self.cursor.execute(sql)
        return not (self.cursor.fetchall() == [])

    def crear_tabla(self):
        if not self.tabla_existe():
            sql = "CREATE TABLE curso(dni INTEGER PRIMARY KEY,\
                nombre TEXT, apellido TEXT, nacimiento TEXT)"
            self.cursor.execute(sql)
            showinfo("Exito al crear",
                     "Curso creado y cargado al sistema con exito")
        else:
            showerror("Error al crear",
                      "Error: ya hay un curso creado y cargado en el sistema")

    def borrar_tabla(self, tree):
        confirmar = askyesno("Confirmar",
                             "¿Desea borrar el cliente actual" +
                             " cargado en el sistema?")
        if confirmar:
            if not self.tabla_existe():
                showerror("Error al borrar", "No hay curso creado previamente")
            else:
                sql = "DROP TABLE curso"
                self.cursor.execute(sql)
                showinfo("Operacion completada", "Curso eliminado")
                self.limpiar_arbol(tree)
