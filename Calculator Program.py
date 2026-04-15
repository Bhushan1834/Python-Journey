# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("Addition:", num1 + num2)
# print("Subtraction:", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Division:", num1 / num2)


import random
def check_palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Input
word = input("Enter a word: ")
check_palindrome(word)