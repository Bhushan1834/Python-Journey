# classes and object 
# class Person :
#     pass 
# obj = Person()
# print (type(obj))
# print(obj)

# class Person:
#     name = "bhushan"
#     age = 21
# per = Person()
# print(per.name)
# print(per.age)
# per.hobby = "cricket"
# per . loveName = "Babu"
# print(per.hobby)
# print(per.loveName) 
# obj = Person()
# print(obj.loveName)


# Initializer and constructor

# class Person:
#    #Initializer and constructor for object 
#  def __init__ (self, name,age) : 
#   self.name=name
#   self.age= age
# per1=Person("bhushan",21)
# per2=Person("ram",24)
# print(per1.name)
# print(per2.name)


#2

# class Person:
#     def __init__(self,name, age):
#         self.nmae = name 
#         self.age = age 
#     def __init__(self,name):
#         self.name = name
# per = Person("Bhushan tarte",)  #per = Person("Bhushan tarte",21 it show the error)
# print(per.name)


#3

# class Person :
#   def __init__(self,name, age=21, hobby="cricket"):
#    self.name = name 
#    self.age = age 
#    self.hobby = hobby  
# per1 = Person ("bhushan")
# per2 = Person ("bhushan",21)
# per3 = Person ("bhushan",43,"kho kho")

# print(per1.hobby)
# print(per3.hobby)

#4

# class Person:
#     country = "india"
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age 
# per1 = Person ("bhushan",21)
# per2 = Person ("sachin",20)
# print(per1.name,per1.country)
# print(per2.name,per2.country)

# method and it's types

#1 instance/object method

# class Person :
#    def __init__(self,name,age):
#        self.name= name
#        self.age= age 
#    def findAge(self):
#        return self.name
# per = Person("bhushan",21) 
# print(per.findAge())


#2 class method 

# class Person :
#    country = "india"
#    @classmethod
#    def greet(cls):
#        print("hello from the ",cls.country)

#    def __init__(self,name,age):
#        self.name= name
#        self.age= age 

#    def findAge(self):
#        return self.age
   
# per = Person("bhushan",21) 
# print(per.findAge())

# Person.greet()
# per.greet() call using object 

#3 static method 

# class Person :
#    country = "india"

#    @classmethod
#    def greet(cls):
#        print("hello from the ",cls.country)

#    @staticmethod
#    def hello():
#        print("hello")

#    def __init__(self,name,age):
#        self.name= name
#        self.age= age 

#    def findAge(self):
#        return self.age
   
# per = Person("bhushan",21) 
# print(per.findAge())

# Person.greet()
# per.greet()

# Person.hello()

#1 method overloading 

# class calculator:
#     def add (self ,a,b):
#         return a+b
#     def add (self ,a,b,c):
#         return a+b+c
# cal= calculator()
# print(cal.add(5,6,7))    

#2 implicit method overloding 

# class calculator :
#   def add(self,a,b,c=0):
#     return a+b+c 
# cal = calculator()
# print(cal.add(5,6,7,))
# print(cal.add(5,6))
        

# Access modifier public and private 


#1 

# class Person :
#     def __init__(self,name,age,salary):
#         self.name = name 
#         self. age= age 
#         self.__salary = salary 


#     def findAge(self):
#         return self.age
    
#     def getSalary(self):
#         print(self.__salary)
#         self.__calculateTax()

#     def __calculateTax(self):
#         print("calculating tax")

# per = Person ("bhushan",99,5000)

# print(per.name)
# per.getSalary()

# # per.__calculateSalary()

# print(per._Person__salary)

# print(per._Person__calculateTax())


# encapsulation 

# class Person :
#     def __init__(self,name,car ) baki ahe ajun 



#inheritance 

# class Animal:
#     def __init__(self,name):
#         self.name = name 
#     def eat(self):
#         print(self.name+"animal is eating")

# class Dog(Animal):
#     def __init__(self,name,type):
#         # Animal.__init__(self,name)
#         super().__init__(name)
#         self.type = type

#     def getTheNameOfDog(self):
#         print(self.name)     

# dog = Dog("Moti","Dobberman")
# dog.eat()
# dog.getTheNameOfDog()


# class Parent:
#     property = 90
#     def eat(self):
#         print("Parent eating")

# class Child(Parent):  
#     property = 99

#     def display(self):
#         print("Child property:", self.property)
#         print("Parent property:", super().property)   # Access parent property

#     def eat(self):
#         print("Child eating")

#     def callEat(self):
#         self.eat()         
#         super().eat()      

# obj = Child()
# obj.display()
# obj.callEat()

#Type of inheritance 

#1 single inheritance 

# class Animal:
#     def __init__(self,name):
#         self.name= name
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def __init(self,name,type):
#         super().__init__(name)
#         self.type= type


# #2 multi level inheritance 


# class Animal:
#     def __init__(self,name):
#         self.name= name
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def __init(self,name,type):
#         super().__init__(name)
#         self.type= type

# class Pet(Dog):
#     def __init__(self,name,type,houseName):
#         super().__init__(name,type)
#         self.housNmae = houseName



# #3 Hierarical inheritance

# class Animal:
#     def __init__(self,name):
#         self.name= name
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def __init__(self,name,type):
#         super().__init__(name)
#         self.type= type

# class Cat(Animal):
#     def __init__(self,name,type):
#         super().__init__(name)
#         self.type= type
        
#4 multiple inheritance 

# class A:
#     def meth1(self):
#         print("Hello from A")
# class B :
#     def meth2(self):
#         print("hello from B")        
# class C(A,B):
#     def meth(self):
#         print("hello from the child")

# c= C()
# c.meth1()
# c.meth2()


# class A:
#     def meth(self):
#         print("Hello from A")
# class B :
#     def meth(self):
#         print("hello from B")        
# class C(A,B):
#     def meth1(self):
#         print("hello from the child")

# c= C()
# c.meth()

# class A:
#     def meth2(self):
#         print("Hello from A")
# class B :
#     def meth(self):
#         print("hello from B")        
# class C(A,B):
#     def meth1(self):
#         print("hello from the child")

# c= C()
# c.meth()


# class A:
#     def meth(self):
#         print("Hello from A")
# class B :
#     def meth(self):
#         print("hello from B")        
# class C(B,A):
#     def meth1(self):
#         print("hello from the child")

# c= C()
# c.meth()

# print(C.__mro__)

#5 hybrid inheritance

class Pet(Dog,cat):
    pass