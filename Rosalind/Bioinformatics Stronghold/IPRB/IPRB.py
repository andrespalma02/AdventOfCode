def mendel(k, m, n):
    total = k + m + n
    prob_dom = k / total
    prob_het = (m / total) * ((0.75 * (m - 1) + k + (0.5 * n)) / (total - 1))
    prob_rec = (n / total) * ((k + (0.5 * m)) / (total - 1))
    return prob_dom + prob_het + prob_rec


# otra solución es sacar el complemento de la probabilidad de que salga un recesivo
# esto solo aplica si n y m son mayores a 0

with open("C:/Users/Pc/PycharmProjects/rosalind/IPRB/rosalind_iprb.txt") as file:
    k, m, n = map(int, file.readline().strip().split())
    print(mendel(k, m, n))
