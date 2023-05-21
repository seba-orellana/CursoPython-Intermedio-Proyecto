from tkinter.messagebox import showerror, showinfo
from verif import Reg
import sqlite3
from observer import Objeto
from decorators import agregar_logs
from decorators import borrar_logs
from decorators import modificar_logs


class Estudiante(Objeto):
    """
    Clase la cual contiene todos los metodos utilizados para \
    realizar el C.R.U.D. junto con los metodos utilizados para\
     operar el treeview(tabla)
    """

    # MOSTRAR/BORRAR DATOS (ARBOL)

    def limpiar_arbol(self, tree):
        """
        Limpia todos los valores del treeview(tabla) dentro de la \
        aplicacion en tkinter.

        :param tree: Variable donde se guarda la treeview(tabla).
        :type tree: Treeview

        """
        for elem in tree.get_children():
            tree.delete(elem)

    def cargar_arbol(self, tree):
        """
        Se realiza una carga de los datos desde la base de datos en SQL\
        al treeview(tabla) dentro de la aplicacion en tkinter.

        :param tree: Variable donde se guarda la treeview(tabla).
        :type tree: Treeview

        """
        try:
            con = sqlite3.connect("estudiantes_curso_2023.db")
            cursor = con.cursor()
        except sqlite3.OperationalError:
            print("Error al conectar a la base de datos")
        else:
            self.limpiar_arbol(tree)
            sql = "SELECT * FROM curso"
            cursor.execute(sql)
            datos = cursor.fetchall()
            for i in range(len(datos)):
                tree.insert("", "end", values=(str(datos[i][0]),
                                               str(datos[i][1]),
                                               str(datos[i][2]),
                                               str(datos[i][3])))

    # ALTA

    def crear_alumno(self, dni, nombre, apellido, nacimiento):
        """
        Se inserta un alumno a la base de datos dentro de SQL

        :param dni: Numero de documento del alumno a cargar.
        :type dni: Int

        :param nombre: Nombre del estudiante a cargar
        :type nombre: Str

        :param apellido: Apellido del estudiante a cargar
        :type apellido: Str

        :param nacimiento: Fecha de nacimiento del estudiante a cargar
        :type nacimiento: Str

        """
        try:
            con = sqlite3.connect("estudiantes_curso_2023.db")
            cursor = con.cursor()
        except sqlite3.OperationalError:
            print("Error al conectar a la base de datos")
        else:
            if (Reg().validar_fecha(nacimiento.get())
                and Reg().validar_dni(dni.get())
                and Reg().validar_nombre_apellido(nombre.get())
                    and Reg().validar_nombre_apellido(apellido.get())):
                data = (dni.get(), nombre.get(), apellido.get(),
                        nacimiento.get(),)
                sql = "INSERT INTO curso(dni, nombre, apellido, nacimiento)\
                VALUES (?,?,?,?)"
                cursor.execute(sql, data)
                con.commit()
            else:
                showerror("Error al cargar estudiante",
                          "Verifique el formato de los datos cargados")

    @agregar_logs
    def insertar_alumno(self, dni, nombre, apellido, nacimiento, tree):
        """
        Se realiza la carga del alumno utilizando ``Estudiante.crear_alumno()``
        .Posteriormente se actualiza la treeview(tabla) con los nuevos datos \
        utilizando ``Estudiante.cargar_arbol()``

        :param dni: Numero de documento del alumno a cargar.
        :type dni: Int

        :param nombre: Nombre del estudiante a cargar
        :type nombre: Str

        :param apellido: Apellido del estudiante a cargar
        :type apellido: Str

        :param nacimiento: Fecha de nacimiento del estudiante a cargar
        :type nacimiento: Str

        :param tree: Variable donde se guarda la treeview(tabla).
        :type tree: Treeview

        """
        self.crear_alumno(dni, nombre, apellido, nacimiento)
        self.cargar_arbol(tree)
        # Observador
        self.update('insertar_alumno', dni.get(),
                    nombre.get(), apellido.get(), nacimiento.get())

    # BAJA

    @borrar_logs
    def borrar_alumno(self, tree):
        """
        Se elimina el alumno de la base de datos de SQL y posteriormente \
        se actualiza la treeview(tabla) utilizando \
        ``Estudiante.cargar_arbol()``

        :param tree: Variable donde se guarda la treeview(tabla).
        :type tree: Treeview

        """
        try:
            con = sqlite3.connect("estudiantes_curso_2023.db")
            cursor = con.cursor()
        except sqlite3.OperationalError:
            print("Error al conectar a la base de datos")
        else:
            elem = tree.focus()
            valor = tree.item(elem)["values"][0]
            tree.delete(elem)
            sql = "DELETE FROM curso WHERE dni = " + str(valor)
            cursor.execute(sql)
            con.commit()
            self.cargar_arbol(tree)
            # Observador
            self.update('borrar_alumno', valor)

    # CONSULTA

    def consultar_alumno(self, opc, val):
        """
        Se consulta dentro de la base de datos si es que un alumno existe.
        En caso de existir, se muestran todos los datos. Caso contrario, se
        muestra un mensaje de error indicando que no existe el estudiante
        buscado

        :param opc: Opcion escogida para buscar por el usuario.
        :type opc: IntVar(tkinter)

        :param val: Valor a consultar de la opcion escogida
        :type val: StringVar(tkinter)

        """
        try:
            con = sqlite3.connect("estudiantes_curso_2023.db")
            cursor = con.cursor()
        except sqlite3.OperationalError:
            print("Error al conectar a la base de datos")
        else:
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
                            # Observador
                            self.update('consultar_alumno', valor)
                    else:
                        showerror("Error al consultar por DNI",
                                  "Verifique el formato del dato ingresado")
                case 2:
                    if Reg().validar_nombre_apellido(valor):
                        sql = "SELECT * FROM curso WHERE nombre = '" \
                              + valor + "'"
                        cursor.execute(sql)
                        res = cursor.fetchone()
                        if res is None:
                            showerror("Error al buscar",
                                      "No hay estudiante con el nombre \
                                       ingresado")
                        else:
                            showinfo("Resultado de la busqueda", "DNI: "
                                     + str(res[0])+"\nNombre: " + res[1] +
                                     "\nApellido: " + res[2] +
                                     "\nFecha de Nacimiento: "+res[3])
                            # Observador
                            self.update('consultar_alumno', valor)
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
                            # Observador
                            self.update('consultar_alumno', valor)
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
                            # Observador
                            self.update('consultar_alumno', valor)
                    else:
                        showerror("Error al consultar por Fecha de Nacimiento",
                                  "Verifique el formato del dato ingresado")

    # MODIFICAR

    @modificar_logs
    def modificar_alumno(self, opc, val, tree):
        """
        Se modifica el estudiante seleccionado en la treeview(tabla), \
        asignandole a la opcion(opc) escogida el nuevo valor(val)

        :param opc: Opcion escogida para modificar por el usuario.
        :type opc: IntVar(tkinter)

        :param val: Valor nuevo que se le asignara al dato a modificar
        :type val: StringVar(tkinter)

        :param tree: Variable donde se guarda la treeview(tabla).
        :type tree: Treeview
        """
        try:
            con = sqlite3.connect("estudiantes_curso_2023.db")
            cursor = con.cursor()
        except sqlite3.OperationalError:
            print("Error al conectar a la base de datos")
        else:
            opcion = opc.get()
            valor = str(val.get())
            elem = tree.focus()
            try:
                val_a_modificar = str(tree.item(elem)["values"][0])
            except IndexError:
                print("Error, No se selecciono valor a modificar")
            else:
                match opcion:
                    case 1:
                        if Reg().validar_dni(valor):
                            sql = ("UPDATE curso SET dni = '"
                                   + valor + "' WHERE dni = '"
                                   + val_a_modificar) + "'"
                            cursor.execute(sql)
                            con.commit()
                            # Observador
                            self.update('modificar_alumno', valor)
                        else:
                            showerror("Error al modificar DNI",
                                      "Verifique el formato del dato \
                                      ingresado")
                    case 2:
                        if Reg().validar_nombre_apellido(valor):
                            sql = ("UPDATE curso SET nombre = '"
                                   + valor + "' WHERE dni = '"
                                   + val_a_modificar) + "'"
                            cursor.execute(sql)
                            con.commit()
                            # Observador
                            self.update('modificar_alumno', valor)
                        else:
                            showerror("Error al modificar Nombre",
                                      "Verifique el formato del dato \
                                      ingresado")
                    case 3:
                        if Reg().validar_nombre_apellido(valor):
                            sql = ("UPDATE curso SET apellido = '"
                                   + valor + "' WHERE dni = '"
                                   + val_a_modificar) + "'"
                            cursor.execute(sql)
                            con.commit()
                            # Observador
                            self.update('modificar_alumno', valor)
                        else:
                            showerror("Error al modificar Apellido",
                                      "Verifique el formato del dato \
                                      ingresado")
                    case 4:
                        if Reg().validar_fecha(valor):
                            sql = ("UPDATE curso SET nacimiento = '"
                                   + valor + "' WHERE dni = "
                                   + val_a_modificar)
                            cursor.execute(sql)
                            con.commit()
                            # Observador
                            self.update('modificar_alumno', valor)
                        else:
                            showerror("Error al modificar la Fecha de \
                                      Nacimiento",
                                      "Verifique el formato del dato \
                                      ingresado")
            self.cargar_arbol(tree)
