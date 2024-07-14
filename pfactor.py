num=int(input("Enter any number to print Prime factors: "))
for i in range(2,num+1):
    if(num%i==0):
        isPrime = 1
        r=i//2
        for j in range(2,r+1):
            if(i%j==0):
                isPrime = 0
                break
        if(isPrime==1):
            print(i,end=' ')
