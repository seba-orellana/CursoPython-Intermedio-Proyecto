import re

# REGEX

# FORMATO PARA VALIDAR LOS DATOS:

# DNI: 7 U 8 DIGITOS SIN PUNTOS
# NOMBRE: DE 1 A 15 LETRAS MAYUSCULAS O MINUSCULAS
# APELLIDO: DE 1 A 15 LETRAS MAYUSCULAS O MINUSCULAS
# FECHA: DD/MM/AAAA
# DD=[01-31]
# MM=[01-12]
# AAAA=[1900-2019]


class Reg():
    def validar_fecha(self, string):
        patron = ("^(0[1-9]|1[0-9]|2[0-9]|3[0-1])"
                  "(/)(0[1-9]|1[0-2])(/)(19[0-9][0-9]|20[0-1][0-9])$")
        return re.match(patron, str(string))

    def validar_dni(self, string):
        patron = r'\d{7,8}$'
        return re.match(patron, str(string))

    def validar_nombre_apellido(self, string):
        patron = "^[A-Za-z]{1,15}$"
        return re.match(patron, str(string))