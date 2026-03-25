class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # Dunder method which is automatically called 
        self.name = name
        self.salary = salary 
        self.language = language
        print("I am creating an object")

    def getInfo(self):
            print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
            print("Good morning")

bhushan = Employee("Bhushan", 1300000, "JavaScript")
# bhushan.name = "Bhushan"
print(bhushan.name, bhushan.salary, bhushan.language)

        