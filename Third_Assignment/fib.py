
"""
Rabbits and Recurrence Relations
url:http://rosalind.info/problems/fib/
Given: Positive integers  and .
Return: The total number of rabbit pairs that will be present after  months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of  rabbit pairs (instead of only 1 pair).
"""

def fib(n, k):
    if n <= 2:
        return 1
    else:
        return fib(n-1,k) + k * fib(n-2,k)


print(fib(int(36), int(3)))