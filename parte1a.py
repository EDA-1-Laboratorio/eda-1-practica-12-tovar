import time

def medir(funcion, *args, repeticiones=5):
    tiempos = []
    resultado = None
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        resultado = funcion(*args)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return resultado, sum(tiempos) / len(tiempos)

def fib_recursivo(n):
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n == 0: return 0
    if n == 1: return 1
    return fib_recursivo(n-1) + fib_recursivo(n-2)

def fib_memo(n, memo=None):
    if memo is None: memo = {}
    if n < 0: raise ValueError("n debe ser >= 0")
    if n == 0: return 0
    if n == 1: return 1
    if n in memo: return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def fib_bottom_up(n):
    if n < 0: raise ValueError("n debe ser >= 0")
    if n == 0: return 0
    if n == 1: return 1
    tabla = [0] * (n+1)
    tabla[1] = 1
    for i in range(2, n+1):
        tabla[i] = tabla[i-1] + tabla[i-2]
    return tabla[n]

print("=== Comparación de tiempos: Fibonacci ===")
print(f"{'n':>5}  {'recursivo (s)':>16}  {'memo (s)':>12}  {'bottom_up (s)':>14}")
for n in [10, 20, 30, 35]:
    _, t_r = medir(fib_recursivo, n)
    _, t_m = medir(fib_memo, n)
    _, t_b = medir(fib_bottom_up, n)
    print(f"  {n:3d}  {t_r:16.8f}  {t_m:12.8f}  {t_b:14.8f}")

print("\n=== Test de doblamiento (recursivo) ===")
tiempos = {}
for n in [10, 20, 17, 35]:
    _, t = medir(fib_recursivo, n)
    tiempos[n] = t
print(f"  r(10→20) = {tiempos[20]/tiempos[10]:.2f}")
print(f"  r(17→35) = {tiempos[35]/tiempos[17]:.2f}")
