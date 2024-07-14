class Empl:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
emp1 = Empl("Kranthi", 10)  
emp2 = Empl("Koushik", 11)   
emp1.display()    
emp2.display() 
