from django import forms
from . import models
class yurlform(forms.ModelForm):
    class Meta:
        model=models.extra
        fields=['ename']
class nurlform(forms.ModelForm):
    class Meta:
        model=models.Drive
        fields=['field_name','field_link']        

