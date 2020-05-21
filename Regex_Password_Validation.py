'''
You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.
'''

import re
regex= re.compile(r""
^ 
((?=.*\d) 	#at least one digit
(?=.*[a-z]) #at least one lowercase
(?=.*[A-Z]) #at least one uppercase
[a-zA-Z0-9]	#only alphanumberic 
{6,})		#at least 6
$""", re.VERBOSE)