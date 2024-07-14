x=input("Enter x value:")
if(x[0]=='a' or x[0]=='e' or x[0]=='i' or x[0]=='o' or x[0]=='u' or x[0]=='A' or x[0]=='E' or x[0]=='I' or x[0]=='O' or x[0]=='U'):
    print(x[0],"is vowel")
elif(x[0]>='a' and x[0]<='z' or x[0]>='A' and x[0]<='Z'):
    print(x[0],"is consonant")
else:
    print(x[0],"is not Alphabet")
