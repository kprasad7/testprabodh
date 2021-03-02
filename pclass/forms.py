from django import forms
from . import models

class sixform(forms.ModelForm):
    class Meta:
        model=models.sixth
        fields=['six' , 'sixn'] 

class sevform(forms.ModelForm):
    class Meta:
        model=models.sevennn
        fields=['sev' , 'sevn'] 

class eigform(forms.ModelForm):
    class Meta:
        model=models.eightn
        fields=['eig' , 'eign'] 

class nineform(forms.ModelForm):
    class Meta:
        model=models.nine
        fields=['nine' , 'ninen'] 


class tenform(forms.ModelForm):
    class Meta:
        model=models.tennn
        fields=['ten' , 'tenn'] 

class spform(forms.ModelForm):
    class Meta:
        model=models.spnn
        fields=['spp' , 'sppp'] 

class labform(forms.ModelForm):
    class Meta:
        model=models.labbb
        fields=['labx' , 'labxx']  
class enform(forms.ModelForm):
    class Meta:
        model=models.envvv
        fields=['evv' , 'evvnn']                

    