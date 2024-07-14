a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if(a>b and a>c):
    print("a is greater than b and c")
if(b>a and b>c):
    print("b is greater than a and c")
if(c>a and c>b):
    print("c is greater than a and b")
else:
    print("All values are equal")

