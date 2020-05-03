'''
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter needs to be converted to its ASCII code.
The second letter needs to be switched with the last letter
Keepin' it simple: There are no special characters in input.
'''
def encrypt_this(text):
    if not text:
        return("")
    else:
        text_list = text.split(" ")
        ascii_per_word = [ord(x[0]) for x in text_list]
        no_1st_letter = [word[1:] for word in text_list]
        for word in no_1st_letter:
            if len(word)>=2:
                word_split = list(word)
                word_split[0], word_split[-1] = word_split[-1], word_split[0]
                no_1st_letter[no_1st_letter.index(word)] = "".join(word_split)
            else:
                pass
        combined = [f"{ascii_per_word[i]}{no_1st_letter[i]}" for i in range(len(ascii_per_word))]    
        return(" ".join(combined))