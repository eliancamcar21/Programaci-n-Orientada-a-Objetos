import numpy as np  # Esta es la forma correcta

Mi_lista = [1, "Chuchin", 2, "Albertano", 3]
array = np.array([1, 2, 3, 4, 5])

# Convertir a un conjunto — unimos ambos, convirtiendo el array a lista primero
conjunto = set(Mi_lista + list(array))
print("Conjunto:", conjunto)

# Convertir a tupla — concatenamos ambas como tuplas
Convertir_tupla = tuple(Mi_lista) + tuple(array)
print("Tupla:", Convertir_tupla)

# Convertir a diccionario — corregido el signo "=" por ":" y las claves
diccionario = {
    "Nombre": ["Pedro Picapedra", "Malagon", "Ozuna"],
    "edad": ["99999", "30", "200"],
    "nacionalidad": ["USA", "Mexico", "Puerto Rico"]
}
print("Diccionario:", diccionario)
