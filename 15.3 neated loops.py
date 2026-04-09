#nested lops 

# for i in range(10):
#     for j in range(5):
#         print("Bhushan tarte ")


# for i in range(4):
#     for j in range(1,13):
#         if j%4==0:
#          break
#     print(j)        

for i in range(4):
    for j in range(1,13):
        if j%2 !=0:
            continue
        print(j)