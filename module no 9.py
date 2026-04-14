# def firstFunction():
#  print("hello bhushan ")
# firstFunction()

# parameter & argument 
# def add(a,b):
#     sum = a + b
#     return sum 
# print(add(20,10))

# variable in function (global & local scope)
 
# x = 101 #global variable/scope
# def func():
#     x = 102 
#     print(x)
# func()
# print(x)    

#  default argument

# def greet(name,message ="good morning"):
#     print(name,message)
# greet("Bhushan")

# keyword arguments 

# def greet(name, age, message):
#     print(message, name,"your age is",age )

# greet(age=21,message="hello",name="bhushan")

# positional argument

# def add_numbers(x, y):
#     print("x",y)
#     print("y",x)
#     print(x+y)
# add_numbers(6,7)




#kwargs in python 

# def disply_info(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key,value,in kwargs .items ():
#      print(key,"-.",value )
# disply_info(name="bhushan",age=21,city="pune")

# def func(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
# func(5,6,3,5,1,name="bhushan",age=21)

# def func1(**kwargs, a,b):
#     print(kwargs)
#     print(a)
#     print(b)                            # A **kwargs is a last parameter it's always define as last other wise it give the error 
# func1(name="bhushan",age=21 ,7,8)



# pass by value
num = 5
def modify_num(num):
    num +=1
    print(num)

modify_num(num)
print("original num ", num)