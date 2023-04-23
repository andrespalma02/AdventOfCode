# programa para calcular la serie de fibonacci
data = {}


def fib(n):
    args = n
    if args in data:
        return data[args]
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    else:
        answer = fib(n - 1) + fib(n - 2)
    data[args] = answer
    return answer


print(fib(23))
