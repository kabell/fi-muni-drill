# -*- coding: utf-8 -*-
from fi_muni_drill.question import *
from fi_muni_drill.answer import *
import json
from fi_muni_drill import settings

class Questions():

    questions = []

    def __init__(self, path):

        self.questions=[]

        with open(settings.BASE_DIR+'/data/questions_'+path+'.json', encoding='utf-8') as f:
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








