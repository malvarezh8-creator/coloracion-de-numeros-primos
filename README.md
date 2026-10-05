# Coloración de números primos

Código que acompaña al informe *Coloración de Números Primos* (Matías Álvarez, 2026).

## La pregunta

Cada primo impar se asigna a uno de dos conjuntos, A o B, sin ninguna regla ni fórmula. Un número par n ≥ 8 está **cruzado** si se puede escribir como n = p + q, con p < q primos, uno en A y el otro en B. Si no se puede, n es un **fallo** de esa partición.

¿Cuál es el menor número de fallos que puede tener una partición?

## Resultados

**Teorema (demostrado).** Para toda partición de los primos impares en dos conjuntos:

1. Hay al menos un fallo, y al menos uno de sus fallos es el 8, el 10 o el 12.
2. Si hay exactamente un fallo, ese fallo es el 10.
3. En ese caso, entre los primos hasta el 31, el conjunto que contiene al 3 es {3, 7, 17, 19} y el otro es {5, 11, 13, 23, 29, 31}.

**Conjetura (verificada hasta 1.000.000).** Existe una partición cuyo único fallo es el 10.

La conjetura implica que todo par desde el 12 es suma de dos primos distintos, una variante de la conjetura de Goldbach. Por eso no puede demostrarse sin demostrar esa variante.

## Qué hace el código

| Parte | Qué hace | Nivel |
|---|---|---|
| 1 | Lista las sumas p + q de los pares del 8 al 38 | Datos para seguir el cálculo a mano |
| 2 | Revisa las 1.024 particiones posibles de los primos del 3 al 31 | Confirma por computador los puntos 2 y 3 del teorema |
| 3 | Construye una partición y verifica sus fallos hasta 1.000.000 | Verificación numérica, no demostración |

En la Parte 3, la partición se construye fijando el núcleo del punto 3 y ubicando los demás primos en orden, alternando conjuntos, salvo cuando hace falta romper la alternancia para no dejar un par sin cruzar. Esa regla es solo un método para construir el ejemplo; lo que cuenta es la verificación final, que revisa de nuevo todos los pares.

## Cómo ejecutarlo

Requiere Python 3. No necesita instalar ninguna librería.

```
python coloracion_primos.py
```

Tarda unos pocos segundos.

## Salida esperada

```
PARTE 1 · Sumas de cada par (p + q, con p < q)
   8 = 3+5
  10 = 3+7
  12 = 5+7
  14 = 3+11
  16 = 3+13  5+11
  18 = 5+13  7+11
  20 = 3+17  7+13
  22 = 3+19  5+17
  24 = 5+19  7+17  11+13
  26 = 3+23  7+19
  28 = 5+23  11+17
  30 = 7+23  11+19  13+17
  32 = 3+29  13+19
  34 = 3+31  5+29  11+23
  36 = 5+31  7+29  13+23  17+19
  38 = 7+31

PARTE 2 · Revisando las 1024 particiones de [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
  Menor número de fallos en cualquier partición: 1
  Particiones con un solo fallo: 2
    único fallo: 10 → conjunto del 3: [3, 7, 17, 19] | otro: [5, 11, 13, 23, 29, 31]
    único fallo: 10 → conjunto del 3: [3, 7, 17, 19] | otro: [5, 11, 13, 23, 29, 31]
  (Son la misma partición con los nombres A y B intercambiados.)

PARTE 3 · Extendiendo la partición hasta 1.000.000
  Fallos entre 8 y 1.000.000: [10]
  Primos en A (rojo): 39.247   Primos en B (azul): 39.250
```

## Uso de inteligencia artificial

El código fue generado con ayuda de IA (Claude, de Anthropic). Los resultados demostrados del teorema fueron verificados a mano por el autor.
