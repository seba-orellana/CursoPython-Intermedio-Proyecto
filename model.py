import sqlite3
from tkinter.messagebox import showerror, showinfo, askyesno


class Base():
    con = None
    cursor = None

    def __init__(self):
        global cursor, con
        con = sqlite3.connect("estudiantes_curso_2023.db")
        cursor = con.cursor()


class Estudiante(Base):

    # CREACION/BORRADO DE TABLAS

    def tabla_existe(self):
        sql = "SELECT * FROM sqlite_master WHERE type='table'"
        cursor.execute(sql)
        return not (cursor.fetchall() == [])

    def crear_tabla(self):
        if not Estudiante().tabla_existe():
            sql = "CREATE TABLE curso(dni INTEGER PRIMARY KEY,\
                nombre TEXT, apellido TEXT, nacimiento TEXT)"
            cursor.execute(sql)
            showinfo("Exito al crear",
                     "Curso creado y cargado al sistema con exito")
        else:
            showerror("Error al crear",
                      "Error: ya hay un curso creado y cargado en el sistema")

    def borrar_tabla(self):
        confirmar = askyesno("Confirmar",
                             "¿Desea borrar el cliente actual" +
                             " cargado en el sistema?")
        if confirmar:
            if not Estudiante().tabla_existe():
                showerror("Error al borrar", "No hay curso creado previamente")
            else:
                sql = "DROP TABLE curso"
                cursor.execute(sql)
                showinfo("Operacion completada", "Curso eliminado")

    # MOSTRAR/BORRAR DATOS (ARBOL)

    def limpiar_arbol(self, tree):
        for elem in tree.get_children():
            tree.delete(elem)

    def cargar_arbol(self, tree):
        self.limpiar_arbol(tree)
        sql = "SELECT * FROM curso"
        cursor.execute(sql)
        datos = cursor.fetchall()
        for i in range(len(datos)):
            tree.insert("", "end", values=(str(datos[i][0]), str(datos[i][1]),
                                           str(datos[i][2]), str(datos[i][3])))

    # ALTA

    def crear_alumno(self, dni, nombre, apellido, nacimiento):
        data = (dni.get(), nombre.get(), apellido.get(), nacimiento.get(),)
        sql = "INSERT INTO curso(dni, nombre, apellido, nacimiento)\
             VALUES (?,?,?,?)"
        cursor.execute(sql, data)
        con.commit()

    def insertar_alumno(self, dni, nombre, apellido, nacimiento, tree):
        self.crear_alumno(dni, nombre, apellido, nacimiento)
        self.cargar_arbol(tree)

    # BAJA

    def borrar_alumno(self, tree):
        elem = tree.focus()
        valor = tree.item(elem)["values"][0]
        tree.delete(elem)
        sql = "DELETE FROM curso WHERE dni = " + str(valor)
        cursor.execute(sql)
        con.commit()
        self.cargar_arbol(tree)

    # CONSULTA

    def consultar_alumno(self, opc, val):
        opcion = opc.get()
        valor = val.get()
        match opcion:
            case 1:
                sql = "SELECT * FROM curso WHERE dni = " + str(valor)
                cursor.execute(sql)
                res = cursor.fetchone()
                if res is None:
                    showerror("Error al buscar", "No hay estudiante\
                         con el DNI ingresado")
                else:
                    showinfo("Resultado de la busqueda", "DNI: "
                             + str(res[0])+"\nNombre: " + res[1] +
                             "\nApellido: " + res[2] +
                             "\nFecha de Nacimiento: "+res[3])
            case 2:
                sql = "SELECT * FROM curso WHERE nombre = '"+str(valor)+"'"
                cursor.execute(sql)
                res = cursor.fetchone()
                if res is None:
                    showerror("Error al buscar", "No hay estudiante con el\
                        nombre ingresado")
                else:
                    showinfo("Resultado de la busqueda", "DNI: "
                             + str(res[0])+"\nNombre: " + res[1] +
                             "\nApellido: " + res[2] +
                             "\nFecha de Nacimiento: "+res[3])
            case 3:
                sql = "SELECT * FROM curso WHERE apellido = '"+str(valor)+"'"
                cursor.execute(sql)
                res = cursor.fetchone()
                if res is None:
                    showerror("Error al buscar", "No hay estudiante con el\
                         apellido ingresado")
                else:
                    showinfo("Resultado de la busqueda", "DNI: "
                             + str(res[0])+"\nNombre: " + res[1] +
                             "\nApellido: " + res[2] +
                             "\nFecha de Nacimiento: "+res[3])
            case 4:
                sql = "SELECT * FROM curso WHERE nacimiento = '"+str(valor)+"'"
                cursor.execute(sql)
                res = cursor.fetchone()
                if res is None:
                    showerror("Error al buscar", "No hay estudiante con la\
                         fecha de nacimiento ingresada")
                else:
                    showinfo("Resultado de la busqueda", "DNI: "
                             + str(res[0])+"\nNombre: " + res[1] +
                             "\nApellido: " + res[2] +
                             "\nFecha de Nacimiento: "+res[3])
