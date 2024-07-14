#global Variable


x=30
def matt():
    global x
    print(x) 
    x = "Kranthi Koushik" #Modifying the value
    print(x)
    
matt()
print(x)
