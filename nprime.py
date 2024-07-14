end=int(input("Find prime numbers between 1 to : "))
print("All prime numbers between 1 to ",end," are:")
for i in range(2,end+1):
        isPrime = 1
        r=i//2
        for j in range(2,r+1):
            if(i%j==0):
                isPrime = 0
                break
        if(isPrime==1):
            print(i,end=' ')
