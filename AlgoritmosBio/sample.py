import math


def biseccion(func, a, b, tol, max_iters):
    if func(a) * func(b) >= 0:
        print("El método de bisección no puede garantizar una raíz en este intervalo")
        return None

    for iteracion in range(max_iters):
        c = (a + b) / 2
        f_c = func(c)

        if abs(f_c) < tol:
            print(f"Iteración {iteracion + 1}: Raíz encontrada con valor {c}")
            return c

        if func(a) * f_c < 0:
            b = c
        else:
            a = c

        print(f"Iteración {iteracion + 1}: a = {a}, b = {b}")

    print("El método de bisección ha alcanzado el número máximo de iteraciones.")
    return None


def funcion(x):
    return x * math.log(x + 1) - 2


a = 0
b = 2
tolerancia = 10 ** -6
max_iteraciones = 100

raíz = biseccion(funcion, a, b, tolerancia, max_iteraciones)

if raíz is not None:
    print(f"Raíz aproximada: {raíz}")


