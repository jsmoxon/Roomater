from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *
from django.contrib.auth.models import User, Permission, Group

def index(request):
    s = get_object_or_404(Survey, pk=1)
    q = s.question_set.all()
    r = Response.objects.filter(question__in=q)
    responders = Response.objects.filter(responder__in=q)
    u = User.objects.all()
#missing chunk! needs another model i think there is a survey, then a SurveyAnswerSet
    return render_to_response('index.html', {'s':s,'q':q,'r':r, 'responders':responders, 'u':u})

#create a survey
#def create_survey(request):
    

#displays a survey
def display_survey(request, entry_id):
    s = get_object_or_404(Survey, pk=entry_id)
    q = s.question_set.all()
    r = "la"
    return render_to_response('real_survey.html', {'s':s,'q':q,'r':r})

#submits a survey     
@csrf_exempt
def submit_survey(request):
    i = 1
    while i<11:
        try:
            new = Response()
            new.responder = request.user
            new.question = Question.objects.get(text=request.POST['row'+str(i)])
            new.save()
            new.text = str(request.POST['r'+str(i)])
            new.save()
        except:
            pass
        i+=1
    return HttpResponse("Thanks!")
