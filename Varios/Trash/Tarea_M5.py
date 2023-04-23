# -*- coding: utf-8 -*-
# Realizar un programa en Python que dé solución al ejercicio planteado en el archivo Tornado.pdf
# Autores: Espinoza Amalia, Gallo Mickaela, García Mario, Palma Andrés, Ojeda Paula

def parser_archivo(archivo):
    with open(archivo) as f:
        dict_array = []
        diccionario_cercas= {}
        num_postes_flag = True
        for line in f:
            line = line.strip()
            if line == "0":
                break
            if num_postes_flag:
                diccionario_cercas = {"num_postes": int(line)}
            else:
                diccionario_cercas["array_postes"] = [int(x) for x in line.split(" ")]
                dict_array.append(diccionario_cercas)
            num_postes_flag = not num_postes_flag
        return dict_array


def validar_datos(diccionario_postes):
    return all(
        poste["num_postes"] == len(poste["array_postes"]) and all(x == 0 or x == 1 for x in poste["array_postes"]) for
        poste in diccionario_postes)


def calcular_postes(cerca):
    postes = 0
    i = 0
    while i < len(cerca["array_postes"]) - 1:
        if cerca["array_postes"][i] == 0 and cerca["array_postes"][i + 1] == 0:
            postes += 1
            i += 2
        else:
            i += 1
    return postes


def imprimir_cerca(poste):
    print("La cerca: " + " ".join(str(x) for x in poste["array_postes"]))


def imprimir_solucion(poste):
    print(f"Se necesitan {calcular_postes(poste)} postes auxiliares.\n")


if __name__ == "__main__":
    diccionario_cercas = parser_archivo('in.txt')
    if validar_datos(diccionario_cercas):
        for cerca in diccionario_cercas:
            imprimir_cerca(cerca)
            imprimir_solucion(cerca)
    else:
        print("Error en los datos")
