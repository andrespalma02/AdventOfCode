def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])


with open("rosalind_ba1c.txt") as file:
    print(reverse_complement(file.readline().strip()))
