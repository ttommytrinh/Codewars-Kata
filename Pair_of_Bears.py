'''
In order to prove it's success and gain funding, the wilderness zoo needs to prove to 
environmentalists that it has x number of mating pairs of bears.

You must check within string(s) to find all of the mating pairs, 
and return a string containing only them. Line them up for inspection.

Rules: Bears are either 'B' (male) or '8' (female), 
Bears must be together in male/female pairs 'B8' or '8B', 
Mating pairs must involve two distinct bears each
('B8B' may look fun, but does not count as two pairs).

Return an array containing a string of only the mating pairs available. 
e.g: 'EvHB8KN8ik8BiyxfeyKBmiCMj' ---> 'B88B' (empty string if there are no pairs)
and true if the number is more than or equal to x,
false if not:
(6, 'EvHB8KN8ik8BiyxfeyKBmiCMj') ---> ['B88B', false];
x will always be a positive integer, and s will never be empty.
'''

def bears(x,s):
    counter = 0
    i = 0
    s_list = [char for char in s]
    mate_list = []
    final_answer = []        
    while 2<=len(s_list):
        if s_list[i]!="8" and s_list[i]!="B":
            s_list.pop(i)
            continue
        if s_list[i]=="8" and s_list[i+1]=="B":           
            mate_list.append(s_list.pop(i))
            mate_list.append(s_list.pop(i))
            counter += 1
            continue
        if s_list[i]=="B" and s_list[i+1]=="8":           
            mate_list.append(s_list.pop(i))
            mate_list.append(s_list.pop(i))
            counter += 1
            continue
        if s_list[i]=="8" and s_list[i+1]!="B":
            s_list.pop(i)
            continue
        if s_list[i]=="B" and s_list[i+1]!="8":
            s_list.pop(i)
            continue            
        else:
            break
    final_answer.append("".join(mate_list))
    if counter >= x:
        final_answer.append(True)
    else:
        final_answer.append(False)
    return(final_answer)