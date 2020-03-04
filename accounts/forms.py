from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.contrib.auth import get_user_model
from django.forms.widgets import DateInput

class CustomUserCreationForm(UserCreationForm):
#Defines fields necessary for signing up, password is a hidden field added by Django
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)
        
class CustomUserChangeForm(UserChangeForm):

    password = None #Hides this field from user
    #Defines fields and also the widget for dates
    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name','MobileNumber','dob')
        labels = {'dob':('D.O.B'), }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

class AddAreaForm(forms.ModelForm):

    #Defines fields and how presented
    class Meta:
        model = Areas
        fields = ("name","areaLead","volunteerNumber",)
        labels = {'name': ('Area Name'),
        'areaLead': ('Area Lead'),
        'volunteerNumber':('Number of Volunteers'),
        }
        error_messages = {"username_exists": ("Area already exists!")} #Defines error message
    
    #Queries db for list of area leads and sets these to be a drop down list for the areaLead field
    def __init__(self, *args,**kwargs):
        super (AddAreaForm,self ).__init__(*args,**kwargs)
        self.fields['areaLead'].queryset = CustomUser.objects.filter(groups__name='Area Leads')

class AreaLinkerForm(forms.ModelForm):

    #Defines fields and how presented
    class Meta:
        model = Area_Linker
        fields = ("area","volunteer",)