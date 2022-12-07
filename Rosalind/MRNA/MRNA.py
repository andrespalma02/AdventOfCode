from Rosalind.CONSTANTS import CODON_TABLE


def infer_mrna_from_protein(protein):
    possible_rna = 1
    for aminoacid in protein:
        possible_rna *= len([i for i in CODON_TABLE.values() if i == aminoacid])
    possible_rna *= len([i for i in CODON_TABLE.values() if i == 'Stop'])
    return possible_rna % 1000000


with open("C:/Users/Pc/PycharmProjects/rosalind/MRNA/rosalind_mrna.txt") as file:
    protein = file.readline().strip()
    print(infer_mrna_from_protein(protein))
