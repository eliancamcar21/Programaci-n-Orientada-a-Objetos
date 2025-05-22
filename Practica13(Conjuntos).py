def operacionesConNumeros():
    conjunto = {1, 2, 3, 4, 5}
    print(conjunto)

    conjunto.add(6)
    print(conjunto)

    conjunto.remove(1)
    print(conjunto)

    print(10 in conjunto)

    conjunto.add(1)
    conjunto.add(2)
    print(conjunto)
    return conjunto

def operacionesConTextos():
    conjunto = {"Uno", "Dos", "Tres", "Cuatro", "Cinco"}
    print(conjunto)

    conjunto.add("Siete")
    print(conjunto)
    return conjunto

def operacionesEntreConjuntos():
    A = {1, 2, 3}
    B = {3, 4, 5}

    union = B.union(A)
    print(union)

    interseccion = B.intersection(A)
    print(interseccion)

    diferencia = A.difference(B)
    print(diferencia)

def ejecutar():
    print("--------- CONJUNTO NUMÉRICO ---------")
    operacionesConNumeros()
    print("--------- CONJUNTO DE TEXTO ---------")
    operacionesConTextos()
    print("--------- OPERACIONES ENTRE CONJUNTOS ---------")
    operacionesEntreConjuntos()

ejecutar()
