'''
File I/O means reading data from a file and writing data to a file using a program.


Input → Taking data from a file (reading).
Output → Saving data into a file (writing)

use File I/O?

To save data permanently.
To store user information.
To read large data (like datasets).
To keep records for future use.

'''


f = open("file.txt")
data = f.read()
print(data)
f.close()