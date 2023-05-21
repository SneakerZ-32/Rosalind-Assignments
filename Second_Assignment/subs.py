
"""
Finding a Motif in DNA
url: http://rosalind.info/problems/subs/
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""

def subs(string1, string2):
    loc = []  # Initialize an empty list to store the positions where string2 occurs in string1
    for i in range(len(string1)):
        if string2 == string1[i: i+len(string2)]:  # Check if the substring of string1 matches string2
            loc.append(i+1)  # If there is a match, add the position (index + 1) to the loc list
    return loc  # Return the list of positions

if __name__ == "__main__":
    with open("rosalind_subs.txt", 'r') as f:
        string1 = f.readline().strip()  # Read the first line from the file and assign it to string1
        string2 = f.readline().strip()  # Read the second line from the file and assign it to string2
    loc = subs(string1, string2)  # Call the subs function to find the positions of string2 in string1
    for i in loc:
        print(i, end=" ")  # Print each position separated by a space


