'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''

def accum(s):
    char_list = []
    multiplier = 1
    for char in s:
        char_list.append(char*multiplier)
        multiplier += 1
    for i in char_list:
        char_list[char_list.index(i)] = i.title()
    return("-".join(char_list))