def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"


def main():
    marks = int(input("Enter student marks: "))
    grade = calculate_grade(marks)
    print("Student Grade is:", grade)
main()