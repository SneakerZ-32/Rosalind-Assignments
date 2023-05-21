#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:51:32 2023

@author: nicolai
"""

def factorial(n):
    """
    Computes the factorial of a given integer n.

    Args:
    n (int): The integer to compute the factorial of.

    Returns:
    int: The factorial of n.
    """
    f = 1
    for i in range(n):
        f *= (i+1)
    return f

def permutations(n, k):
    """
    Computes the number of k-length permutations that can be formed from a set of n distinct elements.

    Args:
    n (int): The number of distinct elements in the set.
    k (int): The length of the permutations.

    Returns:
    int: The number of k-length permutations.
    """
    return int(factorial(n)/factorial(n-k)) % 1000000

# Example usage
print(permutations(99, 8))