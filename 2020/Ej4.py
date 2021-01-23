import re


def validar(passport):
    flag = 0
    for k, v in passport.items():
        if k == "byr":
            if (1920 <= int(v) <= 2002) & (len(v) == 4):
                flag += 1
        if k == "iyr":
            if (2010 <= int(v) <= 2020) & (len(v) == 4):
                flag += 1
        if k == "eyr":
            if (2020 <= int(v) <= 2030) & (len(v) == 4):
                flag += 1
        if k == "hgt":
            if v[-2:] == "cm" and 150 <= int(v[:-2]) <= 193:
                flag += 1
            elif v[-2:] == "in" and 59 <= int(v[:-2]) <= 76:
                flag += 1
        if k == "hcl":
            if re.match('^#[0-9a-f]{6}$', v):
                flag += 1
        if k == "ecl":
            if re.match("(amb|blu|brn|gry|grn|hzl|oth)", v):
                flag += 1
        if k == "pid":
            if re.match('^[0-9]{9}$', v):
                flag += 1
        if flag == 7:
            return True


f = open("input4.txt", "r")
data = f.read().split("\n\n")
lista = list()
passport = dict()
lista_pass = list()
# todos los datos en una sola linea
for line in data:
    lista.append(line.replace(" ", "\n"))
for item in lista:
    # todos los campos separados por datos
    lista2 = item.split("\n")
    for item in lista2:
        if ":" in item:
            k, v = item.split(":")
            passport[k] = v
    lista_pass.append(passport)
    passport = dict()
valid = 0
valid2 = 0
for item in lista_pass:
    #compruebo que tenga los 8 o los 7 campos sin cid
    if len(item) == 8 or (len(item) == 7 and ("cid" not in item)):
        valid += 1
    if validar(item):
        valid2 += 1
print(valid, valid2)
