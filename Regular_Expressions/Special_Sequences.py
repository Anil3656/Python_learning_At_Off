# A special sequence is a "\" followed by one of the characters in the list below, and has a special meaning.
import re
# ->\A  Returns a match if the specified characters are at the beginning of the string
txt = "The rain in Spain"
beginning = re.findall(r"\AThe", txt)
print(beginning, end=" ")

if beginning:
    print("yes!")
else:
    print("No!")

# ->\b Returns a match where the specified characters are at the beginning or at the end of a word
txt = "The rain in Spain"
# beginning1 = re.findall(r"\bain",txt) #output: [] No!
beginning1 = re.findall(r"\brain", txt)  # output: ['rain'] yes!
print(beginning1, end=" ")

if beginning1:
    print("yes!")
else:
    print("No!")

# ->\B  Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
txt = "Ram went to market"
#beginning2 = re.findall(r"mar\B", txt)  # output: ['mar'] yes!
# beginning2 = re.findall(r"\Bket",txt)  #output: ['ket'] yes!
beginning2 = re.findall(r"ent\B", txt)  # output: ['ent'] No!
print(beginning2, end=" ")

if beginning2:
    print("yes!")
else:
    print("No!")

# ->\d Returns if any decimal values present in String between[0-9]
txt = "Manny give me 234 rupees in break"
digit = re.findall(r"\d", txt)  # output: ['2', '3', '4']
print(digit)

# ->\D Returns if any decimal values present in String between[0-9] except that prints every character.
txt = "Manny give me 234 "
digit = re.findall(r"\D", txt)  # output: ['M', 'a', 'n', 'n', 'y', ' ', 'g', 'i', 'v', 'e', ' ', 'm', 'e', ' ', ' ']
print(digit)

# ->\s Returns White space in string
txt = "Manny give me 234 "
space = re.findall(r"\s", txt)  # output: [' ', ' ', ' ', ' ']
print(space)

# ->\S Returns Except White space and return every character in string
txt = "Manny give me _234 "
space = re.findall(r"\S", txt)  # output: ['M', 'a', 'n', 'n', 'y', 'g', 'i', 'v', 'e', 'm', 'e', '_', '2', '3', '4']
print(space)

# ->\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
txt = "1.Everything will be fine  1_day"
word = re.findall("\w",
                  txt)  # output: ['1', 'E', 'v', 'e', 'r', 'y', 't', 'h', 'i', 'n', 'g', 'w', 'i', 'l', 'l', 'b', 'e', 'f', 'i', 'n', 'e', '1', '_', 'd', 'a', 'y']
print(word)

# ->\w  Returns Except the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
txt = "1.Everything %$^$^& will be fine  1_day"
word = re.findall("\W", txt)  # output: ['.', ' ', '%', '$', '^', '$', '^', '&', ' ', ' ', ' ', ' ', ' ']
print(word)

# ->\Z	Returns a match if the specified characters are at the end of the string
txt = "Rahul studying play class"
last = re.findall(r"ss\Z", txt)
print(last, end=" ")

if last:
    print("Yes!")
else:
    print("No!")