#The split() function returns a list where the string has been split at each match.
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split(r"\d", txt)
print(x)

x = re.split(r"\d", txt)
print(x)


#You can control the number of occurrences by specifying the "maxsplit" parameter:
#Split the string only at the first occurrence:

x = re.split(r"\s", txt)
print(x)

txt1 = "The number 1 is grater than 2 and 3"
x = re.split(r"\d",txt1,3)
print(x)

x = re.split("[a-d]",txt)
print(x)