from django.db import models
from django.contrib.auth.models import User, Permission, Group
from datetime import datetime

class PhotoUrl(models.Model):
    url = models.CharField(max_length=500)
    uploaded = models.DateTimeField()
    
    def save(self):
        self.uploaded = datetime.now()
        models.Model.save(self)

class Room(models.Model):
    price = models.IntegerField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    pic = models.CharField(max_length=500, blank=True, null=True)
    def __unicode__(self):
        return str(self.address)+" "+str(self.city)


class Question(models.Model):
    questioner = models.ForeignKey(User)
    text = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str(self.text)

class Response(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str(self.question)+" "+str( self.text)

class Survey(models.Model):
    name = models.CharField(max_length=200)
    questions =models.ManyToManyField(Question)
    room = models.ForeignKey(Room)
    def __unicode__(self):
        return str(self.name)

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    survey = models.ForeignKey(Survey, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200)
    clean_score = models.IntegerField(blank=True)
    smoker = models.NullBooleanField()
    about = models.TextField(blank=True)
    rooms = models.ManyToManyField(Room, blank=True, null=True)
    pic = models.CharField(max_length=500)
    def __unicode__(self):
        return str(self.user)

class ResponseList(models.Model):
    name = models.CharField(max_length=200)
    responder = models.ForeignKey(UserProfile)
    survey = models.ForeignKey(Survey)
    responses = models.ManyToManyField(Response)
    def __unicode__(self):
        return str(self.name)
