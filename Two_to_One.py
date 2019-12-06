'''
Take 2 strings s1 and s2 including only letters from a to z. 
Return a new sorted string, the longest possible, containing distinct letters
'''

def longest(s1, s2):
    list_s1 = [x for x in s1]
    list_s2 = [x for x in s2]
    final_list = list_s1 + list_s2
    return("".join(sorted(set(final_list))))
