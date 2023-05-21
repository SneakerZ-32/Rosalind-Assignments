#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:02:01 2023

@author: nicolai
"""
def read_fasta(file_path):
    seq = {}
    with open(file_path, 'r') as fp:  # using with to open and close the file automatically
        for line in fp:
            if line.startswith('>'):
                name = line[1:].strip()  # using slice to remove '>' and strip to remove white spaces
                seq[name] = ''
            else:
                seq[name] += line.strip()  # using strip to remove white spaces

    return seq

def coding(s):
    codon_table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S', 'TAT': 'Y', 'TAC': 'Y',
        'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H',
        'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R',
        'AGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T',
        'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V',
        'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E',
        'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    return codon_table[s]

def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement_sequence = ''.join([complement[n] for n in reversed(sequence)])
    return reverse_complement_sequence

def find_ORFs(sequence):
    ORFs = set()  # using set to avoid duplicates

    for frame in range(3):  # considering all three possible reading frames
        codons = [sequence[i:i+3] for i in range(frame, len(sequence) - 2, 3)]  # splitting sequence into codons
        i = 0
        while i < len(codons):
            if codons[i] == 'ATG':  # start codon
                j = i + 1
                while j < len(codons):
                    amino_acid = coding(codons[j])
                    if amino_acid == '~':  # stop codon
                        ORFs.add(''.join(codons[i:j+1]))
                        break
                    j += 1
                i = j + 1
            else:
                i += 1

    return ORFs

