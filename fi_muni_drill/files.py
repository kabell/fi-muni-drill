class File:
    def __init__(self,name):
        self.name = name
    
    def getname(self):
        return self.name



class Files:
    
    def __init__(self):
        self.files = [File('PV004'),File('IB101'),File('PB071'),File('VB035')]
        
    def get(self,mode=False):
        return self.files