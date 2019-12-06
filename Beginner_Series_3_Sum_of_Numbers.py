'''
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
'''


def get_sum(a,b):
    sum = 0
    #when a is greater
    if a > b:
        for x in range(b,a+1):
            sum += x
    #when b is greater
    elif b > a:
        for x in range(a,b+1):
            sum += x
    #when they equal
    elif a == b:
        sum = a
    return(sum)