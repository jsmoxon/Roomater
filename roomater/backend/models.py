from django.db import models
from django.contrib.auth.models import User, Permission, Group

class Question(models.Model):
    questioner = models.ForeignKey(User)
    text = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str(self.questioner)+" "+str(self.text)

class Response(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str(self.question)+" "+str( self.text)

class Survey(models.Model):
    name = models.CharField(max_length=200)
    questions =models.ManyToManyField(Question)
    def __unicode__(self):
        return str(self.name)

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    survey = models.ForeignKey(Survey, on_delete=models.SET_NULL, blank=True, null=True)
    nickname = models.CharField(max_length=200)
    clean_score = models.IntegerField(blank=True)
    food_score = models.IntegerField(blank=True)
    about = models.TextField(blank=True)
    pic = models.ImageField(upload_to='profile_pics', blank=True)
    def __unicode__(self):
        return str(self.user)

class ResponseList(models.Model):
    name = models.CharField(max_length=200)
    responder = models.ForeignKey(UserProfile)
    survey = models.ForeignKey(Survey)
    responses = models.ManyToManyField(Response)
    def __unicode__(self):
        return str(self.name)
