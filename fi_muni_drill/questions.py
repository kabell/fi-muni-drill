from question import *
from answer import *
import json


class Questions():

    questions = []

    def __init__(self, path):

        self.questions=[]

        with open('data/'+path+'.json') as f:
            data = json.load(f)
            for q in data:
                answers = []
                for a in q['answers']:
                    answers.append(Answer(a['body'],a['right'],len(answers)))
                self.questions.append(Question(q['name'],answers))
                                


    def getquestion(self, id):
        return self.questions[id]


    def numquestions(self):
        return len(self.questions)








