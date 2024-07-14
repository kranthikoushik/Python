class emp:    
    id = 10   
    name = "Koushik"    
    def display (self):    
        print(self.id,self.name)
Emp = emp()
del Emp.id    
del Emp #Delete
Emp.display()
