import time

# ============================================================
# LABERINTOS DE PRUEBA
# ============================================================

LABERINTO_5x5 = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
]

LABERINTO_SIN_SALIDA = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 1, 0],
]

LABERINTO_SIMPLE = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


# ============================================================
# PARTE 3A – ENCONTRAR UN CAMINO
# ============================================================

def existe_camino(laberinto: list, fila: int, col: int,
                  visitados: set, ruta: list) -> bool:

    filas = len(laberinto)
    cols = len(laberinto[0])

    # Fuera de límites
    if fila < 0 or fila >= filas or col < 0 or col >= cols:
        return False

    # Pared
    if laberinto[fila][col] == 1:
        return False

    # Ya visitada
    if (fila, col) in visitados:
        return False

    # Llegamos a la salida
    if fila == filas - 1 and col == cols - 1:
        ruta.append((fila, col))
        return True

    # Marcar visitada
    visitados.add((fila, col))
    ruta.append((fila, col))

    # Direcciones
    direcciones = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for df, dc in direcciones:
        nueva_fila = fila + df
        nueva_col = col + dc

        if existe_camino(laberinto, nueva_fila, nueva_col,
                         visitados, ruta):
            return True

    # Backtrack
    visitados.discard((fila, col))
    ruta.pop()

    return False


# ============================================================
# PARTE 3B – VISUALIZACIÓN
# ============================================================

def imprimir_laberinto(laberinto: list, visitados: set,
                       ruta: list, paso: int) -> None:

    filas = len(laberinto)
    cols = len(laberinto[0])

    ruta_set = set(ruta)

    print(f"\n--- Paso {paso} ---")

    for i in range(filas):

        fila_texto = ""

        for j in range(cols):

            if (i, j) == (0, 0):
                simbolo = "S"

            elif (i, j) == (filas - 1, cols - 1):
                simbolo = "E"

            elif laberinto[i][j] == 1:
                simbolo = "#"

            elif (i, j) in ruta_set:
                simbolo = "·"

            elif (i, j) in visitados:
                simbolo = "*"

            else:
                simbolo = "."

            fila_texto += simbolo + " "

        print(fila_texto)

    time.sleep(0.2)


def encontrar_camino(laberinto: list, verbose: bool = False) -> list | None:

    visitados = set()
    ruta = []

    pasos = [0]

    def backtrack(fila, col):

        pasos[0] += 1

        if verbose:
            imprimir_laberinto(laberinto, visitados, ruta, pasos[0])

        filas = len(laberinto)
        cols = len(laberinto[0])

        if fila < 0 or fila >= filas or col < 0 or col >= cols:
            return False

        if laberinto[fila][col] == 1:
            return False

        if (fila, col) in visitados:
            return False

        if fila == filas - 1 and col == cols - 1:
            ruta.append((fila, col))
            return True

        visitados.add((fila, col))
        ruta.append((fila, col))

        direcciones = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for df, dc in direcciones:

            if backtrack(fila + df, col + dc):
                return True

        # Backtrack
        visitados.discard((fila, col))
        ruta.pop()

        return False

    if backtrack(0, 0):
        return ruta

    return None


# ============================================================
# PARTE 3C – CONTAR TODOS LOS CAMINOS
# ============================================================

def contar_caminos(laberinto: list, fila: int, col: int,
                   visitados: set) -> int:

    filas = len(laberinto)
    cols = len(laberinto[0])

    # Fuera de límites
    if fila < 0 or fila >= filas or col < 0 or col >= cols:
        return 0

    # Pared
    if laberinto[fila][col] == 1:
        return 0

    # Ya visitada
    if (fila, col) in visitados:
        return 0

    # Marcar visitada
    visitados.add((fila, col))

    # Llegamos a la salida
    if fila == filas - 1 and col == cols - 1:
        cantidad = 1

    else:
        cantidad = 0

        direcciones = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for df, dc in direcciones:

            cantidad += contar_caminos(
                laberinto,
                fila + df,
                col + dc,
                visitados
            )

    # Backtrack
    visitados.discard((fila, col))

    return cantidad


# ============================================================
# EXPERIMENTOS
# ============================================================

if __name__ == "__main__":

    print("=" * 50)
    print("PARTE 3A – Buscar un camino en LABERINTO_5x5")
    print("=" * 50)

    camino = encontrar_camino(LABERINTO_5x5, verbose=False)

    if camino:
        print(f"  Camino encontrado ({len(camino)} pasos):")
        print(f"  {camino}")
    else:
        print("  No existe camino.")

    print("\n" + "=" * 50)
    print("PARTE 3B – Visualización paso a paso")
    print("=" * 50)

    camino_simple = encontrar_camino(LABERINTO_SIMPLE, verbose=True)

    if camino_simple:
        print(f"\n  Camino final: {camino_simple}")

    print("\n" + "=" * 50)
    print("PARTE 3A – Laberinto sin salida")
    print("=" * 50)

    camino_ns = encontrar_camino(LABERINTO_SIN_SALIDA)

    if camino_ns is None:
        print("  Correctamente detectado: no existe camino. ✓")
    else:
        print(f"  ERROR: debería ser None, se obtuvo {camino_ns}")

    print("\n" + "=" * 50)
    print("PARTE 3C – Contar todos los caminos")
    print("=" * 50)

    for nombre, lab in [
        ("simple 3x3", LABERINTO_SIMPLE),
        ("5x5 con paredes", LABERINTO_5x5)
    ]:

        total = contar_caminos(lab, 0, 0, set())

        print(f"  {nombre}: {total} camino(s)")

    print()
    print("Reflexión:")
    print("En la Parte 2 solo se podía mover abajo y derecha.")
    print("Aquí el ratón puede moverse en 4 direcciones.")
    print("Por eso existen más caminos posibles.")
