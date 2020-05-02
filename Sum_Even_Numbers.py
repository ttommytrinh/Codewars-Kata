'''
Task
Write a function named sumEvenNumbers, taking a sequence of numbers as single parameter. Your function must return the sum of the even values of this sequence.

Only numbers without decimals like 4 or 4.0 can be even.
'''
def sum_even_numbers(seq): 
    return(sum([x for x in seq if x%2 == 0]))