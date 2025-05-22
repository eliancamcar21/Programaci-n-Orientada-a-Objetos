class ListaInteractiva:
    def __init__(self):
        self.elementos = []
        self.opcion = 0
        self.activo = True

    def mostrar_menu(self):
        print("----- MENÚ -----")
        print("1 - Agregar")
        print("2 - Eliminar")
        print("3 - Editar")
        print("4 - Ver lista")
        print("5 - Salir")
        try:
            self.opcion = int(input("Seleccione una opción: "))
        except ValueError:
            self.opcion = 0

        if self.opcion == 5:
            self.activo = False

    def ejecutar(self):
        while self.activo:
            match self.opcion:
                case 1:
                    self.agregar()
                case 2:
                    self.eliminar()
                case 3:
                    self.editar()
                case 4:
                    self.mostrar()
                case _:
                    print("Opción inválida.")
            if self.activo:
                self.mostrar_menu()

    def agregar(self):
        try:
            valor = int(input("Ingrese un número: "))
            self.elementos.append(valor)
        except ValueError:
            print("Entrada no válida.")

    def eliminar(self):
        if not self.elementos:
            print("La lista está vacía.")
            return
        self.mostrar()
        try:
            idx = int(input("Posición a eliminar: ")) - 1
            if 0 <= idx < len(self.elementos):
                self.elementos.pop(idx)
            else:
                print("Posición inválida.")
        except ValueError:
            print("Entrada no válida.")

    def editar(self):
        if not self.elementos:
            print("La lista está vacía.")
            return
        self.mostrar()
        try:
            idx = int(input("Posición a editar: ")) - 1
            if 0 <= idx < len(self.elementos):
                nuevo_valor = int(input("Nuevo valor: "))
                self.elementos[idx] = nuevo_valor
            else:
                print("Posición inválida.")
        except ValueError:
            print("Entrada no válida.")

    def mostrar(self):
        print("Lista actual:", self.elementos)


app = ListaInteractiva()
app.mostrar_menu()
app.ejecutar()