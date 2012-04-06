from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from models import *
from forms import ProfileForm, SearchRegForm, ListRegForm, UserRegForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission, Group
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django import forms
from s3 import store_in_s3
from maps import geo_code

class UploadForm(forms.Form):
    file = forms.ImageField(label='Upload your pic')


def create_survey(request):
    standard_questions = Question.objects.filter(standard=True)
    if not request.method == "POST":
        form = ListRegForm()
        user_form = UserRegForm(request.POST)
        return render_to_response('create_survey.html', {"form":form, "user_form":user_form, "standard":standard_questions}, context_instance=RequestContext(request))
    form = ListRegForm(request.POST, request.FILES)
    user_form = UserRegForm(request.POST)
    print "post"
    if not form.is_valid() or not user_form.is_valid():
        print "something not valid"
        return render_to_response('create_survey.html', {"form":form, "user_form":user_form, "standard":standard_questions}, context_instance=RequestContext(request))
    file = request.FILES["file"]
    store_in_s3(file)
    p = PhotoUrl(url="http://roommater.s3.amazonaws.com/"+str(file))
    p.save()
#create a new user and profile
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    newprofile = UserProfile(pic=p.url, user=user,
                             name=request.POST['name'], clean_score=request.POST['clean_score'],
                             about=request.POST['about'])
    newprofile.save()
#log the new user in
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    login(request, user)
#submit the survey they just made
    room = Room(price=request.POST["price"], address=request.POST["address"], city=request.POST["city"], state=request.POST["state"], zip=request.POST["zip"], about=request.POST["room_about"], lat=geo_code(request.POST["address"], request.POST["city"], request.POST['state'], request.POST['zip'])[0], lng = geo_code(request.POST["address"], request.POST["city"], request.POST['state'], request.POST['zip'])[1])
    room.save()
#    print geo_code(request.POST["address"], request.POST["city"])[0]
    submit_create_survey(request, room)
    return redirect('/dash/')

@login_required
def dash(request):
    most_recent ="dlfkj"
    try:
        user_profile = request.user.get_profile()
    except:
        return render_to_response('profile_create.html', {}, context_instance=RequestContext(request))
    pic = user_profile.pic
    try:
        most_recent = user_profile.rooms.all()[len(user_profile.rooms.all())-1]
    except:
        most_recent = ""
    try:
        responses = ResponseList.objects.filter(survey__id=user_profile.survey.id)
    except:
        responses = "No Responses"
    return render_to_response('dash.html', {'pic':pic, 'profile':user_profile, 'responses':responses, 'most_recent':most_recent}, context_instance=RequestContext(request))

#search the site for surveys

def list_of_surveys(request):
    surveys = Survey.objects.all()
    return render_to_response('survey_list.html', {'surveys':surveys}, context_instance=RequestContext(request))

#create a profile without a survey in mind
def create_search_profile(request):
    if request.method == 'POST':
        user_form = UserRegForm(request.POST)
        form = SearchRegForm(request.POST, request.FILES)
        if form.is_valid() and user_form.is_valid():
#upload photo
            file = request.FILES["file"]
            store_in_s3(file)
            p = PhotoUrl(url="http://roommater.s3.amazonaws.com/"+str(file))
            p.save()
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            newprofile = UserProfile(pic=p.url, user=user,
                             name=request.POST['name'], clean_score=request.POST['clean_score'],
                             about=request.POST['about'])
            newprofile.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            if request.REQUEST.get('next' '') != None:
                redirect_to = request.REQUEST.get('next' '')
            else: 
                redirect_to = '/dash/'
            return redirect(redirect_to)
    else:
        user_form = UserRegForm()
        form = SearchRegForm()
    return render_to_response('registration/login.html', {'form':form, 'user_form':user_form}, context_instance=RequestContext(request))    


@csrf_exempt
def submit_create_survey(request, room):
    survey = Survey()
    survey.name = request.user.username
    survey.room = room
    survey.save()
    pre_selected_questions = Question.objects.filter(standard=True)
    for ques in pre_selected_questions:
        try:
            test = request.POST[str(ques.text)]
            survey.questions.add(ques)
            survey.save()
        except:
            pass
    questions = Question.objects.all()
    question_list = []
    for question in questions:
        question_list.append(question.text)
    i = 1
    while i<11:
        if request.POST['q'+str(i)] !="":
            if request.POST['q'+str(i)] in question_list:
                q = Question.objects.get(text=request.POST['q'+str(i)])
            else:
                q = Question()
                q.questioner = request.user
                q.save()
                q.text = str(request.POST['q'+str(i)])
                q.save()
            survey.questions.add(q)
            survey.save()
        i+=1

#adds survey to UserProfile, this may require a request context for security down the line
    user_profile = request.user.get_profile()
    user_profile.survey = Survey.objects.get(name=str(survey))
    user_profile.save()
    return redirect('/dash/')

#displays a survey
def display_survey(request, entry_id):
    s = get_object_or_404(Survey, pk=entry_id)
    question = s.questions.all()
    return render_to_response('real_survey.html', {'s':s, 'question':question}, context_instance=RequestContext(request))

#submits a survey     
@login_required
@csrf_exempt
def submit_survey(request, entry_id):
    list = ResponseList()
    list.survey = Survey.objects.get(pk=entry_id)
    list.name = request.user.username +" "+ str(list.survey)
    user_profile = request.user.get_profile()
    print user_profile
    print list.survey.room
    print user_profile.rooms.all
    if list.survey.room not in user_profile.rooms.all():
        user_profile.rooms.add(list.survey.room)
        list.responder = user_profile
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
    else:
        return redirect('/one_room/')
    return redirect('/dash/')
