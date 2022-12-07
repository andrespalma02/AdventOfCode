f = open("input.txt")

# guardo línea por línea en una lista
lines = f.readlines()

curr_x = 0
# definir movimientos en x, y
mov_x = 3
mov_y = 1
arboles = 0

for curr_y, cada_linea in enumerate(lines):
    if cada_linea[curr_x] == "#":  # Cuando se encuentre el signo numeral se habrá encontrado un arbol, por lo tanto,
        # el contador de árboles aumenta
        arboles += 1
    curr_x = (curr_x + mov_x) % len(cada_linea[
                                    :-1])  # Como en el input solo se tiene una pieza del mapa completo de árboles
    # vamos a repetir esta pieza varias veces hacia la derecha hasta que se llegue a la última fila de la pieza dada
    # por el input

print("PRIMERA PARTE")
print(f"Los arboles encontrados fueron: {arboles}")

# 2
# definimos las pendientes que requiere que evaluemos el ejercicio
pendientes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

# definimos una variable para contar el número de árboles que se encuentran basados en varias pendientes definimos
# desde el valor 1 porque ya se evaluo una pendiente en la parte 1 por lo tanto ya tenemos los arboles evaluados en
# esa pendiente.
multiples_arboles = 1
print()
print("SEGUNDA PARTE")
for pendiente in pendientes:  # recorremos cada pendiente en la lista de pendientes buscando arboles
    mov_x, mov_y = pendiente
    arboles = 0
    curr_x = 0
    for curr_y, cada_linea in enumerate(lines):
        if curr_y % mov_y == 0:
            if cada_linea[curr_x] == "#":
                arboles += 1
            curr_x = (curr_x + mov_x) % len(cada_linea[:-1])
    multiples_arboles *= arboles
print("Multiplicación de arboles encontrados en cada pendiente: ", multiples_arboles)
