from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from models import *
from forms import PhotoForm, ProfileForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission, Group
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django import forms
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.conf import settings
import mimetypes

class UploadForm(forms.Form):
    file = forms.ImageField(label='Upload your pic')

def demo(request):
    def store_in_s3(filename):
        conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        b = conn.create_bucket("roommater")
        mime = mimetypes.guess_type(str(filename))[0]
        k = Key(b)
        k.key = filename
        k.set_metadata("Content-Type", mime)
        k.set_contents_from_file(filename)
        k.set_acl("public-read")

    photos = PhotoUrl.objects.all()
    if not request.method == "POST":
        form = UploadForm()
        return render_to_response('demo.html', {"form":form, "photos":photos}, context_instance=RequestContext(request))
    form = UploadForm(request.POST, request.FILES)
    if not form.is_valid():
        return render_to_response('demo.html', {"form":form, "photos":photos}, context_instance=RequestContext(request))

    file = request.FILES["file"]
    store_in_s3(file)
    p = PhotoUrl(url="http://roommater.s3.amazonaws.com/"+str(file))
    p.save()
    photos = PhotoUrl.objects.all()
#i think this is where i should call a function that creates a user and user profile with the request data
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    newprofile = UserProfile(pic=p, user=user,
                             nickname=request.POST['nickname'], clean_score=request.POST['clean_score'],
                             food_score = request.POST['food_score'], about=request.POST['about'])
    newprofile.save()
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    login(request, user)
    return render_to_response('demo.html', {"form":form, "photos":photos}, context_instance=RequestContext(request))


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

#search the site for surveys
@login_required
def list_of_surveys(request):
    surveys = Survey.objects.all()
    return render_to_response('survey_list.html', {'surveys':surveys})

#create a profile with a survey
def create_survey_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            newprofile = UserProfile(pic=request.FILES['pic'], user=user, 
                                     nickname=request.POST['nickname'], clean_score=request.POST['clean_score'],
                                     food_score = request.POST['food_score'], about=request.POST['about'])
            newprofile.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/backend/dash/')
    else:
        form = ProfileForm()
    return render_to_response('profile_create.html', {'form':form}, context_instance=RequestContext(request))

#create a profile without a survey in mind
def create_search_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            newprofile = UserProfile(pic=request.FILES['pic'], user=user,
                                     nickname=request.POST['nickname'], clean_score=request.POST['clean_score'],
                                     food_score = request.POST['food_score'], about=request.POST['about'])
            newprofile.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/backend/surveys/')
    else:
        form = ProfileForm()
    return render_to_response('profile_create.html', {'form':form}, context_instance=RequestContext(request))    

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
#adds survey to UserProfile, this may require a request context for security down the line
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
    
    return redirect('/backend/dash/')
