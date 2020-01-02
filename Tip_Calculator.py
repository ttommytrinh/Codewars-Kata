'''
Complete the function, which calculates how much you need to tip based on the 
total amount of the bill and the service.

You need to consider the following ratings:

Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%
The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, 
then you need to return:

"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
...or -1 in C#
Because you're a nice person, you always round up the tip, regardless of the service.
'''

import math

def calculate_tip(amount, rating):
    check_rating = rating.lower()
    if "terrible" == check_rating:
        return(0)
    elif "poor" == check_rating:
        return(math.ceil(amount*0.05))
    elif "good" == check_rating:
        return(math.ceil(amount*0.1))
    elif "great" == check_rating:
        return(math.ceil(amount*0.15))
    elif "excellent" == check_rating:
        return(math.ceil(amount*0.2))
    else:
        return("Rating not recognised")