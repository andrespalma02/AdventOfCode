def expected_offspring(k, m, n, o, p):
    return 2 * (k + m + n + 0.75 * o + 0.5 * p)


with open("C:/Users/Pc/PycharmProjects/rosalind/IEV/rosalind_iev.txt") as file:
    a, b, c, d, e, f = map(int, file.readline().strip().split())
    print(expected_offspring(a, b, c, d, e))
