class Question():
    
    zle = 0

    def __init__(self, task, answers):
        self.task = task
        self.answers = answers
        self.selected = None
        

    def validate(self,answer):
        for a in self.answers:
            self.zle += a.validate(answer == a.id)
        return self.zle

        

