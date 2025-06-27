#Special Sequences

import re

txt = "The_ rain $% in Spain 67 67"

b = re.findall(r"\brain",txt)
print(b,end=" ")
if b:
    print("yes!")
else:
    print('No!')

B = re.findall(r"\Brain",txt)
print(B,end=" ")
if B:
    print("yes!")
else:
    print('No!')


d = re.findall(r"\d",txt)
print(d)

D = re.findall(r"\D",txt)
print(D)



s = re.findall(r"\s",txt,1)
print(s)

S = re.findall(r"\S",txt)
print(S)



w = re.findall(r"\w",txt)
print(w)

W = re.findall(r"\W",txt)
print(W)



Z = re.findall(r"67\Z",txt)
print(Z,end=" ")
if Z:
    print("Yes!")
else:
    print("No!")

#Casual Uses:
c = re.findall("ai",txt)
print(c)

