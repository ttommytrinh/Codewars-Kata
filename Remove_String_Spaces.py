'''
Simple, remove the spaces from the string, then return the resultant string.
'''

def no_space(x):
    string_list = x.split()
    return("".join(string_list))