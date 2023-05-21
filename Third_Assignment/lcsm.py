from Bio import SeqIO

sequences = []  # Initialize an empty list to store the sequences

# Open the file 'rosalind_lcsm.txt' for reading
with open('rosalind_lcsm.txt', 'r') as handle:
    # Parse the file using SeqIO to extract the sequences
    for record in SeqIO.parse(handle, 'fasta'):
        sequence = []  # Initialize an empty list to store the nucleotides of the sequence
        seq = ''  # Initialize an empty string to build the sequence
        for nt in record.seq:
            seq += nt  # Append each nucleotide to the sequence string
        sequences.append(seq)  # Add the complete sequence to the list of sequences

# Sort the sequences based on their lengths in ascending order
sorted_sequences = sorted(sequences, key=len)
short_seq = sorted_sequences[0]  # Get the shortest sequence
comp_seq = sorted_sequences[1:]  # Get the remaining sequences

motif = ''  # Initialize an empty string to store the longest common motif

# Iterate over each index in the shortest sequence
for i in range(len(short_seq)):
    # Iterate over each index starting from i to the end of the shortest sequence
    for j in range(i, len(short_seq)):
        m = short_seq[i:j + 1]  # Extract the substring from i to j+1
        found = False  # Initialize a flag to track if the motif is found in all other sequences

        # Iterate over each sequence in the remaining sequences
        for sequ in comp_seq:
            if m in sequ:  # Check if the motif is present in the current sequence
                found = True  # Set the flag to True
            else:
                found = False  # Set the flag to False if the motif is not present in any sequence
                break  # Break out of the inner loop since the motif is not present in the current sequence

        # Check if the motif is found in all other sequences and its length is greater than the current motif
        if found and len(m) > len(motif):
            motif = m  # Update the longest common motif

print(motif)  # Print the longest common motif

