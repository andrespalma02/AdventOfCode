# f(n)=f(n-1)+3*f(n-2)
# f(n)=total de conejos del mes pasado + 3*total de conejos del mes pasado que se reproducen
# o sea total de conejos de hace dos meses
def wascally_wabbits(n, k):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return wascally_wabbits(n - 1, k) + k * wascally_wabbits(n - 2, k)


data = {}


def wascally_wabbits_dynamic(n, k):
    args = (n, k)
    if args in data:
        return data[args]
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    else:
        answer = wascally_wabbits_dynamic(n - 1, k) + k * wascally_wabbits_dynamic(n - 2, k)
    data[args] = answer
    return answer


with open("C:/Users/Pc/PycharmProjects/rosalind/FIB/rosalind_fib.txt") as file:
    n, k = map(int, file.readline().strip().split())
    print(wascally_wabbits_dynamic(n, k))
