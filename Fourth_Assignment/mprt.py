#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:04:32 2023

@author: nicolai

  """          
      
        
# import urllib.request module to make HTTP requests
import urllib.request

# open the text file containing the protein IDs
with open('/home/nicolai/Desktop/Homework 4 Rosalind/rosalind_mprt.txt') as txt:
    record_dict = {}  # create a dictionary to store the records
    for pid in txt:
        protid = pid.strip()  # remove any trailing whitespaces or newlines
        url = f"https://www.uniprot.org/uniprot/{protid}.fasta"  # create URL for the protein record
        try:
            data = urllib.request.urlopen(url).read().decode('utf-8')  # make HTTP request and read the response
        except urllib.error.HTTPError:  # catch HTTP errors (e.g., record not found)
            print(f"No record found for {protid}. Skipping...")
            continue  # move to the next protein ID
        seq = ''.join(data.split('\n')[1:])  # extract the amino acid sequence from the FASTA record
        record_dict[protid] = seq  # store the sequence in the dictionary

solution_dict = {}  # create a dictionary to store the solutions
for protid, seq in record_dict.items():
    solution_dict[protid] = []  # create an empty list to store the positions of the motif
    for i in range(len(seq)-4):  # iterate over all positions in the sequence, except the last 4
        if seq[i] == 'N' and seq[i+1] != 'P' and seq[i+2] in ('S', 'T') and seq[i+3] != 'P':  # check if the motif is present
            solution_dict[protid].append(str(i+1))  # store the position of the motif

for protid, positions in solution_dict.items():
    if positions:  # check if the protein has any motifs
        print(protid)
        print(' '.join(positions))  # print the positions of the motifs separated by spaces

