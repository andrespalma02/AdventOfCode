from itertools import permutations

f = open("rosalind_lexf.txt")
s = f.readline().strip().replace(" ", "")
n = int(f.readline().strip())
s = s*2

# Generar permutaciones de longitud 2
perms = permutations(s, n)

# Convertir a lista y mostrar el resultado
result = list(perms)
for item in sorted(["".join(pair) for pair in set(result)]):
    print(item)