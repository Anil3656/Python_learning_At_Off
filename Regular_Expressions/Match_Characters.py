import re

# -> []
txt = "A brown fox jumps over the lazy dog!"
x = re.findall("[a-p]", txt)
print(x)
# for w in x:
# print(w)

# ->.
txt = "A brown fox jumps over the lazy dog!"
check = re.findall("br..n", txt)
print(check)

# ->\
txt = "Manny give's 30\- rupees to Kezie basu"
digit = re.findall("\d", txt)
print(digit, end=" ")

if digit:
    print("Yes!")
else:
    print('No!')

# ->^ start with "^hello"
txt = "Hello World!"
start = re.findall("^Hello", txt)
print(start, end=" ")

if start:
    print("Text start with hello!")
else:
    print("Not started!")

# ->$ Ended with "world$"
end = re.findall("rld!$", txt)
print(end, end=" ")
if end:
    print("Text ended with World!")
else:
    print("Not Ended!")

# ->* Zero or more occurrences
txt = "hello Anilo"
occurrence = re.findall("he.*o", txt)
print(occurrence)

# ->+ One or more occurrences
txt = "hello world old mood road"
occurrence = re.findall("he.+o", txt)
print(occurrence)

# ->? Zero or one occurrences
txt = "hello world old mood road"  # Output: []
# txt = "helolo world old mood road"  #Output: ['helo']
# txt = "heololo world old mood road" #Output: ['heo']
occurrence = re.findall("he.?o", txt)
print(occurrence)

# ->{value of occurrence}  Exactly the specified number of occurrences
txt = "Hell o hello!"
occurrence = re.findall("he.{3}o", txt)
print(occurrence)

# ->|	Either or
txt = "Hello my dear friend!"
# either =  re.findall(" | ",txt)  #Output: [' ', ' ', ' ']
# either =  re.findall("my|me",txt)    #Output: ['my']
# either =  re.findall("my|dear",txt) #Output: ['my', 'dear']
either = re.findall("|",
                    txt)  # Output: ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
either = re.findall("llo|end", txt)  # Output:['llo', 'end']
print(either)