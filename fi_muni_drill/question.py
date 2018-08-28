class Question():

    zle = 0

    def __init__(self, task, answers, multi):
        self.task = task
        self.answers = answers
        self.selected = None
        self.multi = multi


    def validate(self,answer):
        print(answer)
        for a in self.answers:
            self.zle += a.validate(a.id in answer)
        return self.zle
