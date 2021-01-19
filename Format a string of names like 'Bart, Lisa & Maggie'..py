# -*- coding: utf-8 -*-
"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for 
the last two names, which should be separated by an ampersand.
"""


def namelist(names):
    if len(names) == 0:
        return('')
    elif len(names) == 1:
        return(names[0]['name'])
    elif len(names) == 2:
        string = names[-2]['name']+ " & " + names[-1]['name']
    else:
        string = names[0]['name']
        for x in range(1,len(names)-2):
            string += ", " + names[x]['name']
        string += ", " + names[-2]['name']+ " & " + names[-1]['name']
    return(string)