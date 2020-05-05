'''
Write a function, persistence, that takes in a positive parameter num and returns its 
multiplicative persistence, which is the number of times you must multiply the digits in num 
until you reach a single digit.
'''
import numpy
def persistence(n):
    number_split = [int(x) for x in str(n)]
    counter = 0
    while len(number_split) > 1:
        result = numpy.product(number_split)
        number_split = [int(x) for x in str(result)]
        counter += 1
    return(counter)