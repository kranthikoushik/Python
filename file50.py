class func:  
    def read(self):  
        print("Reading") 
class func1(func):  
    def write(self):  
        print("writing")  
d = func1()  
d.read()  
d.write()
