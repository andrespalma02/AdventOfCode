def genome_assembly(data):
    pass


def similarity(string1, string2):
    half = int(len(string1) / 2) + 1
    print(string1[:half - 1], string1[half - 1:], string2[:half - 1], string2[half - 1:])
    if string1[:half - 1] in string2 or \
            string1[half - 1:] in string2 or \
            string2[:half - 1] in string1 or \
            string2[half - 1:] in string1:
        return True
    return False


print(similarity('ATTAGACCTG', 'AGACCTGCCG'))
