'''
Welcome.

In this kata you are required to, given a string, 
replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
'''
def alphabet_position(text):
    text_num = []
    for char in text:
        if ord(char.lower())>=97 and ord(char.lower())<=122:
            text_num.append(str(ord(char.lower())-96))
    return " ".join(text_num)
