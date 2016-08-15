from time import gmtime, strftime

class Log:
    
    message = ""
    
    def __init__(self,file):
        self.file = file
    
    def log(self,message):
        self.message+=message+" "
    
    def flush(self,request):
        with open(self.file,'a') as f:
            pass
            #f.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+" "+request.META['HTTP_X_FORWARDED_FOR']+" \t "+request.META['HTTP_USER_AGENT']+" \t "+request.META['PATH_INFO']+" \t "+self.message+"\n")

            
    