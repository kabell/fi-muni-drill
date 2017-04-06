# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from fi_muni_drill.question import *
from fi_muni_drill.answer import *
from fi_muni_drill.questions import *
from fi_muni_drill.stats import *
from fi_muni_drill.jokes import *
from fi_muni_drill.log import *
import random
import os
from django.http import HttpRequest  
from time import gmtime, strftime
from  fi_muni_drill import settings



def index(request):
    return render_to_response('index.html', locals())

def question(request, mode=None, filename=None, id=None, poradie=None, answer=None):

    rootURL = settings.rootURL    
    files = [f.getname() for f in Files().get()]
    log = Log(settings.BASE_DIR+'/log/access.log')
    
    # validating arrguments
    if mode==None:
        index=True
        return render_to_response('question.html', locals())

        
    id=int(id)-1
    if answer:
        answer = int(answer)
    
    
    # loading data from session
    stats = Stats(request)
    zle_otazky_dict = request.session.get('zle_otazky',{})
    zle_otazky_dict[filename] = zle_otazky_dict.get(filename,[])
    

    # loading question
    questions = Questions(filename)
    question = questions.getquestion(id)
    question.task=question.task.replace(u'Je následující tvrzení pravdivé?',u'<b>Je následující tvrzení pravdivé?</b>')
    question.task=question.task.replace(u'Je následující tvrzení pro jazyk C pravdivé?',u'<b>Je následující tvrzení pro jazyk C pravdivé?</b>')

    # preparing question
    if mode=='question' or mode=='clear':
        if mode=='clear':
            stats.clear()
            zle_otazky_dict={}
        
        random.shuffle(question.answers)
        poradie = ""
        for a in question.answers:
            poradie+=str(a.id)
            #print a.id
            
    
    elif mode == 'validate':
        result = question.validate(answer)
        if result == 0:
            stats.update(filename,[1,1])
            log.log('OK')
        else:
            zle_otazky_dict[filename].append(id+1)
            stats.update(filename,[0,1])
            log.log('BAD')
            
        for i in range(len(poradie)):
            question.answers[int(poradie[i])].key = i

        question.answers.sort(key=lambda Answer: Answer.key)
        
    # saving variables to session
    
    stats.save(request)
    request.session['zle_otazky']=zle_otazky_dict

            
    # generating variables
    
    questions_count = questions.numquestions()
    id = id+1
    next = min(id+1, questions_count)
    prev = max(id-1, 1)
    statistics = stats.stats.get(filename,[0,0])
    spravne = statistics[0]
    celkovo = statistics[1]
    uspesnost = statistics[0]*100.0/max(statistics[1],1)
    uspesnost = int(uspesnost*100)/100.0
    zle_otazky = zle_otazky_dict.get(filename,[])
    print (zle_otazky)
    joke = Jokes().get_joke(uspesnost)
    
    
    # flush log message
    log.flush(request)
    
    return render_to_response('question.html', locals())
 

