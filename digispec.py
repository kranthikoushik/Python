x=input("Enter x value:")
if((x[0]>='a' and x[0]<='z') or (x[0]>='A' and x[0]<='Z')):
    print(x[0],"is Alphabet")
elif(x[0]>='0' and x[0]<='9'):
    print(x[0],"is digit")
else:
    print(x[0],"is special Character")
