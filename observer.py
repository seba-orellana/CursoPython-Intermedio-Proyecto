class Objeto():
    observadores = []

    def agregar(self, ob):
        self.observadores.append(ob)

    def eliminar(self, ob):
        self.observadores.remove(ob)

    def update(self, *args):
        for obs in self.observadores:
            obs.update(args)


class Observador():
    def __init__(self, nombre):
        self.nombre = nombre

    def update(self, *args):
        print("Actualizacion realizada en", self.nombre)
        print("Parametros involucrados: \n", args)
        print("---------------------------")
