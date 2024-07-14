try:    
    fileptr = open("file2.txt","r")      
    try:    
        fileptr.write("Hello")    
    finally:    
        fileptr.close()    
        print("file closed")    
except:    
    print("Error")
