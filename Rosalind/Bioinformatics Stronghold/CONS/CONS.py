# Nombre del archivo que contiene las secuencias FASTA

from Rosalind.Functions import join_fasta, transpose_matrix


def contar_palabras(array1, array2):
    conteo_palabras = {}
    for palabra in array1:
        conteo = array2.count(palabra)
        conteo_palabras[palabra] = conteo
    return conteo_palabras


archivo_input = "rosalind_cons.txt"

secuencia_combinada = join_fasta(archivo_input)
secuencia_combinada_transpuesta = transpose_matrix(secuencia_combinada)
output = {'A': [], 'C': [], 'G': [], 'T': []}
string_final = ""
for secuencia in secuencia_combinada_transpuesta:
    json_data = contar_palabras(['A', 'C', 'G', 'T'], secuencia)
    clave_maxima = max(json_data, key=json_data.get)
    valor_maximo = json_data[clave_maxima]
    output['A'].append(json_data['A'])
    output['C'].append(json_data['C'])
    output['G'].append(json_data['G'])
    output['T'].append(json_data['T'])
    string_final += clave_maxima

print(string_final)
print("A:", " ".join(map(str, output['A'])))
print("C:", " ".join(map(str, output['C'])))
print("G:", " ".join(map(str, output['G'])))
print("T:", " ".join(map(str, output['T'])))
