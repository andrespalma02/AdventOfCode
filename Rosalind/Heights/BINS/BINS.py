# búsqueda binaria

def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if x < a[mid]:
            right = mid - 1
        elif x > a[mid]:
            left = mid + 1
        else:
            return mid + 1
    return -1


def recorrido(arr1, nums):
    res = ""
    for i in nums:
        res += " " + str(binary_search(arr1, i))
    return res


def parse_arrays(filename):
    with open(filename, 'r') as f:
        # Lee la primera línea y parsea el tamaño del primer array
        array1_size = int(f.readline().strip())

        # Lee la segunda línea y parsea el tamaño del segundo array
        array2_size = int(f.readline().strip())

        # Lee el resto del archivo y parsea los elementos de cada array a enteros
        array1 = [int(num) for num in f.readline().strip().split()]
        array2 = [int(num) for num in f.readline().strip().split()]
    return array1, array2


arr, nums = parse_arrays('rosalind_bins.txt')
data = recorrido(arr, nums)
print(data)
f = open("output.txt", "w")
f.write(str(data))
