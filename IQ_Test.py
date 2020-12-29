"""
Bob is preparing to pass IQ test. The most frequent task in this test is to 
find out which one of the given numbers differs from the others. Bob observed 
that one number usually differs from the others in evenness. Help Bob — to check 
his answers, he needs a program that among the given numbers finds one that is 
different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means 
indexes of the elements start from 1 (not 0)
"""

def iq_test(numbers):
    numbers_list = numbers.split()
    even_counter = 0
    odd_counter = 0
    for x in numbers_list:
        if int(x)%2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    if even_counter == 1:
        for x in numbers_list:
            if int(x)%2==0:
                return(numbers_list.index(x)+1)
    elif odd_counter == 1:
        for x in numbers_list:
            if int(x)%2 != 0:
                return(numbers_list.index(x)+1)