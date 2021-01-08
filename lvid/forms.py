from django import forms
from . import models
class yurlformm(forms.ModelForm):
    class Meta:
        model=models.Itemm
        fields=['videoo','cap']