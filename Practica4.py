class Cuenta:
    def __init__(self, nombre, nip, saldo):
        self.nombre = nombre
        self.__nip = nip
        self.__saldo = saldo

    def mostrar_saldo(self, nip):
        if nip == self.__nip:
            return f"Saldo actual: ${self.__saldo}"
        else:
            return "NIP incorrecto"

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: ${self.__saldo}"
        else:
            return "Cantidad inválida para depósito."

    def retirar(self, cantidad, nip):
        if nip != self.__nip:
            return "NIP incorrecto"
        if cantidad <= 0:
            return "Cantidad inválida para retiro"
        if cantidad > self.__saldo:
            return "Fondos insuficientes"
        self.__saldo -= cantidad
        return f"Retiro exitoso. Saldo restante: ${self.__saldo}"


cuenta = Cuenta("Ludovico PLuche", 1111, 500)

print(cuenta.nombre)                        # LudovicoPluche
print(cuenta.mostrar_saldo(1111))           # $500
print(cuenta.mostrar_saldo(1234))           # NIP incorrecto
print(cuenta.depositar(250))                # Depósito exitoso. Nuevo saldo: $750
print(cuenta.retirar(100, 1111))            # Retiro exitoso. Saldo restante: $650
print(cuenta.retirar(700, 1111))            # Fondos insuficientes
print(cuenta.retirar(-50, 1111))            # Cantidad inválida para retiro
print(cuenta.retirar(50, 1234))             # NIP incorrecto
