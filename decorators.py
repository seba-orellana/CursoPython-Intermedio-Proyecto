import datetime

# SE ENVIAN LOGS A UN TXT MEDIANTE LOS DECORADORES AL CREAR, BORRAR, CONSULTAR
# O MODIFICAR UN ALUMNO


def agregar_logs(func):
    def env(*args, **kwargs):
        file = open("registro_log.txt", "a")
        file.write(str(datetime.datetime.today().strftime("%d/%m/%y"))
                   + "\t" + str(datetime.datetime.today().strftime("%H:%M:%S"))
                   + "\t Registro agregado a la base de datos \n"
                   )
        return func(*args, **kwargs)
    return env


def borrar_logs(func):
    def env(*args, **kwargs):
        file = open("registro_log.txt", "a")
        file.write(str(datetime.datetime.today().strftime("%d/%m/%y"))
                   + "\t" + str(datetime.datetime.today().strftime("%H:%M:%S"))
                   + "\t Se ha eliminado un registro de la base de datos \n"
                   )
        return func(*args, **kwargs)
    return env


def modificar_logs(func):
    def env(*args, **kwargs):
        file = open("registro_log.txt", "a")
        file.write(str(datetime.datetime.today().strftime("%d/%m/%y"))
                   + "\t" + str(datetime.datetime.today().strftime("%H:%M:%S"))
                   + "\t Registro modificado en la base de datos \n"
                   )
        return func(*args, **kwargs)
    return env
