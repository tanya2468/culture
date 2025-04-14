import re

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .forms import IndianForm
from .models import Indian


# Create your views here.
def home(request):
    return render(request,"home.html")
def login(request):
    return render(request,'login.html')
def Register(request):
    return render(request,'sign.html')
def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username Already Exists')
                return render(request, 'sign.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()

                messages.success(request, "Account Created")
                return render(request, 'login.html')
        else:
            messages.error(request, 'Password do not match')
            return render(request, 'sign.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

            return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def item(request,title,category):
    item = get_object_or_404(Indian,title=title)
    if category == "Dances":
        return render(request,'dance.html',{'dance': item})
    elif category == "Cuisines":
        return render(request,'cuisine.html',{'cuisine':item})
    elif category == "religions":
        return render(request,'religion.html',{'religion':item})
    elif category == "Festivals":
        return render(request,'festival.html',{'festival':item})
    elif category == "clothings":
        return render(request,'clothing.html',{'clothing':item})
    elif category == "languages":
        return render(request,'language.html',{'language':item})
    elif category == "holy book":
        return render(request,'holybooks.html',{'holybook':item})
    elif category == "arts":
        return render(request,'artsandcrafts.html',{'arts':item})
    # elif category == "Ayurveda and Traditional Medicine":
    #     return render(request,'ayurveda.html',{'ayurveda':item})
    elif category == "sport":
        return render(request,'sports.html',{'sport':item})

def map(request):
    return render(request,'maps.html')

def contact(request):
    return render(request,'contact.html')


def addindian(request):
    if request.method == 'POST':
        form = IndianForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IndianForm()
    return render(request, 'adddata.html', {'form': form})

def allindians(request):
    allindians = Indian.objects.all()
    return render(request, 'home.html', {'allindians': allindians})