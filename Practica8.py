class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        pass

class Perro(Animal):
    def hacerSonido(self):
        return "guau"

class Gato(Animal):
    def hacerSonido(self):
        return "miau"

class Caballo(Animal):
    def hacerSonido(self):
        return "brrrf"

unAnimal = Perro("Guau")
otroAnimal = Gato("Miau")
Animal = Caballo("Brrrf")

print(unAnimal.nombre, unAnimal.hacerSonido())
print(otroAnimal.nombre, otroAnimal.hacerSonido())
print(Animal.nombre, Animal.hacerSonido())
