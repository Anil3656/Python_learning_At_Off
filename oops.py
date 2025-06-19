'''
------------------------------------------------------ 
     Concept	                 Description
------------------------------------------------------
      Class	            Blueprint for creating objects
      Object	        Instance of a class
    Attribute	        Variable inside an object
     Method	            Function inside a class
   Encapsulation	    Hide internal details
    Inheritance	        One class inherits from another
   Polymorphism	        Same method name, different class-specific behavior'''

#Class 

'''class Dog:   #Here dog class is created
    name = 'Sanjay'  #Static or Class Variable
    def __init__(self,name,breed,colour,weight):   #This __init__ method Automatically execute
        self.name = name    #Instance variable or global variable
        self.breed = breed
        self.colour = colour
        self.weight = weight

        name = 'rakesh'
        print(name)
dog = Dog('Lucky','shizu','white',5)  #Here Create One object for inside Attributes
print(dog.__dict__)
print(dog.name)
print(dog.breed)
print(Dog.name)'''

#class Dog: defines a new class named Dog.
#__init__ is the constructor method that runs when an object is created.
#self refers to the instance of the class.

#Object creation: dog = Dog('Lucky','shizu','white',5)


#Encapsulation? //Bundling data (attributes) and methods (functions) that operate on that data into a single unit (class), while restricting direct access to some of the object's components.
# it’s about keeping internal details private and exposing only what’s necessary.

'''Python uses naming conventions to define access levels:
Access Modifiers in Python (Not Strict, But Conventional)
----------------------------------------------------------
Syntax          	        Meaning
----------------------------------------------------------
public	         name    –> accessible from anywhere
protected   	 _name   –> for internal use, not enforced
private	         __name  –> name mangling makes it hard to access'''

'''class Bank:
    def __init__(self,balance):
        self.__balance = balance     #Private Attribute 

    def deposit(self,amount):
        print('{:.2f}/-'.format(amount))
        if amount > 0:
            self.__balance = amount + self.__balance
    def withdraw(self,amount):
        print('{:.2f}/-'.format(amount))
        if 0 < amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print('Invalid withdraw Amount')
    def get_balance(self):
        return 'remaing Balance:',(f"{self.__balance:.2f}/-")  
bank = Bank(float(input('Enter Amount: ')))
bank.deposit(float(input('Enter DepositAmount: ')))
print(bank.get_balance())
bank.withdraw(float(input('Enter WithdrawAmount: ')))
print(bank.get_balance())'''

'''
-------------------------------------------------------------------
Feature                  	            Explanation
-------------------------------------------------------------------
Encapsulation	         Wrapping data and behavior into one unit
Goal	                 Hide internal state and protect data
Private fields	         Defined using __double_underscore
Getter/Setter	         Control how data is accessed and modified
@property	             Pythonic way to define getters and setters'''


'''#Inheritance ? // An a exsisting class drives by new class or Sub class is called Inheritance
#A parent class driven by Childs classes, Inherites parents behaviors to child classes
class Human:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def self_details(self):
        print(f'My name is: {self.name}')
        print(f'My age is: {self.age}')
        print(f'I belongs to: {self.city}')

    def eat(self):
        print(f'{self.name} eating!')
    
    def sleep(self):
        print(f'{self.name} Sleeping!')

    def play(self):
        print(f'{self.name} Playing!')
class Man(Human):
    def __init__(self, name, age, city, gender):
        super().__init__(name, age, city)
        self.gender = gender

class Women(Human):
    def __init__(self, name, age, city, gender):
        super().__init__(name, age, city)
        self.gender = gender
man = Man('Ak',22,'Nellore','Male')
women = Women('Abc',19,'Hyderabad','Female')
print(man.__dict__)
print(women.__dict__)
print()
print(man.name)
print(man.age)
print(man.city)
print(man.gender)
print()
print(women.name)
print(women.age)
print(women.city)
print(women.gender)
print()
man.self_details()
print()
women.self_details()
print()
man.eat()
man.sleep()
man.play()
women.eat()
women.sleep()
women.play()'''



'''#Polymorpshism ?/// Different classes have method with same name,But differnt Behaviors is called Polymorphism
class Dog:
    def speak(self):
        print("Boow! Boow!")
class Cat:
    def speak(self):
       print("Meow! Meow!") 
def make_animal_speak(animal):
    animal.speak()
    
make_animal_speak(Dog())
make_animal_speak(Cat())'''


'''class Animal:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    
    def eat(self):
        print(f'{self.name} eating!')
    
    def sleep(self):
        print(f'{self.name} Sleeping!')

    def play(self):
        print(f'{self.name} Playing!')

class Dog(Animal):
    def __init__(self, name, type,speed):
        super().__init__(name, type)
        self.speed = speed
class Tiger(Animal):
    def __init__(self, name, type,colour):
        super().__init__(name, type)
        self.colour = colour
class Cow(Animal):
    def __init__(self, name, type,food):
        super().__init__(name, type)
        self.food = food

dog = Dog('Maxi','wild','120Kmph')
tiger = Tiger('Chintu','wild','orange')
cow = Cow('ramu','Non-wild','grass&leaves')

print(dog.__dict__)
print(tiger.__dict__)
print(cow.__dict__)


dog.eat()
cow.eat()

print(dog.speed)'''


gender = 'Male'   #Global Variable
class Employee: #Class Method
    group = 'A'   #Class Variable  
    def __init__(self,name,Id,salary): 
        self.name = name  #Instance variable
        self.Id = Id
        self.salary = salary

        global city   #Global variable with global KeyWord
        city = 'Hyderabad'
        #print(city)

class  Rakesh(Employee):   #Static Method
    def __init__(self, name, Id, salary,city):
        super().__init__(name, Id, salary)
        self.city = city
    

class Srinu(Employee):    #Static Method
    def __init__(self, name, Id, salary):
        super().__init__(name, Id, salary)


srinu = Srinu('Srinu',401,250000)
rakesh = Rakesh('rakesh',501,500000,city = 'Chennai')

emp = Employee.group


print(gender)

print(emp)
print(city)

print(srinu.name)
print(type(rakesh.name))

print(rakesh.__dict__, type(rakesh.__dict__))




