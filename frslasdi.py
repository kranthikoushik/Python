import math
n=int(input("Enter any number: "))
lastDig = n % 10     
digits = (int) (math.log10(n))
frstDig = n // math.pow(10, digits)
print("First digit = ", frstDig)
print("Last digit = ", lastDig)
