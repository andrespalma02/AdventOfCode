# Find the Most Frequent Words with Mismatches in a String
# Given: A string Text as well as integers k and d.
# Return: All most frequent k-mers with up to d mismatches in Text.

# Sample Dataset
# ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4 1

# Sample Output
# GATG ATGC ATGT

f = open("D:\GitKraken\AdventOfCode\Rosalind\Book\BA1I\\rosalind_ba1i.txt", "r")

def approximate_pattern_matching(text, pattern, d):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if sum([1 for x, y in zip(text[i:i + len(pattern)], pattern) if x != y]) <= d:
            positions.append(i)
    return positions

def most_frequent_kmers_with_mismatches(text, k, d):
    kmer_counts = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        for neighbor in neighbors(kmer, d):
            if neighbor in kmer_counts:
                kmer_counts[neighbor] += 1
            else:
                kmer_counts[neighbor] = 1
    max_count = max(kmer_counts.values())
    return [kmer for kmer, count in kmer_counts.items() if count == max_count]

def neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for x in ['A', 'C', 'G', 'T']:
                neighborhood.add(x + text)
        else:
            neighborhood.add(pattern[0] + text)
    return list(neighborhood)

def hamming_distance(s1, s2):
    return sum([1 for x, y in zip(s1, s2) if x != y])

text = f.readline().strip()
k, d = map(int, f.readline().split())
print(" ".join(most_frequent_kmers_with_mismatches(text, k, d)))

