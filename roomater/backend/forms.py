from django.forms import ModelForm
from models import ResponseList, Response, UserProfile
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'survey',)

class PhotoForm(forms.Form):
    pic = forms.ImageField(
        label = "select a pic",
        help_text = "png only!"
    )

