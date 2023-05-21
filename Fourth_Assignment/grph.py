#!/usr/bin/env python3

"""
Created on Tue May  9 10:32:17 2023

@author: nicolai
"""

from Bio import SeqIO

# Define the input file and n value
data_file = "/home/nicolai/Desktop/Homework 4 Rosalind/rosalind_grph.txt"
n = 3

# Parse the FASTA file and store the sequence names and strings
seq_names = []
seq_strings = []
with open(data_file, 'r') as fasta_file:
    for seq_record in SeqIO.parse(fasta_file, 'fasta'):
        seq_names.append(seq_record.name)
        seq_strings.append(str(seq_record.seq))

# Iterate through each pair of sequences.
for i in range(len(seq_strings)):
    for j in range(len(seq_strings)):
        # Skip comparing a sequence to itself
        if i != j:
            # Check if the last n characters of sequence i match the first n characters of sequence j
            if seq_strings[i][-n:] == seq_strings[j][:n]:
                # Print the names of the two sequences
                print(seq_names[i], seq_names[j])˘