
from django.shortcuts import render,redirect
from .models import leavemodels
from leave001.forms import *
# from django.contrib.auth.forms import login,authenticate
# from django.contrib.auth.models import User

def home(request):
    return render(request,'leave001/home.html')


def login(request):
    return render(request,'registration/login.html')


def apply(request):

    form = leaveapply(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'leave001/leaveapply.html',{'form':form})


def signup(request):
    form1 = signform(request.POST)
    if form1.is_valid():
        password = form1.cleaned_data.get("password")
        confirm_password = form1.cleaned_data.get("confirm_password")
        if password==confirm_password:
            form1.save()
            return redirect('login')
        else:
            form1.add_error('confirm_password', 'The passwords do not match')

    else:
        form1 = signform(request.POST)
    return render(request, 'leave001/signup.html', {'form1': form1})


def applied(request):
    x = request.user.id
    if x==10:
        data = leavemodels.objects.all()
        return render(request, 'leave001/data.html', {'data': data})
    else:
        data= leavemodels.objects.filter(id=x)
        return render(request, 'leave001/data.html', {'data': data})
