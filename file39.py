try:  
     num = int(input("Enter a integer: "))  
     if (num <= 0):    
         raise ValueError("It's Negative number")
     if not (num<=0):
         print("It's Positive number")
except ValueError as e:  
     print(e)
