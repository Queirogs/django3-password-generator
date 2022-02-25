from django.shortcuts import render
from django.http import HttpResponse
import random

from h11 import SWITCHED_PROTOCOL

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    passwordLenght = int(request.GET.get('lenght', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXZ'))
        
    if request.GET.get('special'):
        characters.extend(list('!@#$%¨&*()_+-='))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for x in range(passwordLenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})