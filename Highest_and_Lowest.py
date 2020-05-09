'''
In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number.
'''
def high_and_low(numbers):
    number_list = numbers.split()
    for x in number_list:
    	number_list[number_list.index(x)] = int(x)
    return(f"{max(number_list)} {min(number_list)}")