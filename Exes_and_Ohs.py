'''
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive. 
The string can contain any char.
'''

def xo(s):
    x_counter = 0
    o_counter = 0
    for char in s:
        if "x" == char.lower():
            x_counter += 1
        elif "o" == char.lower():
            o_counter +=1
    if x_counter == o_counter:
        return True
    else:
        return False