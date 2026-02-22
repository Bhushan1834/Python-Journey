st = " Hey Bhushan you are amazing"

f = open("myfile.txt", "a") # append mode is used to add content to the end of the file without overwriting it  
f.write(st)
f.close()