from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):

    context = {}
    return render(request, 'generator/home.html', context)

def aboutPage(request):

    context = {}
    return render(request, 'generator/about.html', context )

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQSRTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    context = {'password':thepassword}
    return render(request, 'generator/password.html', context)

