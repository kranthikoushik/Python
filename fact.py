num=int(input("Enter any number to calculate factorial: "))
fact=1
for i in range(1,num+1):
    fact = fact * i;
print("Factorial of ",num,":", fact)
