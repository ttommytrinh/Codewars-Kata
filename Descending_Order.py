'''
Your task is to make a function that can take any non-negative integer as a argument 
and return it with its digits in descending order. Essentially, rearrange the digits 
to create the highest possible number.
'''
def descending_order(num):
    num_split = [x for x in str(num)]
    num_split.sort(reverse=True)
    return(int("".join(num_split)))