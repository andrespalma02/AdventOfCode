def overlap_graph(patterns):
    adj_list = []
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            if patterns[i][1][-3:] == patterns[j][1][:3] and i != j:
                adj_list.append(patterns[i][0] + ' ' + patterns[j][0])
    return adj_list


def clean_fasta(file):
    data = file.read().split('>')[1:]
    data = [i.split('\n') for i in data]
    data = [[i[0], ''.join(i[1:])] for i in data]
    return data


with open("C:/Users/Pc/PycharmProjects/rosalind/GRPH/rosalind_grph.txt") as file:
    print("\n".join(overlap_graph(clean_fasta(file))))
