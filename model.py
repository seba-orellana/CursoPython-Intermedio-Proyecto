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

    def tabla_existe(self):
        sql = "SELECT * FROM sqlite_master WHERE type='table'"
        cursor.execute(sql)
        return not (cursor.fetchall() == [])

    def crear_tabla(self):
        if not Estudiante().tabla_existe():
            sql = "CREATE TABLE curso(dni INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT, nacimiento TEXT)"
            cursor.execute(sql)
            showinfo("Exito al crear", "Curso creado y cargado al sistema con exito")
        else:
            showerror("Error al crear", "Error: ya hay un curso creado y cargado en el sistema")

    def borrar_tabla(self):
        confirmar = askyesno("Confirmar", "¿Desea borrar el cliente actual cargado en el sistema?")
        if confirmar:
            if not Estudiante().tabla_existe():
                showerror("Error al borrar", "No hay curso creado previamente")
            else:
                sql = "DROP TABLE curso"
                cursor.execute(sql)
                showinfo("Operacion completada", "Curso eliminado")

    def crear_alumno(self, dni, nombre, apellido, nacimiento):
        data = (dni.get(), nombre.get(), apellido.get(), nacimiento.get(),)
        sql = "INSERT INTO curso(dni, nombre, apellido, nacimiento) VALUES (?,?,?,?)"
        cursor.execute(sql, data)
        con.commit()

    def consultar_alumno(self, opc, val):
        opcion = opc.get()
        valor = val.get()
        match opcion:
            case 1:
                sql = "SELECT * FROM curso WHERE dni = "+str(valor)
                cursor.execute(sql)
                res = cursor.fetchone()
                if res is None:
                    showerror("Error al buscar", "No hay estudiante con el DNI ingresado")
                else:
                    showinfo("Resultado de la busqueda", "DNI: "+str(res[0])+"\nNombre: "+res[1]+"\nApellido: "+res[2]+"\nFecha de Nacimiento: "+res[3]) 
            case 2:
                sql = "SELECT * FROM curso WHERE nombre = '"+str(valor)+"'"
                cursor.execute(sql)
                res = cursor.fetchone()
                if res is None:
                    showerror("Error al buscar", "No hay estudiante con el nombre ingresado")
                else:
                    showinfo("Resultado de la busqueda", "DNI: "+str(res[0])+"\nNombre: "+res[1]+"\nApellido: "+res[2]+"\nFecha de Nacimiento: "+res[3])
            case 3:
                sql = "SELECT * FROM curso WHERE apellido = '"+str(valor)+"'"
                print(sql)
                cursor.execute(sql)
                res = cursor.fetchone()
                if res is None:
                    showerror("Error al buscar", "No hay estudiante con el apellido ingresado")
                else:
                    showinfo("Resultado de la busqueda", "DNI: "+str(res[0])+"\nNombre: "+res[1]+"\nApellido: "+res[2]+"\nFecha de Nacimiento: "+res[3])
            case 4:
                sql = "SELECT * FROM curso WHERE nacimiento = '"+str(valor)+"'"
                cursor.execute(sql)
                res = cursor.fetchone()
                if res is None:
                    showerror("Error al buscar", "No hay estudiante con la fecha de nacimiento ingresada")
                else:
                    showinfo("Resultado de la busqueda", "DNI: "+str(res[0])+"\nNombre: "+res[1]+"\nApellido: "+res[2]+"\nFecha de Nacimiento: "+res[3])
