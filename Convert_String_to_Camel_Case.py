'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).
'''

def to_camel_case(text):
    new_text = text.replace("_"," ").replace("-"," ")
    camelcase_list = []
    x = new_text.split(" ")
    
    camelcase_list.append(x[0])
    
    for c in x[1:]:
        camelcase_list.append(c.capitalize())
        
    return("".join(camelcase_list))