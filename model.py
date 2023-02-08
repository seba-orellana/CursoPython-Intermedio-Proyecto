import sqlite3


def crear_base():
    con = sqlite3.connect("estudiantes_curso_2023.db")
    return con


con = crear_base()
cursor = con.cursor()


def tabla_no_existe():
    sql = "SELECT * FROM sqlite_master WHERE type='table'"
    cursor.execute(sql)
    ex = cursor.fetchall()
    return ex == []
