CODON_TABLE = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G',
}

AMINOACID_TABLE = {
    'F': 'Phe', 'L': 'Leu', 'I': 'Ile', 'M': 'Met',
    'V': 'Val', 'S': 'Ser', 'P': 'Pro', 'T': 'Thr',
    'A': 'Ala', 'Y': 'Tyr', 'H': 'His', 'N': 'Asn',
    'D': 'Asp', 'Q': 'Gln', 'K': 'Lys', 'E': 'Glu',
    'C': 'Cys', 'W': 'Trp', 'R': 'Arg', 'G': 'Gly',
    'Stop': 'Stop',
}

COMPLEMENTARY_DNA_BASES = {
    'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
}

COMPLEMENTARY_RNA_BASES = {
    'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C',
}
