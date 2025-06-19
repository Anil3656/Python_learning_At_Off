str ="Hello World!"
'''#sclicing String Operations
print(str[0:6])  #Except 6th index print 0 to 5
print(str[:6])   
print(str[6:])   #start printing from 6 to end
print(str[:-1])  #printing start from ending to begining 
print(str[-5:-1])'''
#Modify string Operations
'''a = " World! "
print(str.upper())
print(str.lower())
print(a.strip())  #Removes whiteSpaces beggining and ending
print(str.replace('W','B'))   #Repalcing existing letter with new letter
print(str.split())  #It returns result like list '''



pk_movies = {
    'first': 'Akkada Ammai Ekkada Abbai',
    'second': 'Gokulam lo seetha',
    'third': 'Jhony',
    'fourth': 'Balu',
    'fifth': 'Gudumba shankar',
    'sixth': 'Annavaram',
    'seventh': 'Panja',
    'eight': 'Kumaram Puli',
    'ninth': 'Cameraman gangatho Rambabu',
    'tenth': 'Atharintiki dharedhi',
    'eleventh': 'Gabbar Shing',
    'twelve': 'Sardhar Gabbar Shing',
    'thirteen': 'Agnethavsi',
    'fourteen': 'Beemla Nyak',
    'fifteen': 'Vakilsaab',
    'sixteen': 'Hari Hara Vera Mallu',
    'seventeen': 'OG',
    'eighteen': 'Usthadh Baghath Sihing'
}

keys = pk_movies.keys()
print(keys)
values = pk_movies.values()
print(values)

print(f'Moive is: {pk_movies['fifth']}')

n =5
for i in range(1,11):
    print(f'5 X {i} =',(i*n))


for x in range(10):
       if x == 6:
           print(x,end="")
print(x)