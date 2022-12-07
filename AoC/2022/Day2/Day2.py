def day_2_1_2022(file):
    aux = 0
    meaning = {'A': {'X': 4, 'Y': 8, 'Z': 3},
               'B': {'X': 1, 'Y': 5, 'Z': 9},
               'C': {'X': 7, 'Y': 2, 'Z': 6}}

    for line in file.read().strip().split("\n"):
        comp, mine = line.split()[0], line.split()[1]
        aux += meaning[comp][mine]
    print(aux)


def day_2_2_2022(file_2):
    aux = 0
    meaning = {'A': {'X': 3, 'Y': 4, 'Z': 8},
               'B': {'X': 1, 'Y': 5, 'Z': 9},
               'C': {'X': 2, 'Y': 6, 'Z': 7}}

    for line in file_2.read().strip().split("\n"):
        comp, mine = line.split()[0], line.split()[1]
        aux += meaning[comp][mine]
    print(aux)


with open("input.txt", "r") as file:
    day_2_1_2022(file)
    with open("input.txt", "r") as file_2:
        day_2_2_2022(file_2)
