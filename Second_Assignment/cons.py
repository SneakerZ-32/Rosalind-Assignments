def consensus(DNAs):
    profile = []
    for i in range(len(DNAs[0])):
        counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}  # Use a dictionary for counts instead of separate variables
        for j in range(len(DNAs)):
            nucleotide = DNAs[j][i]
            counts[nucleotide] += 1
        profile.append([(counts['A'], 'A'), (counts['C'], 'C'), (counts['G'], 'G'), (counts['T'], 'T')])

    consensus = ''
    for row in profile:
        common = max(row, key=lambda x: x[0])  # Use the key argument of max() to specify comparison based on counts
        consensus += common[1]
    print(consensus)

    for i in range(4):
        record = profile[0][i][1] + ': '
        for j in range(len(profile)):
            record += str(profile[j][i][0]) + ' '
        print(record)


with open('rosalind_cons.txt', 'r') as file:
    content = file.read()
DNAs_number, lines, line_number, DNAs = content.count('>'), content.splitlines(), 0, []
for i in range(DNAs_number):
    DNA = ''
    line_number += 1
    while lines[line_number][0] != '>':
        DNA += lines[line_number]
        line_number += 1
        if line_number + 1 > len(lines):
            break
    DNAs.append(DNA)

consensus(DNAs)

