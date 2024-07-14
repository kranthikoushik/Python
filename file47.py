class St:    
    def __init__(self, name):  
        print("parametrized") #parameterized 
        self.name = name  
    def show(self):  
        print("Hello",self.name)  
student = St("Koushik")  
student.show()
