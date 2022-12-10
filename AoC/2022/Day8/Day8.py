def day_8_1_2022(file):
    file = file.read().splitlines()
    vis = (len(file) + (len(file[0]) - 2)) * 2
    arr_up = []
    arr_down = []
    for i in range(1, len(file) - 1):
        for j in range(1, len(file[i]) - 1):
            [arr_up.append(int(file[k][j])) for k in range(i)]
            [arr_down.append(int(file[k][j])) for k in range(i + 1, len(file))]
            if max(file[i][:j]) < file[i][j] \
                    or max(file[i][j + 1:]) < file[i][j] \
                    or max(arr_up) < int(file[i][j]) \
                    or max(arr_down) < int(file[i][j]):
                vis += 1
            arr_up = []
            arr_down = []
    print(vis)


def day_8_2_2022(file_2):
    file_2 = file_2.read().splitlines()
    arr_up = []
    arr_down = []
    arr_left = []
    arr_right = []
    points = []

    for i in range(len(file_2)):
        for j in range(len(file_2[i])):
            for k in reversed(range(i)):
                arr_up.append(int(file_2[k][j]))
                if int(file_2[k][j]) < int(file_2[i][j]):
                    continue
                else:
                    break
            for k in range(i + 1, len(file_2)):
                arr_down.append(int(file_2[k][j]))
                if int(file_2[k][j]) < int(file_2[i][j]):
                    continue
                else:
                    break
            for item in reversed(file_2[i][:j]):
                arr_left.append(int(item))
                if int(item) < int(file_2[i][j]):
                    continue
                else:
                    break
            for item in file_2[i][j + 1:]:
                arr_right.append(int(item))
                if int(item) < int(file_2[i][j]):
                    continue
                else:
                    break
            points.append(len(arr_up) * len(arr_down) * len(arr_left) * len(arr_right))
            arr_down = []
            arr_up = []
            arr_left = []
            arr_right = []
    print(max(points))


with open("input.txt", "r") as file:
    day_8_1_2022(file)
    with open("input.txt", "r") as file_2:
        day_8_2_2022(file_2)

