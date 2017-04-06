from fi_muni_drill.colors import Color

class Answer():

    def __init__(self, answer,correct,id):
        self.id = id
        self.answer = answer
        self.color = 'white'
        
        self.correct = (correct=='true' or correct==True)


    def setcolor(self, color):
        self.color = color
        
    def validate(self,selected):
        
        if self.correct:
            self.setcolor(Color.OK)
            if selected:
                return 0
            else:
                return 1
        if selected:
            self.setcolor(Color.BAD)
            return 1
        return 0
        
            
