from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from django.template import RequestContext
from django.core.mail import send_mail, EmailMessage
from backend.models import *

def remove_and_email_applicant(request, survey_id, user_id):
    subject = "Sorry!"
    message = "We don't want you to live with us."
    applicant = get_object_or_404(UserProfile, pk=user_id)
    print applicant
    print applicant.user.email
    to = applicant.user.email
    email = EmailMessage(subject, message, "remindr.email@gmail.com", [], (to, ))
    email.send()
    response_list = get_object_or_404(ResponseList, responder=user_id, survey=survey_id)
    response_list.survey = None
    response_list.save()
    print response_list.survey
    return redirect('/dash/')
