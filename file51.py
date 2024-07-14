from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("Tesla mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("Suzuki mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("Duster mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("Renault mileage is 27kmph ")
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  
