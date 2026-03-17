class Employee:
    language = "py" # This is a class attribute
    salary = 1900000

bhushan = Employee()
bhushan.name = "bhushan" #This is an object(instance) attribute 
print(bhushan.name, bhushan.language, bhushan.salary)

sachin = Employee()
sachin.name = "Sachin"
print(sachin.name, sachin.language, sachin.salary)

# here name is object(instance) attribute and salary and language are class attribute as they directly belong to the class 