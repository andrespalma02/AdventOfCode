from cffi.backend_ctypes import xrange

data = {}


def wascally_wabbits_dynamic(n, k):
    args = (n, k)
    if args in data:
        return data[args]
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    elif n == 2:
        answer = 1
    elif n < k + 1:
        answer = wascally_wabbits_dynamic(n - 1, k) + wascally_wabbits_dynamic(n - 2, k)
    elif n == k + 1:
        answer = wascally_wabbits_dynamic(n - 1, k) + wascally_wabbits_dynamic(n - 2, k) - 1
    else:
        answer = wascally_wabbits_dynamic(n - 1, k) + wascally_wabbits_dynamic(n - 2, k) - wascally_wabbits_dynamic(
            n - k - 1, k)
    data[args] = answer
    return answer


def fib(month, age):
    generation = [0] * age
    generation[0], generation[1] = 0, 1
    for x in range(2, month):
        temp = list(generation)
        generation[0] = sum(generation[1:])  # number of new born
        for i in range(1, age):
            generation[i] = temp[i - 1]
    return sum(generation)

# mejor solución
def fib2(x, y):
    ages = [1] + [0] * (y - 1)
    for i in xrange(x - 1):
        print(ages)
        print([sum(ages[1:])], ages[:-1])
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)


with open("C:/Users/Pc/PycharmProjects/rosalind/FIBD/rosalind_fibd.txt") as file:
    n, k = map(int, file.readline().strip().split())
    print(fib(n, k))
    print(fib2(n, k))
    print(wascally_wabbits_dynamic(n, k))
