#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:43:34 2023

@author: nicolai
"""
from Bio import SeqIO

# define a function to calculate factorial of a given number
def factorial(n):
    f = 1
    for i in range(n):
        f *= (i+1)
    return f

# define a function to calculate the perfect matching of RNA bases
def pmch(s):
    a = s.count('A') # count the number of Adenine bases
    c = s.count('C') # count the number of Cytosine bases
    return factorial(a) * factorial(c) # return the product of factorials of A and C

if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open ("/home/nicolai/Desktop/Homework 4 Rosalind/rosalind_pmch.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    string = seq_string[0] # get the RNA string from the input file
    print( pmch(string) ) # call the pmch function with the RNA string as input and print the result
