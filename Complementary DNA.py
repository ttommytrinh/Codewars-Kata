# -*- coding: utf-8 -*-
"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and 
carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need 
to get the other complementary side. DNA strand is never empty or there is no DNA at 
all (again, except for Haskell).
"""

def DNA_strand(dna):
    dna_list = [x for x in dna]
    complimentary = []
    for i in dna_list:
        if i == "A":
            complimentary.append("T")
        elif i == "T":
            complimentary.append("A")
        elif i == "G":
            complimentary.append("C")
        else:
            complimentary.append("G")
    return "".join(complimentary)