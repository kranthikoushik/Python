def cal(*sumc):    
    sum=0    
    for sum1 in sumc:    
        sum = sum +sum1 #Global
    print("Sum:",sum)    
sum=0    
cal(10,20,30)    
print("Ouside the Function:",sum)      
