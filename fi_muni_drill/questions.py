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
            multi_answers = ['PV157', 'PV157_midterm','PV119', 'PV203', 'PV120']
            multi = False
            if path in multi_answers:
                multi = True
            for q in data:
                answers = []
                correct = 0
                for a in q['answers']:
                    correct += int(a['right']);
                    answers.append(Answer(a['body'],a['right'],len(answers)))
                if correct>1:
                    multi = True
                self.questions.append(Question(q['name'],answers,multi))



    def getquestion(self, id):
        return self.questions[id]


    def numquestions(self):
        return len(self.questions)
