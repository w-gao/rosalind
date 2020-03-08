
# Counting DNA Nucleotides

file = open('rosalind_dna.txt', 'r')
data = file.read()
file.close()

print(data.count('A'), data.count('C'), data.count('G'), data.count('T'))
