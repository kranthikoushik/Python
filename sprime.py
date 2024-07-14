end=int(input("Find prime numbers between 1 to : "))
sum1=0
for i in range(2,end+1):
        isPrime = 1
        r=i//2
        for j in range(2,r+1):
            if(i%j==0):
                isPrime = 0
                break
        if(isPrime==1):
            sum1=sum1+i
print("Sum od prime numbers from 1 to ",end," = ",sum1)
