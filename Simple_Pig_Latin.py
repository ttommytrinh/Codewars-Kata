"""
Move the first letter of each word to the end of it, then add "ay" to the end 
of the word. Leave punctuation marks untouched.
"""
import string 

def pig_it(text):
    text_list = text.split()
    index = 0
    for word in text_list:
        if word in string.punctuation:
            pass
        else:
            text_list[index] = word[1:] + word[0] +  "ay"
            index += 1
    return " ".join(text_list)