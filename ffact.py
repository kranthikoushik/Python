def func():
    n=int(input("Enter the Number:"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("The Fact of ",n,":",fact)
func()
