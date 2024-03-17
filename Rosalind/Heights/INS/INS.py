f = open("rosalind_ins.txt", "r")


# insertion sort
def insertion_sort(arr):
    swap = 0
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            swap += 1
            j -= 1
    print(swap)
    return arr


f.readline()
print(insertion_sort([int(x) for x in f.readline().split()]))
