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

clean_scores = (
    ('1', 'Cleanliness is not that important to me'),
    ('2', 'Cleanliness is moderately important to me'),
    ('3', 'Cleanliness is godliness')
)

smoker_choices = (
    ('Yes', 'Yes'),
    ('No', 'No')
)

class SearchRegForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    email = forms.EmailField(max_length=100)
    name = forms.CharField(max_length=100)
    clean_score = forms.IntegerField(label="How much do you value cleanliness?", widget=forms.Select(choices=clean_scores))
#    smoker = forms.NullBooleanField(widget=forms.Select(choices=smoker_choices))
    about = forms.CharField(widget=forms.Textarea)
    file = forms.ImageField(label='Upload your pic; .png files only')
    
class ListRegForm(forms.Form):
    price = forms.IntegerField()
    address = forms.CharField(max_length=150)
    city = forms.CharField(max_length=150)
    state = forms.CharField(max_length=150)
    zip = forms.CharField(max_length=150)
    room_about = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150)
    email = forms.EmailField()
    name = forms.CharField(max_length=150)
    clean_score = forms.IntegerField()
#    smoker = forms.NullBooleanField()
    about = forms.CharField(widget=forms.Textarea)
    file = forms.ImageField(label='Upload your picture')
