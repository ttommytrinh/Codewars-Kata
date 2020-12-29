
"""
This time we want to write calculations using functions and get the results.
Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: 
    plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function 
represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
"""

import math
def zero(x=None): 
    if x == None:
        return 0
    elif x[0]=="+":
        return (0 + x[1])
    elif x[0]=="-":
        return (0 - x[1])
    elif x[0]=="*":
        return (0 * x[1])
    elif x[0]=="/":
        return math.floor(0 / x[1])
def one(x=None): 
    if x == None:
        return 1
    elif x[0]=="+":
        return (1 + x[1])
    elif x[0]=="-":
        return (1 - x[1])
    elif x[0]=="*":
        return (1 * x[1])
    elif x[0]=="/":
        return math.floor(1 / x[1])
def two(x=None): 
    if x == None:
        return 2
    elif x[0]=="+":
        return (2 + x[1])
    elif x[0]=="-":
        return (2 - x[1])
    elif x[0]=="*":
        return (2 * x[1])
    elif x[0]=="/":
        return math.floor(2 / x[1])
def three(x=None): 
    if x == None:
        return 3
    elif x[0]=="+":
        return (3 + x[1])
    elif x[0]=="-":
        return (3 - x[1])
    elif x[0]=="*":
        return (3 * x[1])
    elif x[0]=="/":
        return math.floor(3 / x[1])
def four(x=None): 
    if x == None:
        return 4
    elif x[0]=="+":
        return (4 + x[1])
    elif x[0]=="-":
        return (4 - x[1])
    elif x[0]=="*":
        return (4 * x[1])
    elif x[0]=="/":
        return math.floor(4 / x[1])
def five(x=None): 
    if x == None:
        return 5
    elif x[0]=="+":
        return (5 + x[1])
    elif x[0]=="-":
        return (5 - x[1])
    elif x[0]=="*":
        return (5 * x[1])
    elif x[0]=="/":
        return math.floor(5 / x[1])
def six(x=None): 
    if x == None:
        return 6
    elif x[0]=="+":
        return (6 + x[1])
    elif x[0]=="-":
        return (6 - x[1])
    elif x[0]=="*":
        return (6 * x[1])
    elif x[0]=="/":
        return math.floor(6 / x[1])
def seven(x=None): 
    if x == None:
        return 7
    elif x[0]=="+":
        return (7 + x[1])
    elif x[0]=="-":
        return (7 - x[1])
    elif x[0]=="*":
        return (7 * x[1])
    elif x[0]=="/":
        return math.floor(7 / x[1])
def eight(x=None): 
    if x == None:
        return 8
    elif x[0]=="+":
        return (8 + x[1])
    elif x[0]=="-":
        return (8 - x[1])
    elif x[0]=="*":
        return (8 * x[1])
    elif x[0]=="/":
        return math.floor(8 / x[1])
def nine(x=None): 
    if x == None:
        return 9
    elif x[0]=="+":
        return (9 + x[1])
    elif x[0]=="-":
        return (9 - x[1])
    elif x[0]=="*":
        return (9 * x[1])
    elif x[0]=="/":
        return math.floor(9 / x[1])

def plus(x): 
    return ["+", x]
def minus(x):     
    return ["-", x]
def times(x):     
    return ["*", x]
def divided_by(x):     
    return ["/", x]