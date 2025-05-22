import math
from math import sqrt, radians, tan

class Figura:
    nLados = 0
    vLado = 0

    def area(self):
        if self.nLados == 3:
            altura = (sqrt(3) / 2) * self.vLado
            areaFigura = (self.vLado * altura) / 2
            print(f"El área del triángulo es: {areaFigura}")

        elif self.nLados == 4:
            areaFigura = self.vLado ** 2
            print(f"El área del cuadrado es: {areaFigura}")

        elif self.nLados > 4:
            angulo = radians(180 / self.nLados)
            apotema = self.vLado / (2 * tan(angulo))
            perimetro = self.vLado * self.nLados
            areaFigura = (perimetro * apotema) / 2
            print(f"El área del polígono es: {areaFigura}")

        else:
            print("Número de lados no válido para calcular el área.")

    def perimetro(self):
        if self.nLados >= 3:
            perimetroFigura = self.vLado * self.nLados
            print(f"El perímetro de la figura es: {perimetroFigura}")
        else:
            print("Número de lados no válido para calcular el perímetro.")

unaFigura = Figura()
unaFigura.nLados = 3
unaFigura.vLado = 4
unaFigura.area()

unaFigura.nLados = 3
unaFigura.vLado = 3
unaFigura.perimetro()
