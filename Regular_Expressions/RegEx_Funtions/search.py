#The search() function searches the string for a match, and returns a Match object if there is a match.
#If there is more than one match, only the first occurrence of the match will be returned.
import re

txt = "A broown fox jumps oover the lazy doog!"
se = re.search(r"oo",txt)
print(se)
print("first white space character is located position:",se.start())

#If no matches are found, the value None is returned:
No_Match = re.search("Spain",txt)
print(No_Match)

No_Match = re.search("oover",txt)
print("Span of matched string:",No_Match.span())      # output: (19, 24)

se1 = re.search(r"\W",txt)
print("Match first white space in String:",se1)

se2 = re.search("[a-n]",txt)
print("Matched character in string: ",se2)

se3 = re.search("[123]",txt)
print(se3)




txt1 ="The rain in spain at 11:30 pm"

se4 = re.search("[123]",txt1)
print(se4)

se5 = re.search("[arn]",txt)
print(se)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x)
print(x.span())


x = re.search(r"\bs\w+", txt)
print(x)
#print(x.span())

x  =re.search(r"\bS\w+",txt)
print(x)
print(x.string)

x  =re.search(r"\bs\w+",txt)
print(x)
#print(x.string)

x = re.search(r"\bS\w+",txt)
print(x)
print(x.group())

x = re.search(r"Sp..n",txt)
print("Sp..n:",x)

x = re.search("ra.+n",txt)
print(x)

x = re.search("ra.*n",txt)
print(x)

x = re.search("ra.{2}n",txt)
print(x)

x = re.search("r.{2}n",txt)
print(x)