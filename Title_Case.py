'''
A string is considered to be in title case if each word in the string is either
(a) capitalised (that is, only the first letter of the word is in upper case) or
(b) considered to be an exception and put entirely into lower case unless it is the first word, 
which is always capitalised.

Write a function that will convert a string into title case, 
given an optional list of exceptions (minor words). 
The list of minor words will be given as a string with each word separated by a space. 
Your function should ignore the case of the minor words string.
It should behave in the same way even if the case of the minor word string is changed.

###Arguments (Haskell)

First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
Second argument: the original string to be converted.

###Arguments (Other languages)

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase
except for the first word in the string. 
The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
'''

def title_case(title, minor_words=" "):
    title_words = title.lower().split()
    if len(title_words) == 0:
        return("")
    minor_check = minor_words.lower().split()
    title_answer = []
    title_answer.append(title_words.pop(0).capitalize())
    for x in title_words:
        if x in minor_check:
            title_answer.append(x)
        else:
            title_answer.append(x.capitalize())
    return(" ".join(title_answer))