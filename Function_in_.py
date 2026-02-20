# 1.Built in function:- this function are alreday made by python
# eg. 1.print() 2.len() 3.input() 4.int() 5.float() 6.str() 7.list() 8.tuple() 9.set() 10.dict() etc.   

# 2.User defined function:- this function are made by user as per their requirement
# eg.
def add(a,b):
    return a+b
print(add(5,10))  #output 15

# 3.Function with parameter:- this function take some input from user and perform some operation on it
# eg. 
def square(X):
    return X * X
print(square(2))  #output 25

# 4.Lambda function:- this function are anonymous function which are defined without a name and can be used in a single line of code
# eg. 
square = lambda x: x * x
print(square(5))  #output 25

# 5.Recursive function:- this function call itself in order to solve a problem
# eg. 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  #output 120

