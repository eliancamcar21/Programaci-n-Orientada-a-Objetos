import math
from math import sqrt
from math import radians
from math import tan

class Figura:
    def area(self, nLados, vLado):
        if nLados == 3:
            # Triángulo 
            altura = (sqrt(3) / 2) * vLado
            areaFigura = (vLado * altura) / 2
            print(f"El área del triángulo es: {areaFigura}")

        elif nLados == 4:
            # Cuadrado
            areaFigura = vLado ** 2
            print(f"El área del cuadrado es: {areaFigura}")

        elif nLados > 4:
            # Polígono regular
            angulo = radians(180 / nLados)
            apotema = vLado / (2 * tan(angulo))
            perimetro = vLado * nLados
            areaFigura = (perimetro * apotema) / 2
            print(f"El área del polígono es: {areaFigura}")

        else:
            print("Número de lados no válido para calcular el área.")

    def perimetro(self, nLados, vLado):
        if nLados >= 3:
            perimetroFigura = vLado * nLados
            print(f"El perímetro de la figura es: {perimetroFigura}")
        else:
            print("Número de lados no válido para calcular el perímetro.")

unaFigura = Figura()
unaFigura.area(3, 4)
unaFigura.perimetro(3, 3)

