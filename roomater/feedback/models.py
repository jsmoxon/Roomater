from django.db import models
import datetime

class fSuggestion(models.Model):
    suggestion = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date submitted')
    def __unicode__(self):
        return self.suggestion

class fQuestion(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.question

class fOption(models.Model):
    question = models.ForeignKey(fQuestion)
    option = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.option