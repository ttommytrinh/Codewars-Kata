'''
Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.
'''

def create_phone_number(n):
    first3 = ""
    for x in range(0,3):
        first3 += str(n[x])
    second3 = ""
    for x in range(3,6):
        second3 += str(n[x])
    last4 = ""
    for x in range(6,10):
        last4 += str(n[x])
    return "(" + first3 + ") " + second3 + "-" + last4