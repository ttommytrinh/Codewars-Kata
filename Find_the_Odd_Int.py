'''
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''
def find_it(seq):
    count = {}

    for number in seq:
        count.setdefault(number, 0)
        count[number] = count[number] + 1
    
    for number in count:
        if count[number]%2 == 1:
            return(number)
