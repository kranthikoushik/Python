class Ercode(Exception):      
    def __init__(self, data):      
        self.data = data      
    def __str__(self):      
        return repr(self.data)      
      
try:      
    raise Ercode(2000)      
except Ercode as ae:      
    print("Received error:", ae.data)
