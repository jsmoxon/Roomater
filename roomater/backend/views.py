from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from models import *
from forms import ResponseForm
from django.contrib.auth.models import User, Permission, Group
from django.views.generic.edit import CreateView


def index(request, entry_id):
    list = ResponseList.objects.filter(survey__id=entry_id)
    return render_to_response('index.html', {'list':list})    

def create_survey(request):
    return render_to_response('create_survey.html')

@csrf_exempt
def submit_create_survey(request):
    survey = Survey()
    survey.name = request.user.username
    survey.save()
    i = 1
    while i<6:
        try:
            q = Question()
            q.questioner = request.user
            q.save()
            q.text = str(request.POST['q'+str(i)])
            q.save()
            survey.questions.add(q)
            survey.save()
        except:
            pass
        i+=1
    return redirect('/index/4')

#displays a survey
def display_survey(request, entry_id):
    s = get_object_or_404(Survey, pk=entry_id)
    question = s.questions.all()
    return render_to_response('real_survey.html', {'s':s, 'question':question})

class AddResponseView(CreateView):
    form_class = ResponseForm
    template_name = "create.html"
    success_url = "/index/1/"
    def get_form(self, form_class):
        form = super(AddResponseView, self).get_form(form_class)
        form.instance.person = self.request.user
        return form

#submits a survey     
@csrf_exempt
def submit_survey(request, entry_id):
    list = ResponseList()
    list.survey = Survey.objects.get(pk=entry_id)
    list.name = request.user.username +" "+ str(list.survey)
    list.save()
    i = 1
    while i<11:
        try:
            new = Response()
            new.responder = request.user
            new.question = Question.objects.get(text=request.POST['row'+str(i)])
            new.save()
            new.text = str(request.POST['r'+str(i)])
            new.save()
            list.responses.add(new)
            list.save()
        except:
            pass
        i+=1
    
    return HttpResponse("Thanks!")
