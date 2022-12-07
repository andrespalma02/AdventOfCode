def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count


# with open("rosalind_ba1a.txt") as file:
#    print(pattern_count(file.readline().strip(), file.readline().strip()))
