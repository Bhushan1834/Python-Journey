'''
Q4.A file contains a word "Donkey" multiple times. Write a program to replace this word with ##### by updating the same file.
'''
word = "Donkey"

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word,"######")

with open("file.txt", "w") as f:
     f.write(contentNew)
