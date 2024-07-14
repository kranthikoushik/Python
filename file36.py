try:      
    a=int(input("a:"))
    b=int(input("b:"))
    c=a/b
    print(c)
except(ArithmeticError, IOError):      
    print("Arithmetic Exception")      
else:      
    print("It's Done")  
