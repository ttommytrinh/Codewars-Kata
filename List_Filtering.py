'''
In this kata you will create a function that takes a list of non-negative integers
and strings and returns a new list with the strings filtered out.
'''

def filter_list(l):
  integer_list = []
  #Go through each value in l and if integer, append to integer_list
  for x in l:
      if type(x) == int:
          integer_list.append(x)
  return(integer_list)