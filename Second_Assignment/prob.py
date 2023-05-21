
"""
Introduction to Random Strings
url: http://rosalind.info/problems/prob
Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
"""

import math

with open("rosalind_prob.txt", "r") as f:
    s = f.readline().strip()  # Read the DNA sequence from the file and remove leading/trailing whitespaces
    A = map(float, f.readline().strip().split(" "))  # Read the list of probabilities and convert them to floats

a = s.count('A') + s.count('T')  # Count the occurrences of 'A' and 'T' in the DNA sequence
c = s.count('C') + s.count('G')  # Count the occurrences of 'C' and 'G' in the DNA sequence

for i in A:
    # Calculate the probability of the given base composition 'A' and the probabilities 'i'
    p = a * math.log((1 - i) / 2, 10) + c * math.log(i / 2, 10)
    print(p, end=" ")  # Print the calculated probability, separated by a space


