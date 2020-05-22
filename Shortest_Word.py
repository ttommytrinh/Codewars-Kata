'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''
def find_short(s):
    word_length = [len(x) for x in s.split()]
    word_length.sort()
    return(word_length[0])

#should've used min(), would've been more efficient and didn't need to sort.