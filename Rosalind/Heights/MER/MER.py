f = open("rosalind_mer.txt", "r")


# merge two sorted arrays
def merge(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i < len(a):
        result.extend(a[i:])
    if j < len(b):
        result.extend(b[j:])
    return result


f.readline()
array1 = [int(x) for x in f.readline().split()]
f.readline()
array2 = [int(x) for x in f.readline().split()]
print(" ".join(map(str, merge(array1, array2))))
