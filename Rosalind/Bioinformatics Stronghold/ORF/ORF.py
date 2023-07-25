from Bio.Seq import reverse_complement, Seq


def subarreglo_compatible(arr):
    inicio = -1
    seq = ""
    for i in range(0, len(arr) - 2, 3):
        if arr[i:i + 3] == "ATG":
            inicio = i
            break
    if inicio != -1:
        sub_arr = arr[inicio:]
        res = len(sub_arr) % 3
        seq = sub_arr[:len(sub_arr) - res]
    return Seq(seq)


seq = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
rc_seq = reverse_complement(seq)
seqs = []
proteins = set()

for i in range(3):
    seqs.append(subarreglo_compatible(seq[i:]))
    seqs.append(subarreglo_compatible(rc_seq[i:]))

for seq in seqs:
    translated_seq = seq.translate(to_stop=True)
    if translated_seq != "":
        proteins.add(translated_seq)

for protein in proteins:
    print(protein)
