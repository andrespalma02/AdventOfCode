# -*- coding: utf-8 -*-
# Programa para realizar mutación inversa de genomas con uso de archivos y funciones
# Autores: Espinoza Amalia, Gallo Mickaela, García Mario, Palma Andrés, Ojeda Paula

# Función para leer y formatear los datos del archivo de entrada
def parser(file):
    with open(file, 'r') as f:  # Abrir el archivo de entrada en modo lectura
        # Se inicializan las variables que se utilizarán para darles formato los datos del archivo
        genes = []  # Lista que contendrá los datos de los genomas
        n_genes = 0
        r_mutaciones = 0
        indices = []
        q_consultas = 0
        consultas = []
        flag_mutaciones = 0
        flag_consultas = 0
        flag_general = 0
        line = f.readline()
        while line.strip("\n") != '0':
            try:  # Intentar formatear los datos del archivo
                # Leer los datos del input
                # Se utilizan los flags para saber en qué parte del archivo se está leyendo
                if flag_general == 0:
                    # Se lee el número de genes
                    n_genes = int(line.strip("\n"))
                    if n_genes < 0:
                        # Si el número de genes es inválido, se asigna el número 1
                        print("ADVERTENCIA: Número de genes inválido. Se asignará el número 1")
                        n_genes = 1
                    # Se cambia el flag para indicar que la siguiente línea a leer es el número de mutaciones
                    flag_general = 1
                elif flag_general == 1:
                    r_mutaciones = int(line.strip("\n"))
                    if r_mutaciones < 0:
                        # Si el número de mutaciones es inválido, se asigna el número 1
                        print("ADVERTENCIA: Número de mutaciones inválido. Se asignará el número 1")
                        r_mutaciones = 1
                    # Se cambia el flag para indicar que la siguiente línea a leer son los índices que se mutarán
                    flag_general = 2
                elif flag_general == 2:
                    i, j = line.strip("\n").split(" ")
                    if int(i) > int(j):
                        print("ADVERTENCIA: El índice i es mayor que el índice j. Se intercambiarán los valores")
                        i, j = j, i
                    if int(i) <= 0:
                        print("ADVERTENCIA: El índice i es inválido. Se asignará el número 1")
                        i = 1
                    if int(j) > n_genes:
                        print("ADVERTENCIA: El índice j es inválido. Se asignará el número ", n_genes)
                        j = n_genes
                    indices.append([int(i), (int(j))])
                    # Se aumenta el contador de mutaciones según el número de mutaciones que se hayan leído
                    flag_mutaciones += 1
                    # Si el contador de mutaciones es igual al número de mutaciones,
                    # se cambia el flag para indicar que la siguiente línea a leer es el número de consultas
                    # y se reinicia el contador de mutaciones
                    if flag_mutaciones == r_mutaciones:
                        flag_general = 3
                        flag_mutaciones = 0
                elif flag_general == 3:
                    q_consultas = int(line.strip("\n"))
                    if q_consultas <= 0:
                        # Si el número de consultas es inválido, se asigna el número 1
                        print("ADVERTENCIA: Número de consultas inválido. Se asignará el número 1")
                        q_consultas = 1
                    # Se cambia el flag para indicar que la siguiente línea a leer son las consultas
                    flag_general = 4
                elif flag_general == 4:
                    consulta = int(line.strip("\n"))
                    if consulta <= 0 or consulta > n_genes:
                        # Si la consulta es inválida, se asigna el número 1
                        print("ADVERTENCIA: La consulta es inválida. Se asignará el número 1")
                        consulta = 1
                    consultas.append(consulta)
                    # Se aumenta el contador de consultas según el número de consultas que se hayan leído
                    flag_consultas += 1
                    # Si el contador de consultas es igual al número de consultas,
                    # se reinicia el contador de consultas y el flag general
                    if flag_consultas == q_consultas:
                        flag_consultas = 0
                        flag_general = 0
                        # Se añade el genoma a la lista de genomas
                        genes.append(
                            ["Genoma " + str(len(genes) + 1), n_genes, r_mutaciones, indices, q_consultas, consultas])
                        # Se reinician las variables
                        n_genes = 0
                        r_mutaciones = 0
                        indices = []
                        q_consultas = 0
                        consultas = []
            except:  # Si no se pueden formatear los datos
                print("ERROR: Estructura de datos inválida. Se terminará la ejecución del programa")
                genes = []
                break
            # Se lee la siguiente línea
            line = f.readline()
    return genes


# Función para realizar la mutación inversa
def reverse(gen):
    result = ""
    # Se crea una lista con los números del 1 al número de genes
    N = list(range(1, gen[1] + 1))
    # Se crea una lista con los genes mutados, inicialmente iguales a la lista N
    gen_mutado = N
    R = gen[2]
    # Se recorren las mutaciones
    for r in range(R):
        # Se obtienen los índices i y j
        i, j = gen[3][r]
        # Se invierten los genes desde i hasta j
        gen_mutado[i - 1:j] = reversed(gen_mutado[i - 1:j])
    result += gen[0] + "\n"
    # Se recorren las consultas
    for q in gen[5]:
        # Se añade el resultado de la consulta
        result += str(gen_mutado.index(q) + 1) + "\n"
    return result


# Función para añadir el resultado en el archivo de salida
def anadir_archivo(file, gen):
    # Se abre el archivo en modo append
    with open(file, 'a') as f:
        # Escribir el resultado en el archivo, también se imprime en consola
        print(gen, end="")
        f.write(gen)


if __name__ == '__main__':
    # Se lee el archivo de entrada
    file = "out.txt"
    genes = parser("genes.txt")
    open(file, "w").close()  # Cada vez que se ejecuta el programa, se borra el archivo de salida
    if genes:  # Si hay genes
        # Se recorren los genes
        for gen in genes:
            # Se añade el resultado de la mutación inversa en el archivo de salida
            anadir_archivo(file, reverse(gen))
    else:  # Si no hay genes
        print("No hay genes")
