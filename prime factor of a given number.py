a=int(input("give"))
for i in range (2,a+1):
    if a % i == 0:
        c=0

        for v in range (2,i):
            if i %v==0:
                c=1
                break
        if c == 0:
            print(i)

            
