def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])


def join_fasta(fasta):
    # Inicializar una variable para almacenar la secuencia combinada
    secuencia_combinada = []

    # Leer el archivo FASTA
    with open(fasta, "r") as archivo:
        lineas = archivo.readlines()
        secuencia_actual = ""
        for linea in lineas:
            if linea.startswith(">"):  # Identificar el encabezado del registro FASTA
                if secuencia_actual:  # Si ya hay una secuencia actual, combínala
                    secuencia_combinada.append(list(secuencia_actual))
                secuencia_actual = ""
            else:
                secuencia_actual += linea.strip()  # Agregar líneas de secuencia

    # Agregar la última secuencia
    if secuencia_actual:
        secuencia_combinada.append(list(secuencia_actual))

    return secuencia_combinada

def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]