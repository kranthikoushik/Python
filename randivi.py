low=int(input("Enter lower range limit:"))
up=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(low,up+1):
    if(i%n==0):
        print(i)
