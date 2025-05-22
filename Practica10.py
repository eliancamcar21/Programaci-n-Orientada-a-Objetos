class Pisto:
    def __init__(self, hielera1, hielera2):
        self.__hielera1 = hielera1
        self.hielera2 = hielera2

    def pistear1(self):
        self.__hielera1 = "Vaciar"
        return self.__hielera1
    
    def pistear2(self):
        self.hielera2 = "Esta vacía :'C"
        return self.hielera2
    
#------------------------------
fiesta = Pisto("Cartón en hielera", "Unas cuantas frías")
print(fiesta.pistear1())
print(fiesta.pistear2())
