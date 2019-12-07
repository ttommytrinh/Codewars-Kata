'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
'''

def getCount(inputStr):
    num_vowels = 0
    str_list = [letter for letter in inputStr]
    for x in str_list:
        if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
            num_vowels += 1
    return(num_vowels)