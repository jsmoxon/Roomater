from django.forms import ModelForm
from models import ResponseList, Response, UserProfile
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'survey', 'pic')

class PhotoForm(forms.Form):
    pic = forms.ImageField(
        label = "select a pic",
        help_text = "png only!"
    )

class SearchRegForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    name = forms.CharField(max_length=100)
    clean_score = forms.IntegerField()
    smoker = forms.BooleanField()
    about = forms.CharField(widget=forms.Textarea)
    file = forms.ImageField(label='Upload your pic')
    
class ListRegForm(forms.Form):
    price = forms.IntegerField()
    address = forms.CharField(max_length=150)
    city = forms.CharField(max_length=150)
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150)
    email = forms.EmailField()
    name = forms.CharField(max_length=150)
    clean_score = forms.IntegerField()
    smoker = forms.NullBooleanField()
    about = forms.CharField(widget=forms.Textarea)
    file = forms.ImageField(label='Upload your picture')
