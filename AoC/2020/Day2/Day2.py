# abrir archivo
f = open("input.txt", "r")
# contraseñas válidas
numvalidas = 0


# parte 1
def regla1(texto, l, num1, num2):
    cont = 0
    for letra in texto:
        if letra == l:
            cont += 1
    if int(num1) <= cont <= int(num2):
        return True


def regla2(texto, l, num1, num2):
    flag = False
    if (l == texto[int(num1)]) & (l != texto[int(num2)]):
        flag = True
    if (l == texto[int(num2)]) & (l != texto[int(num1)]):
        flag = True
    return flag


validas1 = 0
validas2 = 0
for line in f:

    k, texto = line.replace("\n", "").split(":")
    aux, l = k.split(" ")
    num1, num2 = aux.split("-")
    if regla1(texto, l, num1, num2):
        validas1 += 1
    if regla2(texto, l, num1, num2):
        validas2 += 1

print(validas1, validas2)
