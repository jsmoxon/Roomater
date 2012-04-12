from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect
from django.template import RequestContext
from django.core.mail import send_mail, EmailMessage
from backend.models import *

def remove_and_email_applicant(request, survey_id, user_id):
    """
    Removes ResponseList from the survey and sends an email to the responder saying the room is full.
    """
    applicant = get_object_or_404(UserProfile, pk=user_id)
    response_list = get_object_or_404(ResponseList, responder=user_id, survey=survey_id)
    subject = "Roommater - Sorry "+str(response_list.survey.room)+" is full."
    message = "Thank you for applying to "+str(response_list.survey.room)+" but the room is full. We wish you all the best as you continue to search for a room.\n\nSincerely,\n\n"+str(response_list.survey.room)
    to = applicant.user.email
    email = EmailMessage(subject, message, "remindr.email@gmail.com", [], (to, ))
    email.send()
    response_list.survey = None
    response_list.save()
    return redirect('/dash/')
