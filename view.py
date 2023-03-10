from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Radiobutton
from tkinter import ttk
from tkinter import StringVar, IntVar

from model import Estudiante
from db import Base


class Vista():
    def __init__(self):
        pass

    def principal(self, main):
        main.title("Estudiantes Universidad 2023")
        self.colocar_arbol(main)
        self.crear_borrar_curso(main)
        self.cargar_estudiante(main)
        self.borrar_estudiante(main)
        self.modificar_estudiante(main)
        self.consultar_estudiante(main)
        if Base().tabla_existe():
            Estudiante().cargar_arbol(tree)

    # TREEVIEW

    tree = None

    def colocar_arbol(self, main):
        global tree
        tree = ttk.Treeview(main, show="headings", height=25)
        tree["columns"] = ("DNI", "nombre", "apellido", "nacimiento")
        tree.column("DNI", width=80, minwidth=50, anchor="s")
        tree.column("nombre", width=200, minwidth=200, anchor="s")
        tree.column("apellido", width=80, minwidth=50, anchor="s")
        tree.column("nacimiento", width=80, minwidth=50, anchor="s")

        tree.heading("DNI", text="DNI")
        tree.heading("nombre", text="Nombre")
        tree.heading("apellido", text="Apellido")
        tree.heading("nacimiento", text="Nacimiento")

        tree.grid(row=1, column=2, rowspan=18, columnspan=5, padx=20,
                  sticky="n")

    # CREAR/BORRAR CURSO

    def crear_borrar_curso(self, main):
        nuevo_c = Button(main, text="Nuevo curso",
                         command=Base().crear_tabla)
        nuevo_c.grid(row=0, columnspan=2, sticky="s", pady=10)

        borrar_c = Button(main, text="Borrar curso",
                          command=lambda: Base().borrar_tabla(tree))
        borrar_c.grid(row=1, columnspan=2)

    # CARGAR ESTUDIANTE

    def borrar_info(self, info):
        info.delete(0, "end")

    def cargar_estudiante(self, main):
        dni_valor = StringVar()
        nombre_valor = StringVar()
        apellido_valor = StringVar()
        nac_valor = StringVar()

        cargar = Label(main, text="Cargar estudiante al curso")
        cargar.grid(row=3, columnspan=2, sticky="s")

        carga_dni = Label(main, text="DNI")
        carga_nombre = Label(main, text="Nombre")
        carga_apellido = Label(main, text="Apellido")
        carga_nac = Label(main, text="Fecha de Nacimiento")

        carga_dni.grid(row=4, column=0, sticky="w", padx=5)
        carga_nombre.grid(row=5, column=0, sticky="w", padx=5)
        carga_apellido.grid(row=6, column=0, sticky="w", padx=5)
        carga_nac.grid(row=7, column=0, sticky="w", padx=5)

        dni_entry = Entry(main, textvariable=dni_valor)
        nombre_entry = Entry(main, textvariable=nombre_valor)
        apellido_entry = Entry(main, textvariable=apellido_valor)
        nac_entry = Entry(main, textvariable=nac_valor)

        dni_entry.insert(0, "123456789")
        dni_entry.bind("<FocusIn>", lambda event:
                       self.borrar_info(dni_entry))

        nombre_entry.insert(0, "Nombre")
        nombre_entry.bind("<FocusIn>", lambda event:
                          self.borrar_info(nombre_entry))

        apellido_entry.insert(0, "Apellido")
        apellido_entry.bind("<FocusIn>", lambda event:
                            self.borrar_info(apellido_entry))

        nac_entry.insert(0, "DD/MM/AAAA")
        nac_entry.bind("<FocusIn>", lambda event:
                       self.borrar_info(nac_entry))

        dni_entry.grid(row=4, column=1)
        nombre_entry.grid(row=5, column=1)
        apellido_entry.grid(row=6, column=1)
        nac_entry.grid(row=7, column=1)

        # CARGAR ESTUDIANTE (BOTON)

        cargar_boton = Button(main, text="Cargar", width=15,
                              command=lambda: Estudiante().insertar_alumno
                              (dni_valor, nombre_valor,
                               apellido_valor, nac_valor, tree))
        cargar_boton.grid(row=8, columnspan=2, pady=10)

    # BORRAR ESTUDIANTE

    def borrar_estudiante(self, main):
        borrar_boton = Button(main, text="Borrar", width=15, command=lambda:
                              Estudiante().borrar_alumno(tree))
        borrar_boton.grid(row=9, columnspan=2)

    # MODIFICAR ESTUDIANTE

    def modificar_estudiante(self, main):
        modif_opc = IntVar()
        valor = StringVar()

        modif = Label(main, text="Modificar datos")
        modif.grid(row=10, columnspan=2, sticky="s", pady=5)

        opc_dni = Radiobutton(main, text="DNI", value=1, variable=modif_opc)
        opc_dni.grid(row=11, column=0, sticky="w", padx=28)
        opc_nombre = Radiobutton(main, text="Nombre", value=2,
                                 variable=modif_opc)
        opc_nombre.grid(row=11, column=1, sticky="w", padx=20)
        opc_apellido = Radiobutton(main, text="Apellido", value=3,
                                   variable=modif_opc)
        opc_apellido.grid(row=12, column=0, sticky="s", padx=10)
        opc_nac = Radiobutton(main, text="Fecha de Nacimiento", value=4,
                              variable=modif_opc)
        opc_nac.grid(row=12, column=1, sticky="w", padx=20)

        nuevo_val = Label(main, text="Nuevo Valor")
        nuevo_val.grid(row=13, column=0, pady=8)
        nuevo_entry = Entry(main, textvariable=valor)
        nuevo_entry.grid(row=13, column=1, pady=8)

        # MODIFICAR (BOTON)

        modif_boton = Button(main, text="Modificar", width=15,
                             command=lambda: Estudiante().modificar_alumno
                             (modif_opc, valor, tree))
        modif_boton.grid(row=14, columnspan=2, pady=10)

    # CONSULTAR ESTUDIANTE

    def consultar_estudiante(self, main):
        c_valor = StringVar()
        consul_opc = IntVar()

        consul = Label(main, text="Consultar por datos")
        consul.grid(row=15, columnspan=2, sticky="s", pady=5)

        c_opc_dni = Radiobutton(main, text="DNI", value=1, variable=consul_opc)
        c_opc_dni.grid(row=16, column=0, sticky="w", padx=28)
        c_opc_nombre = Radiobutton(main, text="Nombre", value=2,
                                   variable=consul_opc)
        c_opc_nombre.grid(row=16, column=1, sticky="w", padx=20)
        c_opc_apellido = Radiobutton(main, text="Apellido", value=3,
                                     variable=consul_opc)
        c_opc_apellido.grid(row=17, column=0, sticky="s", padx=10)
        c_opc_nac = Radiobutton(main, text="Fecha de Nacimiento", value=4,
                                variable=consul_opc)
        c_opc_nac.grid(row=17, column=1, sticky="w", padx=20)

        consul_val = Label(main, text="Dato a consultar:")
        consul_val.grid(row=18, column=0, pady=8)
        consul_entry = Entry(main, textvariable=c_valor)
        consul_entry.grid(row=18, column=1, pady=8)

        # CONSULTAR (BOTON)

        modif_boton = Button(main, text="Consultar", width=15,
                             command=lambda: Estudiante().consultar_alumno
                             (consul_opc, c_valor))
        modif_boton.grid(row=19, columnspan=2, pady=10)
