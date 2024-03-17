def count_subsets_modulo(n):
    MOD = 10**6
    return pow(2, n, MOD)

# Example usage:
n = int(input("Enter a positive integer (n <= 1000): "))
result = count_subsets_modulo(n)
print("Total number of subsets modulo 1,000,000:", result)
