class Employee:
    language = "Python" # This is a class attribute
    salary = 1900000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    @staticmethod
    def greet(self):
        print("Good Morning")

bhushan = Employee()
bhushan.language= "javaScript" #This is an object(instance) attribute 

# bhushan.getInfo()
Employee.getInfo(bhushan)
bhushan.greet()
