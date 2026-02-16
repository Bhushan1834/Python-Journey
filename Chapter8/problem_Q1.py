'''
Q1.write a program using functions to find gratest of three numbers.
'''
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a = 9
b = 59
c = 60
print(greatest(a,b,c))
