def gc_content(dna):
    gc = 0
    for base in dna:
        if base in 'GC':
            gc += 1
    return gc / len(dna)


def clean_fasta(file):
    data = file.read().split('>')[1:]
    data = [i.split('\n') for i in data]
    data = [[i[0], ''.join(i[1:])] for i in data]
    return data


with open("C:/Users/Pc/PycharmProjects/rosalind/GC/rosalind_gc.txt") as file:
    result = {i[0]: gc_content(i[1]) for i in clean_fasta(file)}
    print(max(result, key=result.get))
    print(result[max(result, key=result.get)] * 100)
