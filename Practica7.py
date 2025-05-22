class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def dormir(self):
        print(f"El {self.especie} está durmiendo")

    def mostrar_info(self):
        print(f"Especie: {self.especie}, Edad: {self.edad} años")

class Perro(Animal):
    def __init__(self, especie, edad, raza):
        super().__init__(especie, edad)
        self.raza = raza

    def ladrar(self):
        print(f"El perro de raza {self.raza} está ladrando")

mascota = Perro("Canino", 4, "Labrador")
mascota.dormir()
mascota.mostrar_info()
mascota.ladrar()
