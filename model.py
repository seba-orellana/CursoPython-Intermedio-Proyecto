from tkinter.messagebox import showerror, showinfo
from regex import Reg
import sqlite3


class Estudiante():

    # MOSTRAR/BORRAR DATOS (ARBOL)

    def limpiar_arbol(self, tree):
        for elem in tree.get_children():
            tree.delete(elem)

    def cargar_arbol(self, tree):
        con = sqlite3.connect("estudiantes_curso_2023.db")
        cursor = con.cursor()
        self.limpiar_arbol(tree)
        sql = "SELECT * FROM curso"
        cursor.execute(sql)
        datos = cursor.fetchall()
        for i in range(len(datos)):
            tree.insert("", "end", values=(str(datos[i][0]), str(datos[i][1]),
                                           str(datos[i][2]), str(datos[i][3])))

    # ALTA

    def crear_alumno(self, dni, nombre, apellido, nacimiento):
        con = sqlite3.connect("estudiantes_curso_2023.db")
        cursor = con.cursor()
        if (Reg().validar_fecha(nacimiento.get())
           and Reg().validar_dni(dni.get())
           and Reg().validar_nombre_apellido(nombre.get())
           and Reg().validar_nombre_apellido(apellido.get())):
            data = (dni.get(), nombre.get(), apellido.get(), nacimiento.get(),)
            sql = "INSERT INTO curso(dni, nombre, apellido, nacimiento)\
                VALUES (?,?,?,?)"
            cursor.execute(sql, data)
            con.commit()
        else:
            showerror("Error al cargar estudiante",
                      "Verifique el formato de los datos cargados")

    def insertar_alumno(self, dni, nombre, apellido, nacimiento, tree):
        self.crear_alumno(dni, nombre, apellido, nacimiento)
        self.cargar_arbol(tree)

    # BAJA

    def borrar_alumno(self, tree):
        con = sqlite3.connect("estudiantes_curso_2023.db")
        cursor = con.cursor()
        elem = tree.focus()
        valor = tree.item(elem)["values"][0]
        tree.delete(elem)
        sql = "DELETE FROM curso WHERE dni = " + str(valor)
        cursor.execute(sql)
        con.commit()
        self.cargar_arbol(tree)

    # CONSULTA

    def consultar_alumno(self, opc, val):
        con = sqlite3.connect("estudiantes_curso_2023.db")
        cursor = con.cursor()
        opcion = opc.get()
        valor = str(val.get())
        match opcion:
            case 1:
                if Reg().validar_dni(valor):
                    sql = "SELECT * FROM curso WHERE dni = " + valor
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
                else:
                    showerror("Error al consultar por DNI",
                              "Verifique el formato del dato ingresado")
            case 2:
                if Reg().validar_nombre_apellido(valor):
                    sql = "SELECT * FROM curso WHERE nombre = '" + valor + "'"
                    cursor.execute(sql)
                    res = cursor.fetchone()
                    if res is None:
                        showerror("Error al buscar",
                                  "No hay estudiante con el nombre ingresado")
                    else:
                        showinfo("Resultado de la busqueda", "DNI: "
                                 + str(res[0])+"\nNombre: " + res[1] +
                                 "\nApellido: " + res[2] +
                                 "\nFecha de Nacimiento: "+res[3])
                else:
                    showerror("Error al consultar por Nombre",
                              "Verifique el formato del dato ingresado")
            case 3:
                if Reg().validar_nombre_apellido(valor):
                    sql = ("SELECT * FROM curso WHERE apellido = '"
                           + valor + "'")
                    cursor.execute(sql)
                    res = cursor.fetchone()
                    if res is None:
                        showerror("Error al buscar",
                                  "No hay estudiante con el"
                                  + "apellido ingresado")
                    else:
                        showinfo("Resultado de la busqueda", "DNI: "
                                 + str(res[0])+"\nNombre: " + res[1] +
                                 "\nApellido: " + res[2] +
                                 "\nFecha de Nacimiento: "+res[3])
                else:
                    showerror("Error al consultar por Apellido",
                              "Verifique el formato del dato ingresado")
            case 4:
                if Reg().validar_fecha(valor):
                    sql = ("SELECT * FROM curso WHERE nacimiento = '"
                           + valor + "'")
                    cursor.execute(sql)
                    res = cursor.fetchone()
                    if res is None:
                        showerror("Error al buscar",
                                  "No hay estudiante con la fecha"
                                  + " de nacimiento ingresada")
                    else:
                        showinfo("Resultado de la busqueda", "DNI: "
                                 + str(res[0])+"\nNombre: " + res[1] +
                                 "\nApellido: " + res[2] +
                                 "\nFecha de Nacimiento: "+res[3])
                else:
                    showerror("Error al consultar por Fecha de Nacimiento",
                              "Verifique el formato del dato ingresado")

    # MODIFICAR

    def modificar_alumno(self, opc, val, tree):
        con = sqlite3.connect("estudiantes_curso_2023.db")
        cursor = con.cursor()
        opcion = opc.get()
        valor = str(val.get())
        elem = tree.focus()
        val_a_modificar = str(tree.item(elem)["values"][0])
        match opcion:
            case 1:
                if Reg().validar_dni(valor):
                    sql = ("UPDATE curso SET dni = '"
                           + valor + "' WHERE dni = '"
                           + val_a_modificar) + "'"
                    cursor.execute(sql)
                    con.commit()
                else:
                    showerror("Error al modificar DNI",
                              "Verifique el formato del dato ingresado")
            case 2:
                if Reg().validar_nombre_apellido(valor):
                    sql = ("UPDATE curso SET nombre = '"
                           + valor + "' WHERE dni = '"
                           + val_a_modificar) + "'"
                    cursor.execute(sql)
                    con.commit()
                else:
                    showerror("Error al modificar Nombre",
                              "Verifique el formato del dato ingresado")
            case 3:
                if Reg().validar_nombre_apellido(valor):
                    sql = ("UPDATE curso SET apellido = '"
                           + valor + "' WHERE dni = '"
                           + val_a_modificar) + "'"
                    cursor.execute(sql)
                    con.commit()
                else:
                    showerror("Error al modificar Apellido",
                              "Verifique el formato del dato ingresado")
            case 4:
                if Reg().validar_fecha(valor):
                    sql = ("UPDATE curso SET nacimiento = '"
                           + valor + "' WHERE dni = "
                           + val_a_modificar)
                    cursor.execute(sql)
                    con.commit()
                else:
                    showerror("Error al modificar la Fecha de Nacimiento",
                              "Verifique el formato del dato ingresado")
        self.cargar_arbol(tree)
