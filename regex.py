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
    """
    Clase utilizada para realizar toda la validacion de datos que el usuario \
    ingresa en los distintos campos de la aplicacion
    """
    def validar_fecha(self, string):
        """
        Se verifica si la fecha ingresada cumple el formato **DD/MM/AAAA** \n
        Donde: \n
        DD: Dias del año, cuyo valor varia entre 01-31 \n
        MM: Meses del año, cuyo valor varia entre 01-12 \n
        AAAA: Año de nacimiento, cuyo valor varia entre 1900-2019 \n

        :param string: Cadena que contiene la fecha de nacimiento a verificar
        :type string: Str
        """
        patron = ("^(0[1-9]|1[0-9]|2[0-9]|3[0-1])"
                  "(/)(0[1-9]|1[0-2])(/)(19[0-9][0-9]|20[0-1][0-9])$")
        return re.match(patron, str(string))

    def validar_dni(self, string):
        """
        Se verifica si el DNI ingresado cumple uno de los siguientes \
        formatos: \n
        * 7 numeros sin ningun caracter especial \
        (Ej: puntos, comas o guiones) \n
        * 8 numeros sin ningun caracter especial \
        (Ej: puntos, comas o guiones) \n

        :param string: Cadena que contiene el dni a verificar
        :type string: Str
        """
        patron = r'\d{7,8}$'
        return re.match(patron, str(string))

    def validar_nombre_apellido(self, string):
        """
        Se verifica si el nombre o el apellido ingresado cumple las \
        siguientes condiciones: \n
        * Cadena de entre un y quince letras del alfabeto [1 - 15] \n
        * Cadena sin ningun caracter especial (Ej: puntos, comas o guiones) \n
        * Sin distincion entre mayusculas y minusculas \n

        :param string: Cadena que contiene el nombre o apellido a verificar
        :type string: Str
        """
        patron = "^[A-Za-z]{1,15}$"
        return re.match(patron, str(string))
