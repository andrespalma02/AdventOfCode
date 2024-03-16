nombre = input("Nombre")
sexo = input("Sexo")
if ("A" <= nombre.upper()[0] <= "M") and (sexo.upper() == "F") or ("N" <= nombre.upper()[0] <= "Z") and (
        sexo.upper() == "F"):
    print("Grupo A")
else:
    print("Grupo B")
