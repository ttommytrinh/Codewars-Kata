'''
Write a function that accepts two arguments and generates a sequence containing the integers from the first argument to the second inclusive.

Pair of integers greater than or equal to 0. The second argument will always be greater than or equal to the first.
'''
def generate_integers(m, n): 
    sequence = []
    for x in range (m,n+1):
        sequence.append(x)
    return(sequence)