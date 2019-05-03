class File:
    def __init__(self,name):
        self.name = name
    
    def getname(self):
        return self.name



class Files:
    
    def __init__(self):
        self.files = [File('PV004'),File('IB101'),File('PB071'),File('VB035'),File('VB036'),File('PB151'),File('PV065'),File('PV080'),File('PV080_midterm'),File('PV119'),File('PV157'),File('PV157_midterm'),File('PV120'),File('PV203'),File('PA179')]
        
    def get(self,mode=False):
        return self.files
