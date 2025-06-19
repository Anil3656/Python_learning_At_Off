'''#Creating an List and Performing some operations (Mutable)................................
my_built_in_list = list()

my_list1 = [1,2,3]

my_list = [10,30,20,"Hi","True",40,50,70,80]

#my_list.append(90)

my_list.insert(3,35)

my_list.sort()

list = my_list.count(20)
print(list)

#my_list.pop()

#my_list.remove(30)

ind = my_list.index(50)
print(ind)

#my_list.clear()

cop = my_list.copy()
print(cop)

my_list.extend(my_list1)
print(my_list)

my_list.reverse()
print(my_list)

#Creating an Tuple and Performing some operations (Immutable)................................
my_built_in_tuple = tuple()
print(my_built_in_tuple)

my_tuple = (10,20,30,40,50,50,60,70)
print(my_tuple)

tuple = my_tuple.index(30)     #fetch the index by using value
print(tuple)

tuple_count = my_tuple.count(50)
print(tuple_count)

print(my_tuple[1])  #fetch the value by using Index

#Creating an Set and Performing some operations (mutable).................................

my_in_built_set = set()
print(my_in_built_set)
my_set1 = {1,2,3}
my_set = {10,20,30,40,50,60,70,80}
print(my_set)

print(len(my_set))
print(max(my_set))
print(min(my_set))

#my_set.add(90)

my_set.update(my_set1)
print(my_set)

print(my_set.difference(my_set1))
print(my_set.intersection(my_set1))
print(my_set.union(my_set1))
print(my_set.symmetric_difference(my_set1))



#Creating Dictionary and performing some operations

my_built_in_dict = dict()
print(my_built_in_dict)
my_dict1 = {"age": 30,
            "Gender" : "male"}
my_dict = {"name" : "Jhon",
           "age" : 25,
           "pin_code" : 50001,
           "city" : "Hyedrabad"
           }
print(my_dict)

#Fetching values using Keys
print(my_dict["name"])
print(my_dict["pin_code"])
print(my_dict["city"])
print(my_dict["age"])

print(len(my_dict))
print(max(my_dict))
print(min(my_dict))

keys = my_dict.keys()
print(keys)

vales = my_dict.values()
print(vales)

get_name = my_dict.get("name")
print(get_name)


my_dict.update(my_dict1)
print(my_dict)



set = my_dict.setdefault("my_dict1", 100)
print(set)
print(my_dict)


#my_dict.clear()
my_dict.pop("my_dict1")
print(my_dict)'''


'''#Operation On String.............................................    
my_str1 = "****"
my_str = "Hello World!"

print(len(my_str))

upper = my_str.upper()
print(upper)

lower  = my_str.lower()
print(lower)

cap = my_str.capitalize()
print(cap)

count = my_str.count("Hello World")
print(count)

format = my_str.format("Hello world")
print(format)

title = my_str.title()
print(title)

join = my_str.join(my_str1)
print(join)

n = int(input("Enter n value: "))
for i in range(n):
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
for i in range(n-1):
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()


for i in range(n):
    for s in range(n-i-1):
        print(' ',end='')
    for j in range(i+1):
        print(chr(65),end=' ')
    print()

for i in range(n):
    print(' '*(n-i-1), end='')
    for j in range(i+1):
        print('*',end=' ')
    print()'''


my_list = [1,2,3,4,5,6,7,8,9,0]
ind = my_list.index(int(input("Enter the number in List: ")))
print('Index Number:',ind)