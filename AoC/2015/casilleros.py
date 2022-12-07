casilleros = list()
estados = list()
personas = 0
for i in range(1,100):
    casilleros.append(i)
    estados.append(0)
for i in range(1, 100):
    for j in range(len(casilleros)):
        if casilleros[j] % i == 0:
            if estados[j] == 0:
                estados[j] = 1
            else:
                estados[j] = 0

for i in range(1,100):
    if estados[i-1]==1:
        print(casilleros[i-1])
