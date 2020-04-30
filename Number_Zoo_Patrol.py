'''
You're working in a number zoo, and it seems that one of the numbers has gone missing!

Zoo workers have no idea what number is missing, and are too incompetent to figure it out, so they're hiring you to do it for them.

In case the zoo loses another number, they want your program to work regardless of how many numbers there are in total.
'''
def find_missing_number(numbers):
    n = len(numbers)+1 #the highest number
    return(n*(n+1)/2 - sum(numbers)) #formula

   
    '''
    The length of the array is n-1. So the sum of all n elements, 
    i.e sum of numbers from 1 to n can be calculated using the formula n*(n+1)/2. 
    Now find the sum of all the elements in the array and subtract it from the sum 
    of first n natural numbers, it will be the value of the missing element.
    '''

 #OTHER SOLUTIONS I TRIED.
 #ITERATING THROUGH EACH INDEX
 def find_missing_number(numbers):
    sorted_list = sorted(numbers) 
    if sorted_list[0] != 1:
        return(1)     
    for x in range(1,len(sorted_list)):
        if sorted_list[x] != x+1:
            return(x+1)      
    return(len(sorted_list)+1)


#BINARY SEARCH-LIKE, CUTTING THE ARRAY IN HALF SEVERAL TIMES THEN INTERATING THROUGH EACH INDEX
def find_missing_number(numbers):
    sorted_list = sorted(numbers)
    if sorted_list[0]!=1:
        return(1)
    while sorted_list[int(len(sorted_list)/2)] == sorted_list[0]+int(len(sorted_list)/2):
        del sorted_list[0:int(len(sorted_list)/2)]
        if len(sorted_list) == 1:
            return(sorted_list[-1]+1)
            break
    while sorted_list[int(len(sorted_list)/2)] <= sorted_list[0]+int(len(sorted_list)/2):
            del sorted_list[:int(len(sorted_list)/2)]
    for x in range(1,len(sorted_list)):
            if sorted_list[x] != sorted_list[0]+x:
                return(sorted_list[0]+x)