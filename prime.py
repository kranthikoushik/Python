isPrime = 1
num=int(input("Enter any number to check prime: "))
r=num//2
for i in range(2,r+1):
    if(num%i==0):
        isPrime = 0
        break
if(isPrime == 1):
    print(num," is prime number")
else:
    print(num," is composite number")
