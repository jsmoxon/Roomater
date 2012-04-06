from django.forms import ModelForm
from models import ResponseList, Response, UserProfile
from django import forms
from django.contrib.auth.models import User, Permission, Group


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

#for validation purposes, we create a user form to give correct error messages to users
class UserRegForm(ModelForm):
    class Meta:
        model = User
        exclude = ('first_name', 'last_name', 'email', 'staff_status', 'groups', 'last_login', 'date_joined', 'user_permissions', 'is_active', 'is_superuser', 'is_staff', )
        widgets = {
            'password' : forms.PasswordInput()
        }
            
           
        
class SearchRegForm(forms.Form):
    email = forms.EmailField(max_length=100)
    name = forms.CharField(max_length=100)
#    clean_score = forms.IntegerField(label="How much do you value cleanliness?", widget=forms.Select(choices=clean_scores))
    about = forms.CharField(widget=forms.Textarea)
    file = forms.ImageField(label='Upload a photo of yourself; .png files only')
    
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
#    clean_score = forms.IntegerField()
    about = forms.CharField(widget=forms.Textarea, required=False)
    file = forms.ImageField(label='Upload your picture', required=False)
