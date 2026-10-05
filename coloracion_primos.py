"""
Coloración de Números Primos — código del anexo
Autor del informe: Matías Álvarez

Nota: este código fue generado con ayuda de IA (Claude, de Anthropic).
El autor verificó a mano los resultados de las Partes 1 y 2.

Reglas:
  - Cada primo impar va al conjunto A (rojo) o al conjunto B (azul).
  - Un número par n >= 8 está CRUZADO si n = p + q, con p < q primos,
    uno en A y el otro en B. Si no existe ninguna suma así, n es un FALLO.
  - El 2 queda fuera (2 + primo impar da impar) y p + p no cuenta
    (siempre queda dentro de un solo conjunto, así que nunca cruza).

Para ejecutar:  python coloracion_primos.py
No necesita instalar nada.
"""

N = 1_000_000          # hasta dónde verificar en la Parte 3
A, B = 0, 1            # nombres de los dos conjuntos


def miles(x):
    """Escribe un número con punto de miles: 1000000 -> 1.000.000"""
    return f"{x:,}".replace(",", ".")


def criba(limite):
    """Criba de Eratóstenes: es_primo[k] es True si k es primo."""
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False
    for i in range(2, int(limite ** 0.5) + 1):
        if es_primo[i]:
            es_primo[i * i::i] = [False] * len(es_primo[i * i::i])
    return es_primo


es_primo = criba(N)
impares = [p for p in range(3, N + 1) if es_primo[p]]


def sumas(n):
    """Todas las formas de escribir n = p + q con p < q primos impares."""
    return [(p, n - p) for p in impares if 2 * p < n and es_primo[n - p]]


def cruzado(n, conjunto):
    """¿Tiene n alguna suma p + q con p y q en conjuntos distintos?"""
    for p in impares:
        if 2 * p >= n:
            return False
        q = n - p
        if es_primo[q] and conjunto[p] != conjunto[q]:
            return True
    return False


# ─────────────────────────────────────────────────────────────────────
# PARTE 1 · Las sumas de los pares del 8 al 38
# (todas usan solo los primos del 3 al 31)
# ─────────────────────────────────────────────────────────────────────
print("PARTE 1 · Sumas de cada par (p + q, con p < q)")
for n in range(8, 39, 2):
    texto = "  ".join(f"{p}+{q}" for p, q in sumas(n))
    print(f"  {n:>2} = {texto}")

# ─────────────────────────────────────────────────────────────────────
# PARTE 2 · Prueba exhaustiva: las 2^10 = 1024 particiones posibles
# de los diez primeros primos impares, revisando los pares del 8 al 38
# ─────────────────────────────────────────────────────────────────────
nucleo = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print("\nPARTE 2 · Revisando las 1024 particiones de", nucleo)

minimo = None
con_un_fallo = []
for codigo in range(2 ** len(nucleo)):
    conjunto = {p: (codigo >> i) & 1 for i, p in enumerate(nucleo)}
    fallos = [n for n in range(8, 39, 2) if not cruzado(n, conjunto)]
    if minimo is None or len(fallos) < minimo:
        minimo = len(fallos)
    if len(fallos) == 1:
        con_un_fallo.append((conjunto, fallos))

print(f"  Menor número de fallos en cualquier partición: {minimo}")
print(f"  Particiones con un solo fallo: {len(con_un_fallo)}")
for conjunto, fallos in con_un_fallo:
    del_3 = [p for p in nucleo if conjunto[p] == conjunto[3]]
    otro = [p for p in nucleo if conjunto[p] != conjunto[3]]
    print(f"    único fallo: {fallos[0]} → conjunto del 3: {del_3} | otro: {otro}")
print("  (Son la misma partición con los nombres A y B intercambiados.)")

# ─────────────────────────────────────────────────────────────────────
# PARTE 3 · Extender la partición hasta N
# Regla: se fija el núcleo de la Parte 2; luego se ubican los primos en
# orden, alternando conjuntos, y solo se rompe la alternancia cuando hace
# falta para no dejar un par sin cruzar. Al final se verifica todo de nuevo.
# La regla es solo un método para construir el ejemplo; lo que cuenta es
# la verificación final. Esto es una VERIFICACIÓN numérica, no una
# demostración.
# ─────────────────────────────────────────────────────────────────────
print(f"\nPARTE 3 · Extendiendo la partición hasta {miles(N)}")

conjunto = [None] * (N + 1)
for p in [3, 7, 17, 19]:
    conjunto[p] = A
for p in [5, 11, 13, 23, 29, 31]:
    conjunto[p] = B

anterior = B
inicio = impares.index(37)
for i in range(inicio, len(impares)):
    p = impares[i]
    siguiente = impares[i + 1] if i + 1 < len(impares) else N + 2
    # pares que quedan completamente decididos al ubicar p
    nuevos = range(p + 3, min(siguiente + 1, N) + 1, 2)
    for c in (1 - anterior, anterior):   # primero intenta alternar
        conjunto[p] = c
        if all(cruzado(n, conjunto) for n in nuevos):
            break
    anterior = conjunto[p]

fallos = [n for n in range(8, N + 1, 2) if not cruzado(n, conjunto)]
en_A = sum(1 for p in impares if conjunto[p] == A)
en_B = len(impares) - en_A
print(f"  Fallos entre 8 y {miles(N)}: {fallos}")
print(f"  Primos en A (rojo): {miles(en_A)}   Primos en B (azul): {miles(en_B)}")
