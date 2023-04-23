# -*- coding: utf-8 -*-
# Programa para resolver ecuaciones cuadráticas en Python por el método de la fórmula cuadrática
# Autores: Espinoza Amalia, Gallo Mickaela, García Mario, Palma Andrés, Ojeda Paula

# Importar las librerías
import os
import math


# Borrar la pantalla de la terminal
# os.system("clear")

# El método de la fórmula cuadrática incluye la operación raíz cuadrada, la cual requiere importar la librería math

def format(x):
    if x == round(x):
        x_formateado = '{:.0f}'.format(x)
    elif round(x * 10, 1) == round(x * 10):
        x_formateado = '{:.1f}'.format(x)
    elif round(x * 10, 2) == round(x * 10):
        x_formateado = '{:.2f}'.format(x)
    else:
        x_formateado = '{:.3f}'.format(round(x, 3))

    return x_formateado


# Introducción de datos
print("-- CÁLCULO DE LAS RAÍCES DE UNA ECUACIÓN CUADRÁTICA (ax² + bx + c = 0) --\n")
print("Ingreso de los coeficientes a, b y c")
try:
    a = float(input("Coeficiente a: "))
    if a == 0:
        print("El coeficiente a debe ser distinto de cero. Se asignó el valor a=1.")
        a = 1
except ValueError:
    print("El coeficiente a debe ser un número real. Se asignó el valor a=1.")
    a = 1
try:
    b = float(input("Coeficiente b: "))
except ValueError:
    print("El coeficiente b debe ser un número real. Se asignó el valor b=0.")
    b = 0
try:
    c = float(input("Coeficiente c: "))
except ValueError:
    print("El coeficiente c debe ser un número real. Se asignó el valor c=0.")
    c = 0
print()

ecuacion = ""

if a == 1:
    ecuacion += "x^2 "
elif a == -1:
    ecuacion += "-x^2 "
else:
    ecuacion += f"{format(a)}x^2 "

if b != 0:
    if b == 1:
        ecuacion += "x "
    elif b == -1:
        ecuacion += "-x "
    elif b > 0:
        ecuacion += f"+ {format(b)}x "
    else:
        ecuacion += f"- {format(-b)}x "

if c != 0:
    if c > 0:
        ecuacion += f"+{format(c)}"
    else:
        ecuacion += f"- {format(-c)}"
print("La ecuación es: " + ecuacion + "= 0")

# Cálculo del discriminante
disc = (b ** 2) - (4 * a * c)

# Condición para determinar el tipo de solución
if disc > 0:  # La solución cuenta con 2 raices reales: x1 = xxx y x2 = yyy
    xxx = ((-b + math.sqrt(disc)) / (2 * a))
    yyy = ((-b - math.sqrt(disc)) / (2 * a))

    if int(math.fabs(xxx)) == 0:
        x1 = 0
    if int(math.fabs(yyy)) == 0:
        x2 = 0

    print(f"Se encontraron 2 raíces reales y son: X₁ = {format(xxx)}; X₂ = {format(yyy)}\n")
elif disc == 0:  # La solución cuenta con 1 raíz real: x1 = zzz
    zzz = (-b / (2 * a))
    if int(math.fabs(zzz)) == 0:
        x = 0.0
    print(f"Se encontró una única raíz real y es: X = {format(zzz)}\n")
elif disc < 0:  # Las raices son imaginarias
    print("Las raíces son imaginarias\n")
print("-- Gracias por usar este programa --\n")
