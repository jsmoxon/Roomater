from django.db import models

class Suggestions(models.Model):
    suggestions = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date submitted')

class Survey(models.Model):
    survey = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    survey = models.ForeignKey(Survey)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()


