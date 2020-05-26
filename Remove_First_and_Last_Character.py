'''
It's pretty straightforward. 
Your goal is to create a function that removes the first and last characters of a string. 
You're given one parameter, the original string. You don't have to worry with strings with 
less than two characters.
'''
def remove_char(s):
    word_split = [x for x in s]
    word_split.pop(0)
    word_split.pop(-1)
    return("".join(word_split))