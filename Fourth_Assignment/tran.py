#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:01:11 2023

@author: nicolai
"""

from Bio import SeqIO

# Define lists of tuples representing transitions and transversions
TRANSITIONS = [('A', 'G'), ('T', 'C'), ('C', 'T'), ('G', 'A')]
TRANSVERSIONS = [('A', 'T'), ('A', 'C'), ('T', 'A'), ('T', 'G'), ('C', 'A'), ('C', 'G'), ('G', 'T'), ('G', 'C')]

def calculate_transition_transversion_ratio(seq_strings):
    """
    Calculates the ratio of the number of transitions to transversions between two DNA sequences.
    Args:
        seq_strings: a list of two DNA sequences
    Returns:
        A float representing the transition/transversion ratio
    """
    transition_count, transversion_count = 0, 0
    s1, s2 = seq_strings

    # Iterate over the nucleotides in the sequences and count the number of transitions and transversions
    for i in range(len(s1)):
        if (s1[i], s2[i]) in TRANSITIONS:
            transition_count += 1
        if (s1[i], s2[i]) in TRANSVERSIONS:
            transversion_count += 1

    # Calculate and return the transition/transversion ratio
    return transition_count/transversion_count

if __name__ == "__main__":
    seq_name, seq_string = [], []
    with open ("/home/nicolai/Desktop/Homework 4 Rosalind/rosalind_tran.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))

    # Call the function and print the result
    seq_strings = seq_string[0], seq_string[1]
    transition_transversion_ratio = calculate_transition_transversion_ratio(seq_strings)
    print(transition_transversion_ratio)
