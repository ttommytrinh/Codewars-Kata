'''
You are given an array (which will have a length of at least 3, but could be very large) 
containing integers. The array is either entirely comprised of odd integers or entirely comprised 
of even integers except for a single integer N. Write a method that takes the array as an argument 
and returns this "outlier" N.
'''
def find_outlier(integers):
    even_list = [x for x in integers if x%2==0]
    odd_list = [x for x in integers if x%2==1]
    if len(even_list)==1:
        return(even_list[0])
    else:
        return(odd_list[0])