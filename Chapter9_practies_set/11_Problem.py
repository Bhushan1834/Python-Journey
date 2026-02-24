'''
Q11.Write a Python program to rename a file to 'renamed_by_python.txt'.
'''

with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt") as f:
     f.write(content)   