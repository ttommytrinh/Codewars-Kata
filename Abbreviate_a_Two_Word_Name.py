'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
'''
def abbrevName(name):
    name_list = name.split()
    return(name_list[0][0].upper()+"."+name_list[1][0].upper())