a1=int(input("Enter angle1:"))
a2=int(input("Enter angle2:"))
a3=int(input("Enter angle3:"))
sum=a1+a2+a3
if sum==180 and a1!=0 and a2!=0 and a3!=0:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
