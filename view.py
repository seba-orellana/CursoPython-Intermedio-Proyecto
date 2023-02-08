from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Radiobutton
from tkinter import ttk
from tkinter import StringVar, IntVar

from model import crear_base


def principal(main):
    main.title("Estudiantes Universidad 2023")
    crear_base()

    # TREEVIEW

    tree = ttk.Treeview(main, show="headings", height=25)
    tree["columns"] = ("#", "cod", "nombre", "cant", "precio")
    tree.column("#", width=50, minwidth=50, anchor="s")
    tree.column("cod", width=80, minwidth=50, anchor="s")
    tree.column("nombre", width=200, minwidth=200, anchor="s")
    tree.column("cant", width=80, minwidth=50, anchor="s")
    tree.column("precio", width=80, minwidth=50, anchor="s")

    tree.heading("#", text="#")
    tree.heading("cod", text="Codigo")
    tree.heading("nombre", text="Nombre")
    tree.heading("cant", text="Cantidad")
    tree.heading("precio", text="Precio")

    tree.grid(row=1, column=2, rowspan=18, columnspan=5, padx=20, sticky="n")

    # CREAR/BORRAR CURSO

    nuevo_c = Button(main, text="Nuevo curso")
    nuevo_c.grid(row=0, columnspan=2, sticky="s", pady=10)

    borrar_c = Button(main, text="Borrar curso")
    borrar_c.grid(row=1, columnspan=2)

    # CARGAR ESTUDIANTE

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

    dni = StringVar()
    nombre = StringVar()
    apellido = StringVar()
    nac = IntVar()

    dni_entry = Entry(main, textvariable=dni)
    nombre_entry = Entry(main, textvariable=nombre)
    apellido_entry = Entry(main, textvariable=apellido)
    nac_entry = Entry(main, textvariable=nac)
    dni_entry.grid(row=4, column=1)
    nombre_entry.grid(row=5, column=1)
    apellido_entry.grid(row=6, column=1)
    nac_entry.grid(row=7, column=1)

    # CARGAR ESTUDIANTE (BOTON)

    cargar_boton = Button(main, text="Cargar", width=15)
    cargar_boton.grid(row=8, columnspan=2, pady=10)

    # BORRAR ESTUDIANTE (BOTON)

    borrar_boton = Button(main, text="Borrar", width=15)
    borrar_boton.grid(row=9, columnspan=2)

    # MODIFICAR ESTUDIANTE

    modif = Label(main, text="Modificar datos")
    modif.grid(row=10, columnspan=2, sticky="s", pady=5)

    opc_dni = Radiobutton(main, text="DNI", value=1)
    opc_dni.grid(row=11, column=0, sticky="w", padx=28)
    opc_nombre = Radiobutton(main, text="Nombre", value=2)
    opc_nombre.grid(row=11, column=1, sticky="w", padx=20)
    opc_apellido = Radiobutton(main, text="Apellido", value=3)
    opc_apellido.grid(row=12, column=0, sticky="s", padx=10)
    opc_nac = Radiobutton(main, text="Fecha de Nacimiento", value=4)
    opc_nac.grid(row=12, column=1, sticky="w", padx=20)

    valor = StringVar()

    nuevo_val = Label(main, text="Nuevo Valor")
    nuevo_val.grid(row=13, column=0, pady=8)
    nuevo_entry = Entry(main, textvariable=valor)
    nuevo_entry.grid(row=13, column=1, pady=8)

    # MODIFICAR (BOTON)

    modif_boton = Button(main, text="Modificar", width=15)
    modif_boton.grid(row=14, columnspan=2, pady=10)

    # CONSULTAR ESTUDIANTE

    consul = Label(main, text="Consultar por datos")
    consul.grid(row=15, columnspan=2, sticky="s", pady=5)

    c_opc_dni = Radiobutton(main, text="DNI", value=1)
    c_opc_dni.grid(row=16, column=0, sticky="w", padx=28)
    c_opc_nombre = Radiobutton(main, text="Nombre", value=2)
    c_opc_nombre.grid(row=16, column=1, sticky="w", padx=20)
    c_opc_apellido = Radiobutton(main, text="Apellido", value=3)
    c_opc_apellido.grid(row=17, column=0, sticky="s", padx=10)
    c_opc_nac = Radiobutton(main, text="Fecha de Nacimiento", value=4)
    c_opc_nac.grid(row=17, column=1, sticky="w", padx=20)

    c_valor = StringVar()

    nuevo_val = Label(main, text="Dato a consultar:")
    nuevo_val.grid(row=18, column=0, pady=8)
    nuevo_entry = Entry(main, textvariable=c_valor)
    nuevo_entry.grid(row=18, column=1, pady=8)

    # CONSULTAR (BOTON)

    modif_boton = Button(main, text="Consultar", width=15)
    modif_boton.grid(row=19, columnspan=2, pady=10)
