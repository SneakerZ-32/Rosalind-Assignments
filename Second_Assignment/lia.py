
"""
Independent Alleles
url: http://rosalind.info/problems/lia/
Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
"""

def factorial(n):
    # Calculate the factorial of a given number 'n'
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def combination(i, j):
    # Calculate the combination of 'i' choose 'j'
    return factorial(i) // (factorial(j) * factorial(i - j))

def independent_alleles(k, n):
    # Calculate the probability of at least 'n' AaBb offspring in 'k' generations
    probability = 0
    total_count = pow(2, k)  # Total number of individuals in the generation

    for i in range(n, total_count+1):
        # Calculate the probability of getting 'i' AaBb offspring
        probability += combination(total_count, i) * pow(0.25, i) * pow(0.75, total_count - i)

    return probability

if __name__ == "__main__":
    with open("rosalind_lia.txt", "r") as f:
        k, n = [int(i) for i in f.readline().strip().split(" ")]  # Read the values of 'k' and 'n' from the file

    print(independent_alleles(k, n))  # Print the probability of at least 'n' AaBb offspring in 'k' generations

