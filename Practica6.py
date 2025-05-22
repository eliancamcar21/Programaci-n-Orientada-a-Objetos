class Cerveza:
    def mostrar(self):
        print("Caguamon")

class Hielera:
    def __init__(self):
        self.cervezas = []

    def agregar(self, cerveza):
        self.cervezas.append(cerveza)
        print("Agregaste una caguama a la hielera.")

    def sacar(self):
        if self.cervezas:
            self.cervezas.pop(0)
            print("Sacaste una caguama de la hielera.")
        else:
            print("La hielera está vacía.")

h = Hielera()
h.agregar(Cerveza())

h.sacar()
h.sacar()
