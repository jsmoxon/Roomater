from django.forms import ModelForm
from models import ResponseList, Response

class ResponseForm(ModelForm):
    class Meta:
        model = ResponseList
