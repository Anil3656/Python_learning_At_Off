import keyword
print(keyword.kwlist)



n = int(input("Enter the n value: "))
fac = 1
if n < 1:
    print("Number should be positive!")
else:
    for i in range(1,n+1):
        fac = fac*i
print(f"Factorial of {n} is: ",fac)

i = 1
while i <= 4:
    j = 1
    while j <= 4:
        print("*", end="  ")
        j += 1
    print()
    i += 1
    
x = input("Enter your name:")
while x == "":
    print("You did't enter your name")
    x = input("Enter your name")
print(f"Hello {x}")