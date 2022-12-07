from Rosalind.Book.BA1A.BA1A import pattern_count


def frequent_words(text, k):
    frequent_patterns = []
    count = []
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i + k]
        count.append(pattern_count(text, pattern))
    max_count = max(count)
    for i in range(0, len(text) - k + 1):
        if count[i] == max_count:
            frequent_patterns.append(text[i:i + k])
    frequent_patterns = sorted(list(set(frequent_patterns)))
    return frequent_patterns


with open("rosalind_ba1b.txt") as file:
    print(" ".join(frequent_words(file.readline().strip(), int(file.readline().strip()))))
