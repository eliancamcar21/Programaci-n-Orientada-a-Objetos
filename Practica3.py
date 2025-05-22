from math import sqrt, pi, tan

class Figura:
    def __init__(self, numLados, lado):
        self.numLados = numLados
        self.lado = lado
        self.perimetro = self.calculo_perimetro()
        self.area = self.calculo_area()

    def calculo_perimetro(self):
        return self.numLados * self.lado

    def calculo_area(self):
        theta = pi / self.numLados
        apotema = self.lado / (2 * tan(theta))
        area = (self.perimetro * apotema) / 2
        return area

    def mostrar_resultado(self):
        if self.numLados <= 1:
            print("No existen poligonos de un solo lado")
        else:
            print("El perímetro de una figura de",self.numLados,"lados es igual a",self.perimetro,"y el área es igual a",self.area,"unidades")

numLados = int(input("Ingrese el número de lados de la figura: "))
lado = float(input("Ingrese el tamaño del lado: "))

poligono = Figura(numLados, lado)
poligono.mostrar_resultado()