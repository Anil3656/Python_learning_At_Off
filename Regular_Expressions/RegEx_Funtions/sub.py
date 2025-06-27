#The sub() function replaces the matches with the text of your choice.

import re

txt = "A brown fox jumps over the lazy dog!"
#Replace every white-space character with the number _ underscore
sub = re.sub(" ","_",txt)
print(sub)

#You can control the number of replacements by specifying the count parameter.
#Replace the first n occurrences
n = 2
sub1 = re.sub(" ","_",txt,n)
print(sub1)