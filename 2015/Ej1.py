f = open("input1.txt", "r")
pisos = str(f.readlines())[2:-2]
con = 0
for i in range(len(pisos)):
    if pisos[i] == "(":
        con += 1
    else:
        con -= 1
        if con == -1:
            print(i+1)
print(con)
