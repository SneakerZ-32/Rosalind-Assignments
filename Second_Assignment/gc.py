start = open('rosalind_gc.txt')  # Open the file 'rosalind_gc.txt'
strands = start.readlines()  # Read the lines of the file into a list
temp = ''  # Temporary variable to store the DNA strands
data = []  # List to store the processed data
counter = 1  # Counter to iterate through the strands

# Extract the DNA strands from the file and store them in the 'data' list
while counter < len(strands):
    if '>' in strands[counter]:  # '>' indicates the start of a new DNA strand
        data.append(temp)  # Add the completed DNA strand to the 'data' list
        data.append(strands[counter])  # Add the strand's name to the 'data' list
        temp = ''  # Reset the temporary variable
        counter += 1
    else:
        temp += strands[counter]  # Concatenate the lines to form the DNA strand
        counter += 1
data.append(temp)  # Add the last DNA strand to the 'data' list
data.insert(0, strands[0])  # Insert the first line (header) to the 'data' list

# Clean up the data by removing newline characters and '>'
for n in range(len(data)):
    data[n] = data[n].replace('\n', '')  # Remove newline characters
    data[n] = data[n].replace('>', '')  # Remove '>' characters

name_of_the_string = ''  # Variable to store the name of the DNA strand with the highest GC content
gc_content = 0  # Variable to store the highest GC content percentage

# Calculate GC content percentage for each DNA strand and find the one with the highest value
for q in range(1, len(data), 2):
    gc = data[q].count('G') + data[q].count('C')  # Count the occurrences of 'G' and 'C' in the DNA strand
    gc_percent = (gc / len(data[q])) * 100  # Calculate the GC content percentage
    if gc_percent > gc_content:  # If the GC content percentage is higher than the previous highest value
        gc_content = gc_percent  # Update the highest GC content percentage
        name_of_the_string = data[q-1]  # Update the name of the DNA strand with the highest GC content

print(name_of_the_string)  # Print the name of the DNA strand with the highest GC content
print(round(gc_content, 6))  # Print the highest GC content percentage, rounded to 6 decimal places

