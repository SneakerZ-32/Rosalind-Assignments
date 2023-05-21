s = "CCGCTCTAGAAGGAAAATAAACGTATACCGTGTACTACCTTAGACGGGTGAGTAGCCGGGACTGTAATCACATGCTACCGTTTTCTTAGGGCCTGCGATTCGTCATCCACGTGTCATTAAATACTAACAGGCTGTGATGCCAGAGATTTTGCCCCCAACTAAGCACAACGGGTACGGACTTCCAATGCGCGATATAATACTCCAAGGAGTCCCAACGGGTTCGTATAAATAAGCAGATGTTCGCGACCCTCTCTTTATTACGCGCAGATGCGCGTCCTATTGCCTTGTGTATAAGATGGATTTTTTGTGCGAGTCCACGGGATAGTTCGGGACTCCCGGGTAAGTGTGCTGAGGGAGACATACGCCACCATACCTTGTGACGCTAACCAGACACAACTAGCACTAGACCGAGGGTCCTATCAGATCGGGCCAGGCACTACCGACGTGAAGCGCCAGCGCTAGACATCCTATCTGGAGTTCTGCACATCCCATGCTGTCTAATGAGAGAAAAGGGGTGTCCAGAACGTCCTCAGGACTAGAAGAGCCCGAGACTTTAAGCTGCGCTATTGCAGTATGTAGGCATAGCCATGTAAGCGTACCCGCCGCCGCTCTAACGACGCAGCAGTGGAACCCAGATGAAGACAGCCACAAACAAGCGGCTCGCGCACTTCTAGAGTGACCAGACGGAGCGCATTCATTTCATTGATTTTTCTGTATCCTGAAGAATTGCCTAATGCAGGCGATGTGAGCACCCAGAACCGAGTGCCAACACGAAGTCGTCTGGGTACACGACTGGTCAGCGTCCCGCGTAAGTCAAAAGCTAGCCACCCTGGTCGCCTTTCGACATGTTTACGCCCAAGTCAGATATAACTCGCCGGACCCTGCGCGACCCCTGTGATTTCTACGCC"

def base_counter(s):
    adenines = 0  # Counter for adenines
    citosines = 0  # Counter for cytosines
    timines = 0  # Counter for thymines
    guanines = 0  # Counter for guanines
    
    for char in s:  # Iterate through each character in the string
        if char == "A":
            adenines += 1  # Increment the adenine count if the character is 'A'
        if char == "C":
            citosines += 1  # Increment the cytosine count if the character is 'C'
        if char == "G":
            guanines += 1  # Increment the guanine count if the character is 'G'
        if char == "T":
            timines += 1  # Increment the thymine count if the character is 'T'
        # else:
            # print("Unknown character in string! Please recompile.")
            # It seems like the commented else block was meant to handle unknown characters.
            # Instead of printing an error message, it might be better to raise an exception or return an error value.

    # Print the counts of each nucleotide
    print("A's=", adenines, "C's=", citosines, "G's=", guanines, "T's=", timines)

# Assuming 's' is a string containing nucleotide characters
base_counter(s)

