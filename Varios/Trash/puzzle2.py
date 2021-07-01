#Nombre: Steven Javier Rivera Tenelanda

"""
Se define una lista que contendran informacion del estado inicial
y el estado objetivo del juego 8-puzzle
"""
estado_objetivo = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
estado_inicial = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
temporal = []

# Inicializacion de los valores de las heuristicas h1 y h2
h1 = -1
h2 = 0

print("El estado inicial es: ", estado_inicial)

print("\nEl estado objetivo es: ", estado_objetivo)

print("\n================== HEURISTICA 'h1' ==================")

# En esta seccion del codigo se implementa el conteo
# de las casillas erroneas comparado con el estado objetivo
for i in range(len(estado_inicial)):
    for j in range(len(estado_inicial)):
        if estado_inicial[i][j] != estado_objetivo[i][j]:
            h1 += 1

print("\nEl numero de las casillas erroneas es: ", h1)


"""
En esta parte del codigo se comprobara el numero de movimientos de cada una de 
las casillas para llegar a su estado objetivo y se los almacenaran en una lista llamada "temporal"
"""
for i in range(len(estado_inicial)):
    for j in range(len(estado_inicial)):
        if estado_inicial[i][j] == 0:
            pass
        else:
            if estado_objetivo[0][0] == estado_inicial[i][j]:
                temporal.append(abs(i - 0) + abs(j - 0))

            elif estado_objetivo[0][1] == estado_inicial[i][j]:
                temporal.append(abs(i - 0) + abs(j - 1))

            elif estado_objetivo[0][2] == estado_inicial[i][j]:
                temporal.append(abs(i - 0) + abs(j - 2))

            elif estado_objetivo[1][0] == estado_inicial[i][j]:
                temporal.append(abs(i - 1) + abs(j - 0))

            elif estado_objetivo[1][1] == estado_inicial[i][j]:
                temporal.append(abs(i - 1) + abs(j - 1))

            elif estado_objetivo[1][2] == estado_inicial[i][j]:
                temporal.append(abs(i - 1) + abs(j - 2))

            elif estado_objetivo[2][0] == estado_inicial[i][j]:
                temporal.append(abs(i - 2) + abs(j - 0))

            elif estado_objetivo[2][1] == estado_inicial[i][j]:
                temporal.append(abs(i - 2) + abs(j - 1))

            elif estado_objetivo[2][2] == estado_inicial[i][j]:
                temporal.append(abs(i - 2) + abs(j - 2))

print("\n================== HEURISTICA 'h2' ==================")
print("\nEl numero de movimientos de cada una de las baldosas para llegar a su estado objetivo son: " + str(temporal))

for i in range(len(temporal)):
    h2 += temporal[i]
print("\nLa suma de los movimientos necesarios para llegar al estado objetivo es: ", h2)

"""
Para sumar todos los movimientos necesarios para llegar al estado objetivo
Se declara un for que va a ir sumando todos los valores almacenados en la lista llamada "temporal"
que contendra todos los movimientos necesarios de cada baldosa para llegar a su estado objetivo
"""