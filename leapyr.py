x=int(input("Enter x value:"))
if x%400==0:
    print(x,"is a leap year")
elif x%100==0 or x%4==0:
    print(x,"is a leap year")
else:
    print(x,"is not a leap year")
