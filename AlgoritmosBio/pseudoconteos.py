secuencias = ["tatcacaATGGTAGGTAACT", "TCAACCAGGAGTAAGTCTTG", "GTTGCACCCTGTAAGTCTCA", "tatcacaATGGTAGGTAACT",
              "TCAACCAGGAGTAAGTCTTG", "CTTGCGAGAGGTGTGACATG", "GCTCTACTCGGTAAGGTGAC", "GCCTGGAGAGGTAATGACCC",
              "CAAAACCATTGTGAGTAATC", "GCCAGAGCAGGTAAAATATC", "GAACAGTCAGGTCTGTTGCT", "GAAGGCCCAGGTGAGCATAA",
              "TCCTCTACAGGTGGGTACAT", "GGCGTCCCGCGTAAGTATGG", "CCTCGTGCAGGTAAGATTAA", "TGCATGACAGGTGAGTGTTA",
              "GAAATGTACAGTAAGTCTCT", "GGTTCTCTGGGTAAGTAGAG", "AAATGTACAGGTGAGTACTG", "ACCTCGCTTGGTACGTGGGA",
              "AATCAGACAGGTATAGAAAC", "AGGACAGAAGGTAATTTTCT", "AACTATTTGGGTAGGTAGCA", "AAACTTGAAGGTATGTTGTT",
              "CTGGGATAAGGTAAAAGTAT", "TTGCACCCAGGTTAGTGGAT", "ACTTCAATCGGTATGTTTTC", "ACAGAGAAAAGTAAATTCCT",
              "AATGGGAAAGGTAACAACAA", "CATGCTACAGGTAGGTGAAT", "ggctaggATGGTGAGGGCGC", "CGACGCGGGCGTGAGAGGCG",
              "CATTGAGAATGTGAGTTATT", "AACAGAGCAGGTACTTGTAT", "TGAACCAAAGGTGAAGACAT"]

# Definimos las posiciones que queremos analizar
start_pos = 6
end_pos = 15

# Creamos diccionarios vacíos para contar la cantidad de veces que aparece cada base
freq_c = {}
freq_g = {}
freq_t = {}
freq_a = {}
freq_x = {}

arr = list(zip(*secuencias))

# Recorremos las secuencias
for i in range(start_pos, end_pos + 1):
    # Contamos la cantidad de veces que aparece cada base
    freq_c[i] = [str(elemento).upper() for elemento in arr[i]].count("C")
    freq_g[i] = [str(elemento).upper() for elemento in arr[i]].count("G")
    freq_t[i] = [str(elemento).upper() for elemento in arr[i]].count("T")
    freq_a[i] = [str(elemento).upper() for elemento in arr[i]].count("A")
    freq_x[i] = len(arr[i])

# Imprimimos los resultados
print("Posición\tC\tG\tT\tA\trel_C\trel_G\trel_T\trel_A")
for i in range(start_pos, end_pos + 1):
    print(f"{i}\t\t\t{freq_c[i]}\t{freq_g[i]}\t{freq_t[i]}\t{freq_a[i]}\t{freq_c[i] / freq_x[i]:.2f}"
          f"\t{freq_g[i] / freq_x[i]:.2f}\t{freq_t[i] / freq_x[i]:.2f}\t{freq_a[i] / freq_x[i]:.2f}")
