try:
    num = int(input("Ingresa un número para dividir 100: "))
    resultado = 100 / num
    print(f"100 dividido entre {num} es {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Entrada inválida, ingresa un número entero.")

try:
    lista = [1, 2, 3]
    idx = int(input("Ingresa un índice para acceder a la lista: "))
    print(f"Valor en índice {idx}: {lista[idx]}")
except IndexError:
    print("Error: Índice fuera de rango.")
except ValueError:
    print("Error: Entrada inválida, ingresa un número entero.")

try:
    valor = input("Ingresa un número decimal: ")
    num_decimal = float(valor)
    print(f"Número decimal ingresado: {num_decimal}")
except ValueError:
    print("Error: No es un número decimal válido.")
