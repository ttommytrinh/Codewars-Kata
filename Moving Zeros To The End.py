# -*- coding: utf-8 -*-
"""
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.
"""


def move_zeros(array):    
    a = 0
    for i in array:
        if array[a] == 0 and not isinstance(array[a], bool):
            del array[a]
            array.append(0)
        else:
            a += 1         
    return array  