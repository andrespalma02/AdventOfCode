import time


# Ejercicios de A Common-Sense Guide to Data Structures and Algorithms
# Final del capítulo 12


def golomb(n, series=None):
    if n not in series:
        series[n] = 1 + golomb(n - golomb(golomb(n - 1, series), series), series)
    return series[n]


def add_until_100(array):
    if len(array) == 0:
        return 0
    else:
        suma = add_until_100(array[1:])
        return suma if array[0] + suma > 100 else array[0] + suma


def unique_paths(rows, columns, memo=None):
    if rows == 1 or columns == 1:
        return 1
    else:
        memo[(rows, columns)] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)
    return memo[(rows, columns)]


start = time.time()
# print(golomb(999, {1: 1}))
end = time.time()
# print(end - start)

start = time.time()
# print(add_until_100([i for i in range(1, 900)]))
end = time.time()
# print(end - start)

start = time.time()
# print(unique_paths(25, 25, {}))
end = time.time()
# print(end - start)
