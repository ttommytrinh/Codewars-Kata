'''
Given a mixed array of number and string representations of integers, add up the string integers and subtract this from the total of the non-string integers.

Return as a number.
'''

def div_con(x):
    int_list = []
    int_total = 0
    nonint_list = []
    nonint_total = 0
    for item in x:
        if type(item) == int:
            int_list.append(item)
        elif type(item) == str:
            nonint_list.append(item)
    for y in int_list:
        int_total += y
    for z in nonint_list:
        nonint_total += int(z)   
    return(int_total - nonint_total)