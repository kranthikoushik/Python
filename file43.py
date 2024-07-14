class car:  
    def __init__(self,name, yr):  
        self.name = name  
        self.yr = yr  
    def display(self):  
        print(self.name,self.yr)  
  
c1 = car("Toyota", 2024)  
c1.display()
