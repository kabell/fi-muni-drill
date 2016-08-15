from files import Files


class Stats:
    
    stats = {}
    celkovo = None
    
    def __init__(self,request):
        for file in Files().get(True):
            self.stats[file.getname()]=request.session.get('stats',{}).get(file.getname(),[0,0])
        
        self.celkovo = request.session.get('stats',{}).get('celkovo',[0,0])
        '''
        if self.celkovo==None:
            self.celkovo = [0,0]
        '''
        #print self.stats
        #print self.celkovo
        
    def update(self,filename,stat):
        self.add(self.stats[filename],stat)
        self.add(self.celkovo,stat)        
        
        
    def save(self,request):
        request.session['stats']=self.stats
        request.session['stats']['celkovo']=self.celkovo
        
    def add(self,stat,data):
        stat[0]+=data[0]
        stat[1]+=data[1]
        
    def clear(self):
        self.stats={}
        self.celkovo = [0,0]
        