# Proyecto Final - Sebastian Orellana

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import ImageTk, Image
import os
import tkinter as tk
import sqlite3
import re

main = Tk()

main.title("STools 1.0")

# Logo

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR, "logo.png")

logo1 = Image.open(ruta)
logo = ImageTk.PhotoImage(logo1)
panel = tk.Label(main, image=logo)
panel.grid(row=0, column=0, columnspan=7, pady=10)

# Arbol de datos

tree = ttk.Treeview(main, show="headings", height=14)
tree["columns"] = ("#", "cod", "nombre", "cant", "precio")
tree.column("#", width=50, minwidth=50, anchor=S)
tree.column("cod", width=80, minwidth=50, anchor=S)
tree.column("nombre", width=200, minwidth=200, anchor=S)
tree.column("cant", width=80, minwidth=50, anchor=S)
tree.column("precio", width=80, minwidth=50, anchor=S)

tree.heading("#", text="#")
tree.heading("cod", text="Codigo")
tree.heading("nombre", text="Nombre")
tree.heading("cant", text="Cantidad")
tree.heading("precio", text="Precio")

tree.grid(row=1, column=2, rowspan=14, columnspan=5, padx=20, sticky=N)

# Precio Total

res_total = Label(main, text="TOTAL: $")
res_total.grid(row=14, column=4, sticky=E)

precio = StringVar()


def act_precio():
    total = 0
    for elem in tree.get_children():
        total += int(tree.item(elem, "values")[4])
    precio.set(str(total))


total = Label(main, textvariable=precio)
total.grid(row=14, column=5, sticky=W)

# Apertura de Base de Datos


def crear_base():
    con = sqlite3.connect("lista_clientes_2022.db")
    return con


def borrar_datos():
    for elem in tree.get_children():
        tree.delete(elem)


def tabla_no_existe():
    sql = "SELECT * FROM sqlite_master WHERE type='table'"
    cursor.execute(sql)
    ex = cursor.fetchall()
    return ex == []


def carga_datos():
    if not tabla_no_existe():
        borrar_datos()
        sql = "SELECT * FROM cliente"
        cursor.execute(sql)
        datos = cursor.fetchall()
        for i in range(len(datos)):
            tree.insert("", "end", values=(datos[i][0], datos[i][1], datos[i][2], datos[i][3], datos[i][4]))
    act_precio()


con = crear_base()
cursor = con.cursor()
carga_datos()

# Creacion/Borrado de Clientes


def crear_cliente():
    if tabla_no_existe():
        sql = "CREATE TABLE IF NOT EXISTS cliente(id INTEGER PRIMARY KEY, codigo INTEGER, nombre TEXT, cantidad INTEGER, precio INTEGER)"
        cursor.execute(sql)
        showinfo("Exito al crear", "Cliente creado y cargado al sistema con exito")
    else:
        showerror("Error al crear", "Error: ya hay un cliente creado y cargado en el sistema")


def borrar_cliente():
    confirmar = askyesno("Confirmar", "¿Desea borrar el cliente actual cargado en el sistema?")
    if confirmar:
        if tabla_no_existe():
            showerror("Error al borrar", "Cliente inexistente")
        else:
            sql = "DROP TABLE cliente"
            cursor.execute(sql)
            borrar_datos()
            showinfo("Operacion completada", "Cliente borrado con exito")
    act_precio()


nuevo_c = Button(main, text="Nuevo cliente", command=crear_cliente)
nuevo_c.grid(row=0, columnspan=2, sticky=S)

borrar_c = Button(main, text="Borrar cliente actual", command=borrar_cliente)
borrar_c.grid(row=1, columnspan=2)

# Cargar

patronNombre = "^[a-zA-Z0-9 ,.-]+$"
patronNumeros = "^[0-9]+$"

cargar = Label(main, text="Cargar elemento")
cargar.grid(row=3, columnspan=2, sticky=S,)

carga_codigo = Label(main, text="Codigo")
carga_nombre = Label(main, text="Nombre")
carga_cantidad = Label(main, text="Cantidad")
carga_precio = Label(main, text="Precio($)")
carga_codigo.grid(row=4, column=0, sticky=W, padx=5)
carga_nombre.grid(row=5, column=0, sticky=W, padx=5)
carga_cantidad.grid(row=6, column=0, sticky=W, padx=5)
carga_precio.grid(row=7, column=0, sticky=W, padx=5)

codigo_entry = Entry(main)
nombre_entry = Entry(main)
cantidad_entry = Entry(main)
precio_entry = Entry(main)
codigo_entry.grid(row=4, column=1)
nombre_entry.grid(row=5, column=1)
cantidad_entry.grid(row=6, column=1)
precio_entry.grid(row=7, column=1)


def verifRegEx(codigo, nombre, cant, precio):
    error = 0
    if (not re.match(patronNombre, nombre)):
        showerror("Error al ingresar los datos", "Error, verifique los datos ingresados en el campo nombre")
        error = 1
    if (not re.match(patronNumeros, codigo)):
        showerror("Error al ingresar los datos", "Error, verifique los datos ingresados en el campo codigo ([0-9])")
        error = 1
    if not re.match(patronNumeros, cant):
        showerror("Error al ingresar los datos", "Error, verifique los datos ingresados en el campo cantidad ([0-9])")
        error = 1
    if not re.match(patronNumeros, precio):
        showerror("Error al ingresar los datos", "Error, verifique los datos ingresados en el campo precio ([0-9])")
        error = 1
    return error


contador = 1


def ajuste_id():
    indice = 1
    for elem in tree.get_children():
        tree.set(elem, '#1', indice)
        indice += 1


def cargar_elem():
    global contador
    codigo = codigo_entry.get()
    nombre = nombre_entry.get()
    cant = cantidad_entry.get()
    precio = precio_entry.get()
    if verifRegEx(codigo, nombre, cant, precio) == 0:
        tree.insert("", "end", values=(contador, codigo, nombre, cant, precio))
        contador += 1
        ajuste_id()
        act_precio()
    codigo_entry.delete(0, END)
    nombre_entry.delete(0, END)
    cantidad_entry.delete(0, END)
    precio_entry.delete(0, END)



cargar_boton = Button(main, text="Cargar", width=15, command=cargar_elem)
cargar_boton.grid(row=8, columnspan=2, pady=10)


# Borrar


def borrar_elem():
    global contador
    item = tree.focus()
    tree.delete(item)
    contador -= 1
    ajuste_id()
    act_precio()


borrar_boton = Button(main, text="Borrar", width=15, command=borrar_elem)
borrar_boton.grid(row=9, columnspan=2)

# Modificar


modif_opc = IntVar()


def modificar(): 
    selec = tree.focus()
    opcion = modif_opc.get()
    match opcion:
        case 1:
            nuevo_cod = nuevo_entry.get()
            if (not re.match(patronNumeros, nuevo_cod)):
                showerror("Error al modificar los datos", "Error, verifique el formato del codigo ([0-9])")
            else:
                valor = tree.item(selec)
                arr = valor["values"]
                arr[1] = nuevo_cod
                tree.item(selec, values=(arr[0],arr[1],arr[2], arr[3], arr[4]))
        case 2:
            nuevo_nombre = nuevo_entry.get()
            if (not re.match(patronNombre, nuevo_nombre)):
                showerror("Error al modificar los datos", "Error, verifique el formato del nombre")
            else:
                valor = tree.item(selec)
                arr = valor["values"]
                arr[2] = nuevo_nombre
                tree.item(selec, values=(arr[0],arr[1],arr[2], arr[3], arr[4]))
        case 3:
            nueva_cant = nuevo_entry.get()
            if (not re.match(patronNumeros, nueva_cant)):
                showerror("Error al modificar los datos", "Error, verifique el formato de la cantidad ([0-9])")
            else:
                valor = tree.item(selec)
                arr = valor["values"]
                arr[3] = nueva_cant
                tree.item(selec, values=(arr[0],arr[1],arr[2], arr[3], arr[4]))
        case 4:
            nuevo_precio = nuevo_entry.get()
            if (not re.match(patronNumeros, nuevo_precio)):
                showerror("Error al modificar los datos", "Error, verifique el formato del precio ([0-9])")
            else:
                valor = tree.item(selec)
                arr = valor["values"]
                arr[4] = nuevo_precio
                tree.item(selec, values=(arr[0],arr[1],arr[2], arr[3], arr[4]))
    nuevo_entry.delete(0, END)
    act_precio()


modif = Label(main, text="Modificar valor")
modif.grid(row=10, columnspan=2, sticky=S, pady=5)

opc_codigo = Radiobutton(main, text="Codigo", value=1, variable=modif_opc)
opc_codigo.grid(row=11, column=0, sticky=W, padx=10)
opc_nombre = Radiobutton(main, text="Nombre", value=2, variable=modif_opc)
opc_nombre.grid(row=11, column=1, sticky=W, padx=20)
opc_cantidad = Radiobutton(main, text="Cantidad", value=3, variable=modif_opc)
opc_cantidad.grid(row=12, column=0, sticky=S, padx=10)
opc_precio = Radiobutton(main, text="Precio", value=4, variable=modif_opc)
opc_precio.grid(row=12, column=1, sticky=W, padx=20)

nuevo_val = Label(main, text="Nuevo Valor")
nuevo_val.grid(row=13, column=0, pady=8)
nuevo_entry = Entry(main)
nuevo_entry.grid(row=13, column=1, pady=8)

modif_boton = Button(main, text="Modificar", width=15, command=modificar)
modif_boton.grid(row=14, columnspan=2, pady=10)

# Consultar


def consulta_precio_total():
    sql = "SELECT precio FROM cliente"
    cursor.execute(sql)
    res = cursor.fetchall()
    precio_total = 0
    for i in res:
        precio_total += i[0]
    return precio_total


def consulta():
    sql = "SELECT COUNT(*) FROM cliente"
    cursor.execute(sql)
    res = cursor.fetchone()
    cant_art_dist = res[0]
    sql = "SELECT cantidad FROM cliente"
    cursor.execute(sql)
    res = cursor.fetchall()
    cant_art_total = 0
    for i in res:
        cant_art_total += i[0]
    precio_total = consulta_precio_total()
    showinfo("Resultado de la Consulta", "Estado actual de la base de datos del cliente:\n\nCantidad de articulos distintos cargados: " + str(cant_art_dist) + "\nCantidad total de articulos cargados: " + str(cant_art_total) + "\nPrecio total de los elementos: $" + str(precio_total))


consul_boton = Button(main, text="Consultar Informacion", command=consulta)
consul_boton.grid(row=14, column=2)

# Guardar datos del cliente


def guardar_datos():
    lista_elem = []
    sql = "DELETE FROM cliente"
    cursor.execute(sql)
    for elem in tree.get_children():
        lista_elem.append(tuple(tree.item(elem)["values"]))
    for elem in lista_elem:
        sql = "INSERT INTO cliente(id, codigo, nombre, cantidad, precio) VALUES (?,?,?,?,?)"
        cursor.execute(sql, elem)
    con.commit()
    showinfo("Archivo Guardado", "Datos guardados con exito")


guardar = Button(main, text="Guardar Datos", command=guardar_datos)
guardar.grid(row=14, column=3)

main.mainloop()
con.close()