import math
num=int(input("Enter any number: ")) 
lastDig= num % 10
dig= (int)(math.log10(num))
frstDig = num // math.pow(10, dig)
swappedNum  = lastDig;
swappedNum *= (int) (math.pow(10, dig))
swappedNum += num % ((int) (math.pow(10, dig)))
swappedNum -= lastDig
swappedNum += frstDig
print("Original number = ",num)
print("Number after swapping first and last digit: ",int(swappedNum))
