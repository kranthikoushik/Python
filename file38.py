try:    
    age = int(input("Age:"))    
    if(age<18):    
        raise ValueError   
    else:    
        print("Age is valid")    
except ValueError:    
    print("Age is not valid")
