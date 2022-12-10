import re

sample_stack = [['N', 'Z'], ['D', 'C', 'M'], ['P']]
stack = [['G', 'P', 'N', 'R'],
         ['H', 'V', 'S', 'C', 'L', 'B', 'J', 'T'],
         ['L', 'N', 'M', 'B', 'D', 'T'],
         ['B', 'S', 'P', 'V', 'R'],
         ['H', 'V', 'M', 'W', 'S', 'Q', 'C', 'G'],
         ['J', 'B', 'D', 'C', 'S', 'Q', 'W'],
         ['L', 'Q', 'F'],
         ['V', 'F', 'L', 'D', 'T', 'H', 'M', 'W'],
         ['F', 'J', 'M', 'V', 'B', 'P', 'L']]


def day_5_1_2022(file):
    stack_to_use = stack
    instructions = []
    for line in file.read().strip().split("\n"):
        instructions.append(list(map(int, re.split("from|to", line.replace("move", ""))))) if line.startswith("move") \
            else ""
    for instruction in instructions:
        for number in range(instruction[0]):
            aux = stack_to_use[instruction[1] - 1].pop(0)
            stack_to_use[instruction[2] - 1].insert(0, aux)
    print("".join(item.pop(0) for item in stack_to_use))


def day_5_2_2022(file):
    stack_to_use = stack
    print(stack_to_use)
    instructions = []
    for line in file.read().strip().split("\n"):
        instructions.append(list(map(int, re.split("from|to", line.replace("move", ""))))) if line.startswith("move") \
            else ""
    i = 0
    for instruction in instructions:
        i += 1
        print(i, "-", instruction)
        aux = stack_to_use[instruction[1] - 1][:instruction[0]]
        del stack_to_use[instruction[1] - 1][:instruction[0]]
        stack_to_use[instruction[2] - 1][0:0] = aux
        print(stack_to_use)
    print(stack_to_use)
    print("".join(item.pop(0) for item in stack_to_use if item))


with open("input.txt") as file:
    day_5_1_2022(file)
    with open("input.txt") as file_2:
        day_5_2_2022(file_2)
