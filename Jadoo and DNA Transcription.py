dna = input()
new = ""

for i in dna:
    if i not in 'ATGC':
        new = "Invalid Input"
        break
    if i == 'A':
        new += 'U'
    elif i == 'C':
        new += 'G'
    elif i == 'T':
        new += 'A'
    else:
        new += 'C'

print(new)
