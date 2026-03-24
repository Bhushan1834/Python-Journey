# Q1)Create a class “Programmer” for storing information of a few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name 
        self.salary = salary
        self.pin = pin

p = Programmer("Bhushan", 1200000,413701)
print(p.name, p.salary, p.pin, p.company)

p = Programmer("Sachin", 1100000,415601)
print(p.name, p.salary, p.pin, p.company)



