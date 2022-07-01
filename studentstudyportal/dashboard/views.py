from cgitb import text
from email import message
from multiprocessing import context
from unittest import result
from django.shortcuts import render
from youtubesearchpython import VideosSearch

from dashboard.forms import DashboardSearch, UserRegistrationForm


#creating views here
def home(request):
    return render(request,'dashboard/home.html')

def login(request):
    return render(request,'dashboard/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message.success(request,f"Account created for {username}!! ")
    else:
        form = UserRegistrationForm()
    context = {
    'form':form
    }
    return render(request,"dashboard/register.html",context)
    
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




    