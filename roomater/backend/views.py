from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *
from django.contrib.auth.models import User, Permission, Group

def index(request, entry_id):
    list = ResponseList.objects.filter(survey__id=entry_id)
    return render_to_response('index.html', {'list':list})    

#displays a survey
def display_survey(request, entry_id):
    s = get_object_or_404(Survey, pk=entry_id)
    question = s.questions.all()
    return render_to_response('real_survey.html', {'s':s, 'question':question})

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
