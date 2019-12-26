'''
The first century spans from the year 1 up to and including the year 100, 
The second - from the year 101 up to and including the year 200, etc.
'''

def century(year):
    if year % 100 == 0:
        return(int(year/100))
    else:
        return(int(year/100) + 1)