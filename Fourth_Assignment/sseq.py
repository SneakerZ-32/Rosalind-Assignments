#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:37:04 2023

@author: nicolai
"""

from Bio import SeqIO

def spliced_motif_founder(s, t):
    # initialize a list to store the positions where each character in t occurs in s
    position = [0]

    # loop through each character in t
    for i in t:
        # find the position of the next occurrence of the current character in s, starting from the end of the previous match
        # add 1 to account for 0-based indexing in Python
        # add the previous position to get the absolute position in s
        position.append(s[position[-1]:].index(i) + 1 + position[-1])

    # print the positions, separated by spaces
    for p in position[1:]:
        print(p, end=" ")

if __name__ == "__main__":
    # load data from a FASTA file
    seq_name, seq_string = [], []
    with open ("/home/nicolai/Desktop/Homework 4 Rosalind/rosalind_sseq.txt",'r') as fa:
        for seq_record in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))

    # extract the sequences s and t from the list of strings
    s, t = seq_string[0], seq_string[1]

    # call the function to find the positions where t is a subsequence of s
    spliced_motif_founder(s, t)
