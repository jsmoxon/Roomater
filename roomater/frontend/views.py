from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from feedback.models import *

def home(request):
    return render_to_response('home.html')
