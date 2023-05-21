#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:22:04 2023

@author: nicolai
"""

from Bio import SeqIO

# define a dictionary with codon:amino acid mappings
CODING_TABLE = {
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S',
    'TTT': 'F', 'TTC': 'F',
    'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'TAT': 'Y', 'TAC': 'Y',
    'TGT': 'C', 'TGC': 'C',
    'TGG': 'W', 
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
    'ATG': 'M', 
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 
    'AAT': 'N', 'AAC': 'N', 
    'AAA': 'K', 'AAG': 'K',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'TAA': 'end', 'TAG': 'end', 'TGA': 'end'
}

def RNA_splicing(dna_string, introns):
    """
    This function takes a DNA string and a list of introns,
    removes the introns from the DNA string, and returns the
    protein string translated from the spliced RNA.
    """
    # remove introns from DNA string
    for intron in introns:
        dna_string = dna_string.replace(intron, "")
    
    protein_string  = ""
    
    # translate spliced RNA into protein string
    for i in range(0, len(dna_string)-2, 3):
        codon = dna_string[i:i+3]
        if CODING_TABLE[codon] == "end":
            break
        protein_string += CODING_TABLE[codon]
    
    return protein_string

if __name__ == "__main__":
    # load data
    seq_name, seq_string = [], []
    with open ("/home/nicolai/Desktop/Homework 4 Rosalind/rosalind_splc.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq)) 
    # print(seq_string)
    dna_string, introns = seq_string[0], seq_string[1:]
    rna_string = RNA_splicing(dna_string, introns)
    print(rna_string)