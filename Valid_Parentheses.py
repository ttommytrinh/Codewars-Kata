# -*- coding: utf-8 -*-
"""
Write a function called that takes a string of parentheses, and determines if 
the order of the parentheses is valid. The function should return true if the 
string is valid, and false if it's invalid.
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Along with opening (() and closing ()) parenthesis, input may contain any valid 
ASCII characters. Furthermore, the input string may be empty and/or not contain
any parentheses at all. Do not treat other forms of brackets as parentheses
(e.g. [], {}, <>).
"""

def valid_parentheses(string):
    string_list = [x for x in string]
    while True:
        if "(" not in string_list and ")" not in string_list:
            return(True)
        elif "(" not in string_list or ")" not in string_list:
            return(False)
        elif string_list.index("(") > string_list.index(")"):
            return(False)
        elif string_list.index("(") < string_list.index(")"):
                first_locator = string_list.index("(")
                second_locator = string_list.index(")")  
                string_list.pop(second_locator)
                string_list.pop(first_locator)
