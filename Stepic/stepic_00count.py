# coding=utf8
# Find times a pattern appears in a text, allows overlapping

def PatternCount (text, pattern):
    #Number of times a k-mer pattern appears as substring of text
    k = len(pattern)
    count = 0    # contador
    for itext in range(len(text)-k+1):
        if text[itext:itext+k] == pattern:
            count += 1
    return count

Text = 'ACAACTATGCATACTATCGGGAACTATCCT'
Pattern = 'ACTAT'

#Reading file with DNA sequence
with open('stepic_count3.txt','r') as leo:
    Text = leo.readline().strip()
    Pattern = leo.readline().strip()

print PatternCount( Text, Pattern)