
"""
Enumerating k-mers Lexicographically
url: http://rosalind.info/problems/lexf/
Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n <= 10).
Return: All strings of length that can be formed from the alphabet, ordered lexicographically.
"""

import itertools

with open("rosalind_lexf.txt", 'r') as f:
    string = f.readline().split()  # Read the first line from the file and split it into a list of characters
    n = int(f.readline().strip())  # Read the second line from the file and convert it to an integer
    result = list(itertools.product(string, repeat=n))  # Generate all possible combinations of length n from the characters in the string
    for x in result:  # Iterate over each combination
        print("".join(x))  # Join the characters in the combination and print them


