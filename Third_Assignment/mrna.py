
"""
Inferring mRNA from Protein
url: http://rosalind.info/problems/mrna/
Given: A protein string of length at most 1000 aa.
Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
"""
def mrna(protein):
    # Codon table mapping amino acids to codons
    codons = {
        'F': ['UUU', 'UUC'],  # Phenylalanine
        'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],  # Leucine
        'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],  # Serine
        'Y': ['UAU', 'UAC'],  # Tyrosine
        '*': ['UAA', 'UAG', 'UGA'],  # Stop codon
        'C': ['UGU', 'UGC'],  # Cysteine
        'W': ['UGG'],  # Tryptophan
        'P': ['CCU', 'CCC', 'CCA', 'CCG'],  # Proline
        'H': ['CAU', 'CAC'],  # Histidine
        'Q': ['CAA', 'CAG'],  # Glutamine
        'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],  # Arginine
        'V': ['GUU', 'GUC', 'GUA', 'GUG'],  # Valine
        'A': ['GCU', 'GCC', 'GCA', 'GCG'],  # Alanine
        'D': ['GAU', 'GAC'],  # Aspartic Acid
        'E': ['GAA', 'GAG'],  # Glutamic Acid
        'G': ['GGU', 'GGC', 'GGA', 'GGG'],  # Glycine
        'I': ['AUU', 'AUC', 'AUA'],  # Isoleucine
        'M': ['AUG'],  # Methionine (Start codon)
        'T': ['ACU', 'ACC', 'ACA', 'ACG'],  # Threonine
        'N': ['AAU', 'AAC'],  # Asparagine
        'K': ['AAA', 'AAG']  # Lysine
    }
    
    # Initialize the number of possible mRNA sequences
    number = 1
    
    # Iterate over each amino acid in the protein sequence
    for aa in protein:
        # Multiply the number by the number of possible codons for the current amino acid
        number = number * len(codons[aa])
    
    # Multiply the number by the number of stop codons ('*')
    number = number * len(codons["*"])
    
    # Take the modulo of the number to obtain the result within the desired range
    return number % 1000000

f = "MVQNRALGPSMMSFISAQWVYTNNQPFFQHFHGEWIIRMWQESGDVWQLAYVDTMNPGHKAPCIRQVWLFVEVLWSWLFDHPCYKPIDKYNQEVINTFYTSFKINWVIPLDPPRPVHGSMPPPKCKVKVIECYMMMTAYPISCCPPRDGMYAKIWAKCVWIRFHQEKLYCKQMGNWITSSLVVESLLANESLQKGQTNYDLFCAFDHLICSGMYTDYPAAIVCPNINAWPMMNDNNVMWSFRVTWVDQAPIFCTTTLLQVFCWHWDHWHIKTMMNDHENQDDWRETREHTNCSMNQDMPMIVCETTCPEMRHQSANYPWFGMMGQQWWVPLHNYFHDSKLCCMVSFYAVEWNWTYVFGALNYIGFACQMIIRCCNLEMLLYDCEIMSTQDSINQDGHNKMFIYESFDYREMTQGVCGDETTQVLWYADMPPHQNNQEPHHDQRVIAPKWIREGGHLQLMKVNWSAWTEEGAVGCGKDEMKVCMCNSSMSCPCKQQTEVLEAASHGGRHYVYWDVSCFHVYGYPGSKPLFHKPNTHAFNITWIDFTYMTTLVHNPVCWGSLHQIRIPFDHFDMRPRWCFVEFQQSDSCCPNQSPVKTGGAHDLWPLKEQGMSHNAINGMHHPRDFELMRAHCERRMSDLGIYEILMFREDYYLSQNEMCVPQAPTPPWPGWAYSFEFSRILPFLLISCDHLQVVWQTMMQHYWAWYQPAWPPPYQFMEMEIFFGCSINTPITCLRCRLGPFISKSIRYTIQMSWLETPSHVSAECAHAAVEAYSNIENSSPMFVRSQQDEKIYDKNHDDMRFPHKCMENYKDFFGFAPDQLHKATCIAFPTDYNAQIRSNKLISHGGPFEVSFQFVTECLHVCGAPGKYKYHRKFQVWKRICRYKCYHFAVPLSMFWHYGCNLRYEDHPMLTDTKIRFCQFGIMPMDAMKMRWAVVHNICGGIDTRTAIYHQVFCSWVGCKIHNKFLASCNPYANETCCTYHELNHEEHYVKIDSLWANW"
protein = f.strip()
number = mrna(protein)
print(number)
