# -*- coding: utf-8 -*-
"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
@author: ttomm
"""
def anagrams(word, words):
    word_match = []
    for x in words:
        if len(word) == len(x) and "".join(sorted(word)) in "".join(sorted(x)):
            word_match.append(x)
    return(word_match)
