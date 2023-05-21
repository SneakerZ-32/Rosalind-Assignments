#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:28:32 2023

@author: nicolai
"""

from Bio import SeqIO

# Function to get the overlap between two strings
def _get_overlap_strings(s1, s2):
    combine_strings = []
    overlap_strings = []
    # Iterate over s1 and check if it matches the end of s2
    for i in range(len(s1)):
        if s1[i:] == s2[:len(s1)-i]:
            overlap_strings.append(s1[i:])
            combine_strings.append(s1+s2[len(s1)-i:])
            break
    # Iterate over s2 and check if it matches the end of s1
    for i in range(len(s2)):
        if s2[i:] == s1[:len(s2)-i]:
            overlap_strings.append(s2[i:])
            combine_strings.append(s2+s1[len(s2)-i:])
            break
    # If no overlap is found, return empty strings
    if not overlap_strings:
        return "", ""

    # Find the shortest combined string and the longest overlap
    combine_string = min(combine_strings, key=len)
    overlap_string = max(overlap_strings, key=len)
    return combine_string, overlap_string

# Function to find the shortest superstring from a list of strings
def find_shortest_superstring(strings):
    temp = strings

    # Combine strings until there is only one left
    while len(temp) > 1:
        most_overlapping_string = ""
        most_overlapping_string_pair = []
        most_overlapping_string_length = 0

        # Find the two strings with the most overlap
        for i in range(len(temp)-1):
            for j in range(i+1, len(temp)):
                combine_string, overlap_string = _get_overlap_strings(temp[i], temp[j])
                if len(overlap_string) > most_overlapping_string_length:
                    most_overlapping_string = combine_string
                    most_overlapping_string_pair = [temp[i], temp[j]]
                    most_overlapping_string_length = len(overlap_string)

        # Remove the two strings with the most overlap and add the combined string
        temp.remove(most_overlapping_string_pair[0])
        temp.remove(most_overlapping_string_pair[1])
        temp.append(most_overlapping_string)
        
    return temp[0]

if __name__ == "__main__":
    # Load data from a fasta file
    seq_name, seq_string = [], []
    with open ("/home/nicolai/Desktop/Homework 4 Rosalind/rosalind_long.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))

    # Find the shortest superstring and print it
    shortest_superstring = find_shortest_superstring(seq_string)
    print(shortest_superstring)
