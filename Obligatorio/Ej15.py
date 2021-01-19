lista_turnos = [5,2,8,16,18,0,1]
dic_turn = dict()
for i in range(len(lista_turnos)):
    dic_turn[lista_turnos[i]] = [i + 1]
num = lista_turnos[-1]
for i in range(len(lista_turnos),2020):
    if len(dic_turn[num]) == 1:
        num = 0
        dic_turn[num].append(i + 1)
    else:
        num = dic_turn[num][-1] - dic_turn[num][-2]
        if num in dic_turn:
            dic_turn[num].append(i + 1)
        else:
            dic_turn[num] = [i + 1]
print("El turno", i + 1, "es:", num)