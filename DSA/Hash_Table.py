#A Hash Map (also known as a Hash Table) is a data structure that stores key-value pairs and allows for very fast access to values based on their keys.
#A Hash Map uses a "hash function" to compute an index (or hash code) into an array of buckets or slots, from which the desired value can be found.
#It stores (key, value) pairs, and you can retrieve the value quickly by using the key.
'''#  Why Do We Use a Hash Map?
Fast Access Time:
  ->On average, operations like insert, delete, and search are done in O(1) time.

Efficient Lookups:
  ->Ideal for situations where you frequently need to look up data by a unique key (e.g., user ID, product code).

Key-Based Access:
  -> Unlike arrays or lists where access is by index, hash maps let you access data using a meaningful key (like a name or ID).
    
    
    
#Common Use Cases
->Storing data for quick lookup (e.g., dictionary words, user sessions)
->Counting frequency of elements (e.g., word counts)
->Caching data
->Implementing sets (a HashSet uses a hash map under the hood)'''


'''my_hash_Table = {} #empty hash table or dictionary
print(my_hash_Table,type(my_hash_Table))

my_hash_Map = dict()   #In-built function to create an dictionary
print(my_hash_Map,type(my_hash_Map))

#Traditional way to Create a Dictionary
employee_data = {'Name' : "Anna", 'Age' : 23, 'City' : 'Hyderabad'}
print(employee_data['Name'],employee_data['Age'])

#Using dict() function
dict_fun = dict(name ='Ann',Age = 23, city ='Bangalore')
print(dict_fun)
print(dict_fun['city'])
print(type(dict_fun))    #<class 'dict'>'''

#Creating Nested Dictionaries:

'''employee_details ={'Employee' :{'Anna': {'Id': 401,
                                         'Salary' : 50000,
                                         'designation' : "Developer"},
                                'Bunny' : {'Id' : 402,
                                           'Salary' : 600000,
                                           'Designation' : 'ASD'}}}
#Accessing a particular Key
print(employee_details['Employee']['Anna']["Id"])


#Looping Through all employee
for name, details in employee_details['Employee'].items():
    print(f'Name: {name}')
    for key, Value in details.items():
        print(f'{key} : {Value}')'''
        


'''employee_data = {'Name' : "Anna", 'Age' : 23, 'City' : 'Hyderabad'}

#Access using Key values
print(employee_data)
print(employee_data['Name'])


#Access using Functions
print(employee_data.keys())
print(employee_data.values())
print(employee_data.items())
print(employee_data.get('Name'))

#Access through for Loop
for key, value in employee_data.items():
    print(f'{key} : {value}')
    
    
print(employee_data)
#Update the value using Key
employee_data['Age'] = 22
employee_data['City'] = 'Delhi'
print(employee_data)


#Deleting  items from dictionary
#del employee_data['Name']        #Delete Key-value pair
print(employee_data)       

#employee_data.pop('Age')        #removes value of Age
print(employee_data)

employee_data.popitem()          #removes last item in dictionary or Last Inserted item
print(employee_data)'''




'''import pandas as pd
print(pd.__version__)

employee_details ={'Employee' :{'Anna': {'Id': 401,
                                         'Salary' : 50000,
                                         'designation' : "Developer"},
                                'Bunny' : {'Id' : 402,
                                           'Salary' : 600000,
                                           'designation' : 'ASD'}}}


df = pd.DataFrame(employee_details['Employee'])
print(df)'''



#Example programs:
#1.Check if a Key Exists in Hash Table
hash_table = {'fruit' : 'Apple' , 'student' : 'Anil', 'vehicles' : 'Bike'}

if 'student' in hash_table:
    print(hash_table['student'])
else: 
    print('Not present!')
    


#2.Count Frequency of Characters Using Hash Table

text ="Hello_World"
feq = {}
print(type(feq))
for char in text:
    if char in feq:
        feq[char] += 1
    else:
        feq[char] = 1
for char, count in feq.items():
    print(f'{char} : {count}')