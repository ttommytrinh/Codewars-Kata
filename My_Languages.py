'''
You are given a dictionary/hash/object containing some languages and your test results 
in the given languages. Return the list of languages where your test score is at least 60, 
in descending order of the results.

Note: the scores will always be unique (so no duplicate values)
'''
def my_languages(results):
    sorted_dict = sorted((value,key) for (key,value) in results.items())
    reverse_list = sorted_dict[::-1]
    return_list = []
    for x in reverse_list:
        if x[0] >= 60:
            return_list.append(x[1])
    return(return_list)