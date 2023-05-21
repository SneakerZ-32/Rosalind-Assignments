import math
import itertools

n = 5

# Calculate the factorial of n using the math module
print(math.factorial(n))

# Generate permutations of numbers from 1 to n
perm = itertools.permutations(list(range(1, n + 1)))

# Enumerate through the permutations and print them
for i, j in enumerate(list(perm)):
    permut = ''
    for item in j:
        permut += str(item) + ' '
    print(permut)

