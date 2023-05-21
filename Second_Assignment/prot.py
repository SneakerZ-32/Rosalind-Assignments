RNA = open('rosalind_prot.txt').read()  # Read the RNA sequence from the file
n = 3  # Set the length of each codon to 3 nucleotides
protein_string = ''  # Initialize an empty string to store the protein sequence
codon_seq = [RNA[i:i+n] for i in range(0, len(RNA)-2, n)]  # Split the RNA sequence into codons

codon_map = open('PROT.txt').readlines()  # Read the codon map from the file
dictionary = {}  # Initialize an empty dictionary to store the codon translations

# Populate the dictionary with codon mappings
for el in codon_map:
    el = el.strip().split()  # Split each line into codon and protein symbol
    dictionary[el[0]] = el[1]  # Add the codon-protein mapping to the dictionary

# Translate each codon to its corresponding protein symbol
for el in codon_seq:
    if el in dictionary:
        protein_string += dictionary.get(el)  # Append the protein symbol to the protein sequence

print(protein_string)  # Print the resulting protein sequence

