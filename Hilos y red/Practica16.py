import threading
import time

class hilo(threading.Thread):
    def __init__(self, nombre, intervalo):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo

    def run(self):
        print(f"El hilo {self.nombre} Ha comenzado")
        for i in range(5):
            print(f"El intervalo {self.intervalo} se encuentra en {i}")
            time.sleep(self.intervalo)
        print(f"El hilo {self.nombre} ha finalizado")

hilo1 = hilo("1",2)
hilo2 = hilo("2", 4)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print("Todos los hilos han terminado.")