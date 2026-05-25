import time

def es_valida(tablero):

    n = len(tablero)

    # Revisar cada par de reinas
    for i in range(n):

        for j in range(i + 1, n):

            # Misma columna
            if tablero[i] == tablero[j]:
                return False

            # Misma diagonal
            if abs(tablero[i] - tablero[j]) == abs(i - j):
                return False

    return True



def es_segura(tablero, fila, col):

    # Revisar filas anteriores
    for i in range(fila):

        # Misma columna
        if tablero[i] == col:
            return False

        # Misma diagonal
        if abs(tablero[i] - col) == abs(i - fila):
            return False

    return True


def resolver_backtracking(tablero, fila, n):

    # Caso base
    if fila == n:
        return True

    # Probar columnas
    for col in range(n):

        if es_segura(tablero, fila, col):

            # Colocar reina
            tablero[fila] = col

            # Resolver siguiente fila
            if resolver_backtracking(tablero, fila + 1, n):
                return True

            # Backtrack
            tablero[fila] = -1

    return False


def resolver_n_reinas(n):

    tablero = [-1] * n

    if resolver_backtracking(tablero, 0, n):
        return tablero

    return None



# IMPRIMIR TABLERO 


def imprimir_tablero(tablero):

    if tablero is None:
        print("No existe solución")
        return

    n = len(tablero)

    print()

    for fila in range(n):

        for col in range(n):

            if tablero[fila] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

    print()



def contar_backtracking(tablero, fila, n):

    # Solución completa encontrada
    if fila == n:
        return 1

    total = 0

    # Probar columnas
    for col in range(n):

        if es_segura(tablero, fila, col):

            # Colocar reina
            tablero[fila] = col

            # Contar soluciones
            total += contar_backtracking(tablero, fila + 1, n)

            # Backtrack
            tablero[fila] = -1

    return total


def contar_soluciones(n):

    tablero = [-1] * n

    return contar_backtracking(tablero, 0, n)


# =========================================================
# MEDICIÓN DE TIEMPOS
# =========================================================

def medir_tiempo(n):

    inicio = time.time()

    total = contar_soluciones(n)

    fin = time.time()

    tiempo = fin - inicio

    return total, tiempo


# =========================================================
# PRUEBA DEL VERIFICADOR
# =========================================================

print("=================================================")
print("PRUEBA DEL VERIFICADOR")
print("=================================================")

tablero1 = [1, 3, 0, 2]
tablero2 = [0, 1, 2, 3]

print("\nTablero 1:", tablero1)
print("¿Es válido?", es_valida(tablero1))

print("\nTablero 2:", tablero2)
print("¿Es válido?", es_valida(tablero2))



print("\n=================================================")
print("BUSCAR UNA SOLUCIÓN")
print("=================================================")

for n in range(1, 9):

    print("\nN =", n)

    solucion = resolver_n_reinas(n)

    if solucion is None:
        print("No existe solución")
    else:
        print("Solución encontrada:")
        print(solucion)

        imprimir_tablero(solucion)


# =========================================================
# TABLA DE SOLUCIONES
# =========================================================

print("\n=================================================")
print("TABLA DE SOLUCIONES")
print("=================================================")

print("\nN\tSoluciones")

for n in range(1, 9):

    total = contar_soluciones(n)

    print(f"{n}\t{total}")


# =========================================================
# MEDICIÓN DE TIEMPOS
# =========================================================

print("\n=================================================")
print("MEDICIÓN DE TIEMPOS")
print("=================================================")

valores = [4, 6, 8, 10, 12]

tiempos = []

for n in valores:

    total, tiempo = medir_tiempo(n)

    tiempos.append(tiempo)

    print(f"\nN = {n}")
    print("Soluciones =", total)
    print("Tiempo =", tiempo, "segundos")


# =========================================================
# TEST DE DOBLAMIENTO
# =========================================================

print("\n=================================================")
print("TEST DE DOBLAMIENTO")
print("=================================================")

for i in range(1, len(tiempos)):

    razon = tiempos[i] / tiempos[i - 1]

    print(
        f"r({valores[i]}) = "
        f"{tiempos[i]:.6f} / {tiempos[i - 1]:.6f} "
        f"= {razon:.4f}"
    )

