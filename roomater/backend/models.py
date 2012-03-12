from django.db import models
from django.contrib.auth.models import User, Permission, Group

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    nickname = models.CharField(max_length=200)
    clean_score = models.IntegerField()
    food_score = models.IntegerField()
    about = models.TextField()
    pic = models.ImageField(upload_to='profile_pics')
    def __unicode__(self):
        return str(self.user)

class Question(models.Model):
    questioner = models.ForeignKey(User)
    text = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str(self.questioner)+" "+str(self.text)

class Response(models.Model):
    responder = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    text = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str(self.responder)+" "+str(self.question)+" "+str( self.text)

class Survey(models.Model):
    name = models.CharField(max_length=200)
    questions =models.ManyToManyField(Question)
    def __unicode__(self):
        return str(self.name)

class ResponseList(models.Model):
    name = models.CharField(max_length=200)
    survey = models.ForeignKey(Survey)
    responses = models.ManyToManyField(Response)
    def __unicode__(self):
        return str(self.name)
