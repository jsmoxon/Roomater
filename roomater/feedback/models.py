from django.db import models
import datetime

class Suggestion(models.Model):
    suggestion = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date submitted')
    def __unicode__(self):
		return self.suggestion

class Survey(models.Model):
    survey = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
		return self.survey

class Option(models.Model):
    survey = models.ForeignKey(Survey)
    option = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
		return self.option

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    
    def __unicode__(self):
        return self.choice