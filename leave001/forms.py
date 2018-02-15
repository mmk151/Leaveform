from django import forms
from leave001.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class leaveapply(forms.ModelForm):
    class Meta:
        model = leavemodels
        fields=['section','reason',]

class signform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    email=forms.CharField(max_length=80)
    first_name=forms.CharField(max_length=55)
    last_name = forms.CharField(max_length=55)



    class Meta:
        model=user
        fields=['first_name','last_name','email','password','confirm_password','rollno',]


    def save(self,commit=True):
            data=self.cleaned_data
            first_name = data['first_name']
            last_name = data['last_name']
            rollno = data['rollno']
            password = data['password']
            email = data['email']
            user_obj = User.objects.create_user(username=rollno,first_name=first_name,last_name=last_name,email=email,password=password),
            user.objects.create(rollno=rollno,foreign_user=user_obj)
            return user_obj
