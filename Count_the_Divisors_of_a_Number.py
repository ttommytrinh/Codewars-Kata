'''
Count the number of divisors of a positive integer n.
'''
def divisors(n):
    count = 1
    for number in range(1,n):
        if n%number == 0:
            count += 1
    return(count)