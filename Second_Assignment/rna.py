t = "GATGCCACCGCAATTTTGTCGAATCCTCGGCCGTAGGGATTGTGGGATGGTGTTCTTTCTTACGTGATGGTGTATGTTCCATTGGCATAAGTCTGGATACGACCGCGACTTCTATCATGTCAATTCGAGACTTCTGACCTGGACTGAACTCGCACCATTTGTAGGGACAGCAGATCATATCCAGCTGTTGCCTGCGTGCGAACGGTTTACTGGGTTGTTATTTCGCGGAGAATGTGACACGGAAATAACCGCACACCCGGTGTGCCGTTAGCATCCGATATCATGGCGCTATAGAGTAGTTCCTCCCACTGGGTGCAAGTTTTAGTCCGAATGCGCAGCCGGTAATGGGGCAGCCCAAGATCAGCGTTTAGCACAACAGCAATATGCATGTGAGTAGGCCTACTCATCCATAGCTTGCTTTACCATTAGGGGATGGTGCGCGAGTTTAGTTGTCGCAAAGTGTGAGGTCAACCAGAGGCCCACAAATATGAACGATCCTATGTACTACATGTACTTCTGCCCTTACGAACAGCCTTTCCAGTTAATAGTGCTTAGCGTGCCCCAGCGACATAGGCCAAGGGTATGTTAACCACCCTGGCCGGATGCACAATCGTACCGAAGAATACGGTGCCGCTACCCTTGCCACATACGGATTAAATTCTGGCGGAAATTGTGAGTCGTCCCGTTTAAATCACCGACTGGAACACGAATTCAGCACCTGTTCGGCCTAAAACCAGACGGCCTAACGCTCGAGGACCGAGGGTACTATGCGCACCGATTAACTGAAGAAGGTGTCGAGCTCGTGTTTCACGTCCCGCCCGTTGGGGCACATTTATCAAGAGACACGTGCCGTATTAGGGAAACAGAATGACGTAGTCTTTAGAATTTAAGGTCTGATTGCGGCTACCTCCGTCTGAG"
u = ""
for char in t:
    if char in ["A","C","G"]:
        u = u + char
    else:
        u = u + "U"
print(u)