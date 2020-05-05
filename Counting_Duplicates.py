'''
Write a function that will return the count of distinct case-insensitive alphabetic characters
and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and 
numeric digits.
'''
def duplicate_count(text):
    char_counter = {}
    result = 0
    for x in text.upper():
        char_counter.setdefault(x,0)
        char_counter[x] = char_counter[x] + 1
    
    for x in char_counter:
        if char_counter[x] > 1:
            result += 1
    return(result)