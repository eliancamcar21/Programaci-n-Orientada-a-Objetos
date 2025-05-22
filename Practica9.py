from enum import Enum

class Semana(Enum):
    LUNES = "Lunes"
    MARTES = "Martes"
    MIERCOLES = "Miércoles"
    JUEVES = "Jueves"
    VIERNES = "Viernes"
    SABADO = "Sábado"
    DOMINGO = "Domingo"

def validar_dia(dia):
    try:
        if type(dia) is not str:
            raise TypeError("El valor debe ser una cadena de texto.")

        dia_formateado = dia.strip().capitalize()

        if dia_formateado in (dia.value for dia in Semana):
            print(f"Día aceptado: {dia_formateado}")
        else:
            raise ValueError("Día incorrecto. Introduce un día válido de la semana.")

    except TypeError as err:
        print(f"Tipo de dato inválido: {err}")
    except ValueError as err:
        print(f"Valor inválido: {err}")
    finally:
        print("Proceso completado.")

# Pruebas de la función
validar_dia("domingo")        # Día aceptado
validar_dia("Finde")          # Valor inválido
validar_dia(42)               # Tipo de dato inválido
validar_dia(" Miercoles ")    # Día aceptado
