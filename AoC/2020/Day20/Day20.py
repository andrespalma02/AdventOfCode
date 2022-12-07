from copy import deepcopy


# metodo para retornar un borde específico de la pieza
def borde(pieza, borde):
    if borde == "arriba":
        return pieza[0]
    if borde == "abajo":
        return pieza[-1][::-1]
    if borde == "derecha":
        return "".join([t[-1] for t in pieza])
    if borde == "izquierda":
        return "".join([t[0] for t in pieza])[::-1]
    raise ValueError


# metodo para obtener todos los lados de una pieza
def bordes(pieza):
    return [borde(pieza, "arriba"), borde(pieza, "derecha"), borde(pieza, "abajo"), borde(pieza, "izquierda")]


# metodo para rotar una pieza
def rotar(pieza):
    R = len(pieza)
    C = len(pieza[0])
    aux = [["x" for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            aux[r][c] = pieza[C - c - 1][r]
    return ["".join(r) for r in aux]


# metodo para voltear una pieza
def voltear(pieza):
    return pieza[::-1]


# metodo para añadir una pieza en su posicion correcta en la imagen
# sobre la que se buscará el monstruo
def add_imagen(pieza, flag=False):
    global imagen
    if imagen == []:
        imagen = deepcopy(pieza)
    elif flag:
        for r in pieza:
            imagen.append(r)
    else:
        R = len(imagen) - len(pieza)
        for r in range(len(pieza)):
            imagen[r + R] += pieza[r]


f = open("input.txt", "r")
dato = f.read().strip().split("\n\n")
piezas = {}
# se obtienen las piezas y se guardan en un diccionario
# con los datos de la última línea del ciclo for externo
for raw_pieza in dato:
    linea = raw_pieza.strip("\n").split("\n")
    idn = int(linea[0].split()[1].strip(":"))
    matriz = linea[1:]
    bordeaux = bordes(matriz)
    bordeaux += [s[::-1] for s in bordeaux]
    piezas[idn] = {"matriz": matriz, "bordes": bordeaux, "adyacente": {}}
    # se realiza la comparacion de cada pieza para encontrar los lados adyacentes
    for i, pieza in piezas.items():
        if i == idn:
            continue
        shared = [s for s in pieza["bordes"] if s in bordeaux[:4]]
        for s in shared:
            piezas[idn]["adyacente"][i] = s
            piezas[i]["adyacente"][idn] = s
# se determinan que piezas tienen dos piezas adyacentes
esquinas = list(map(int, [t for t in piezas if len(piezas[t]["adyacente"]) == 2]))
res = 1
for c in esquinas:
    res *= c

print("Parte 1")
print("Esquinas: ", esquinas, " Producto de las esquinas: ", res)

r, c = 0, 0
mapa = {}
imagen = []

while not len(mapa) == len(piezas):
    # al iniciar se esocoge una esquina y se la añade a la imagen
    if r == 0 and c == 0:
        idn = esquinas[0]
        pieza = piezas[idn]["matriz"]
        adyacente = list(piezas[idn]["adyacente"].values())
        adyacente += [n[::-1] for n in adyacente]
        while True:
            abajo, derecha = borde(pieza, "abajo"), borde(pieza, "derecha")
            if abajo in adyacente and derecha in adyacente:
                break
            pieza = rotar(pieza)
        mapa[(r, c)] = idn
        piezas[idn]["matriz"] = pieza
        add_imagen(pieza)
        c += 1
    elif c == 0:
        p_idn = mapa[(r - 1, c)]
        p_pieza = piezas[p_idn]["matriz"]
        borde_options = [borde(p_pieza, "abajo"), borde(p_pieza, "abajo")[::-1]]
        idn = [i for i, s in piezas[p_idn]["adyacente"].items() if s in borde_options][0]
        pieza = piezas[idn]["matriz"]
        n_borde = borde(piezas[p_idn]["matriz"], "abajo")
        found = False
        # por cada pieza existen 8 orientaciones por lo que esta pieza
        # se puede rotar 4 veces, y en caso de no encajar, se voltea
        for i in range(8):
            if i == 4:
                pieza = voltear(pieza)
            if borde(pieza, "arriba") == n_borde[::-1]:
                found = True
                break
            pieza = rotar(pieza)
        if not found:
            pass
        mapa[(r, c)] = idn
        piezas[idn]["matriz"] = pieza
        add_imagen(pieza, flag=True)
        c += 1
    else:
        p_idn = idn
        p_pieza = piezas[p_idn]["matriz"]
        borde_options = [borde(p_pieza, "derecha"), borde(p_pieza, "derecha")[::-1]]
        idn = [i for i, s in piezas[p_idn]["adyacente"].items() if s in borde_options]
        if len(idn) == 1:
            idn = idn[0]
            pieza = piezas[idn]["matriz"]
            n_borde = borde(piezas[p_idn]["matriz"], "derecha")
            found = False
            for i in range(8):
                if i == 4:
                    pieza = voltear(pieza)
                if borde(pieza, "izquierda") == n_borde[::-1]:
                    found = True
                    break
                pieza = rotar(pieza)
            if not found:
                pass
            mapa[(r, c)] = idn
            piezas[idn]["matriz"] = pieza
            add_imagen(pieza)
            c += 1
        elif len(idn) == 0:
            r, c = r + 1, 0
        else:
            raise Exception

# por cada pieza de la imagen es necesario remover los bordes
tot = []
for i in range(len(imagen) // 10):
    tot.extend(imagen[(10 * i) + 1: (10 * i) + 9])
tot = ["".join([r[(10 * c) + 1: (10 * c) + 9] for c in range(len(r) // 10)]) for r in tot]

# Se determinan puntos que permitiran determinar donde está el monstruo en la imagen

monstruo = [(0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1),
            (12, 1), (13, 2), (16, 2), (17, 1), (18, 0), (18, 1), (19, 1)]

# la imagen final debe ser girada y volteada hasta que se encuentre el patron del monstruo
mon = 0
lala = 0
for i in range(8):
    if i == 4:
        tot = voltear(tot)
    for r in range(len(tot) - 2):
        for c in range(len(tot[0]) - 20):
            if all([tot[r + dr][c + dc] == "#" for dc, dr in monstruo]):
                mon += 1
    tot = rotar(tot)

nomon = len([c for r in tot for c in r if c == "#"]) - mon * len(monstruo)
print("Parte 2")
print("La cantidad de # en donde no esta el monstruo es: ", nomon)
