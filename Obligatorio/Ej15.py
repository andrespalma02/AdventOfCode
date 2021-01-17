lista_turnos = [5, 2, 8, 16, 18, 0, 1, 0]
dic_turn = dict()
for i in range(len(lista_turnos)):
    dic_turn[lista_turnos[i]] = i + 1
print(dic_turn)
for i in range(len(lista_turnos) - 1, 2019):
    if lista_turnos[i] in lista_turnos[:-2]:
        l_aux = lista_turnos[:-1]
        dif = len(lista_turnos) - (len(l_aux) - l_aux[::-1].index(lista_turnos[i]))
        lista_turnos.append(dif)
    else:
        lista_turnos.append(0)

print("EL turno", i + 2, "es:", lista_turnos[-1])
