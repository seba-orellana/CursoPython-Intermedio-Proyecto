import sqlite3
from tkinter.messagebox import showerror, showinfo, askyesno


class Base():
    """
    Clase utilizada para operar con las tablas dentro de la base de datos en \
    SQL
    """
    def __init__(self):
        self.con = sqlite3.connect("estudiantes_curso_2023.db")
        self.cursor = self.con.cursor()

    def tabla_existe(self):
        """
        Se verifica si dentro del archivo **estudiantes_curso_2023.db** \
        existe una tabla

        :return: Tabla existe o no existe dentro del archivo
        :rtype: Boolean
        """
        try:
            sql = "SELECT * FROM sqlite_master WHERE type='table'"
            self.cursor.execute(sql)
            return not (self.cursor.fetchall() == [])
        except sqlite3.OperationalError:
            print("Error al verificar informacion en \
                  la tabla de la base de datos")

    def crear_tabla(self):
        """
        Se crea una tabla nueva dentro del archivo \
        **estudiantes_curso_2023.db** si es que esta no existia previamente. \
        En caso de que ya existiera, se muestra un mensaje de error
        """
        if not self.tabla_existe():
            try:
                sql = "CREATE TABLE curso(dni INTEGER PRIMARY KEY,\
                    nombre TEXT, apellido TEXT, nacimiento TEXT)"
                self.cursor.execute(sql)
            except sqlite3.OperationalError:
                print("Error al intentar crear la tabla de estudiantes")
            else:
                showinfo("Exito al crear",
                         "Curso creado y cargado al sistema con exito")
        else:
            showerror("Error al crear",
                      "Error: ya hay un curso creado y cargado en el sistema")

    def borrar_tabla(self, tree):
        """
        Se borra la tabla dentro del archivo **estudiantes_curso_2023.db** \
        tras confirmar con el usuario. En caso de que la tabla no existiese, \
        se muestra un mensaje de error
        """
        confirmar = askyesno("Confirmar",
                             "¿Desea borrar el cliente actual" +
                             " cargado en el sistema?")
        if confirmar:
            if not self.tabla_existe():
                showerror("Error al borrar", "No hay curso creado previamente")
            else:
                try:
                    sql = "DROP TABLE curso"
                    self.cursor.execute(sql)
                    showinfo("Operacion completada", "Curso eliminado")
                    self.limpiar_arbol(tree)
                except sqlite3.OperationalError:
                    print("Error al intentar borrar la tabla de estudiantes")
