from cgitb import text
from django.shortcuts import redirect, render
from . forms import *
from django.views import generic
from email import message
from multiprocessing import context
from unittest import result
from django.shortcuts import render, redirect
from youtubesearchpython import VideosSearch
from django.contrib import messages
import requests
from django.contrib.auth.decorators import login_required

from dashboard.forms import DashboardSearch, UserRegistrationForm


#creating views here
@login_required
def home(request):
    return render(request,'dashboard/home.html')

#creating for login
#def login(request):
#    return render(request,'dashboard/login.html')

#creating for register
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f"Account created for {user}!! ")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
    'form':form
    }
    return render(request,"dashboard/register.html",context)

@login_required    
def youtube(request):
    if request.method == "POST":
        form =DashboardSearch(request.POST)
        text= request.POST['text']
        video = VideosSearch(text,limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title']
            }

    else:
        form = DashboardSearch()
    context = {'form':form}
    return render(request,'dashboard/youtube.html',context)



def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title=request.POST['title'],desc=request.POST['desc'])
            notes.save()
        messages.success(request,f"Notes Save By {request.user.username} Successfully")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)

@login_required
def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")


class NotesDetailView(generic.DetailView):
    model = Notes




    