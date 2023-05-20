from tkinter import Tk
from view import Vista
from observer import Objeto, Observador

if __name__ == "__main__":

    # INICIALIZACION DE OBSERVADOR/ES

    obs = Observador('ObservadorPrimario')
    Objeto().agregar(obs)

    # EJECUCION

    main = Tk()
    Vista().principal(main)
    main.mainloop()
