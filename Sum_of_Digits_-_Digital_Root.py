'''
A digital root is the recursive sum of all the digits in a number. 
Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
This is only applicable to the natural numbers.
'''
def digital_root(n):
    num_split = [int(i) for i in str(n)]
    return_num = 0
    while len(num_split) > 1:
        return_num = sum(num_split)
        num_split = [int(i) for i in str(return_num)]
    return(return_num)