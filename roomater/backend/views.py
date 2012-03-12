from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from models import *
from forms import ResponseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission, Group
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

@login_required
def dash(request):
    try:
        user_profile = request.user.get_profile()
    except:
        return render_to_response('profile_create.html')
    pic = user_profile.pic
    try:
        responses = ResponseList.objects.filter(survey__id=user_profile.survey.id)
    except:
        responses = "No Responses"
    return render_to_response('dash.html', {'pic':pic, 'profile':user_profile, 'responses':responses})

def log_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            try:
                profile = request.user.get_profile()
                return redirect('/backend/dash/')
            except:
#                UserProfile.objects.get_or_create(user=user)
                return render_to_response('profile_create.html')
        else:
            return HttpResponse('Please submit a valid password')
    else:
        return HttpResponse('Roomater is in private beta; please check again later.')

#submit a profile
@csrf_exempt
def create_profile(request):
    profile = UserProfile()
    profile.user = request.user
    profile.nickname = str(request.POST['nickname'])
    profile.food_score = int(request.POST['food_score'])
    profile.clean_score = int(request.POST['clean_score'])
    profile.about = str(request.POST['about'])
    profile.save()
    return redirect('/backend/dash/')

#creating surveys
def create_survey(request):
    user_profile = request.user.get_profile()
    pic = user_profile.pic
    return render_to_response('create_survey.html', {'pic':pic})

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
#adds survey to UserProfile
    user_profile = request.user.get_profile()
    user_profile.survey = Survey.objects.get(name=str(survey))
    user_profile.save()
    return redirect('/backend/dash/')

#displays a survey
@login_required
def display_survey(request, entry_id):
    s = get_object_or_404(Survey, pk=entry_id)
    question = s.questions.all()
    return render_to_response('real_survey.html', {'s':s, 'question':question})

#submits a survey     
@csrf_exempt
def submit_survey(request, entry_id):
    list = ResponseList()
    list.survey = Survey.objects.get(pk=entry_id)
    list.name = request.user.username +" "+ str(list.survey)
    user_profile = request.user.get_profile()
    list.responder = user_profile
    list.save()
    i = 1
    print "list made"
    while i<11:
        print "loop start"
        try:
            print "try start"
            new = Response()
            print "new init"
            new.responder = request.user
            print "responder added" 
            new.question = Question.objects.get(text=request.POST['row'+str(i)])
            new.save()
            print "response started"
            new.text = str(request.POST['r'+str(i)])
            new.save()
            list.responses.add(new)
            list.save()
        except:
            pass
        i+=1
    
    return redirect('/backend/dash/')
