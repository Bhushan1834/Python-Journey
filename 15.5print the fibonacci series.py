n = int (input ("Please enter the value of n - upto which we want the fibonacci series "))
if (n<=0):
    print("Number entered is not currect . It should be > 0 . Enter num",n)
    print(1,end=",")
    if (n==1):
        pass
    else:
        print(2,end= ",")
        if (n==2):
            pass
        else:
            prev = 1
            prev_prev = 1
            for num in range(3,n+1):
                print(prev+prev_prev,end=",")
                prev,prev_prev = prev+prev_prev,prev
