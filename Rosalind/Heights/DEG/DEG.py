f = open("rosalind_deg.txt", "r")

nodes = {}

f.readline()
for line in f:
    m, n = map(int, line.split(" "))
    nodes.setdefault(m, []).append(n)
    nodes.setdefault(n, []).append(m)
sorted_aux = sorted(nodes.items())
sorted_nodes = dict(sorted_aux)
for k, v in sorted_nodes.items():
    print(k,":",v)
print(" ".join([str(len(v)) for k, v in sorted_nodes.items()]))
