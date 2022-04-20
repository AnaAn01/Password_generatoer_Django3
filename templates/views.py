from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'home.html')

def password(request):

    letters=list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('upper'):
        letters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        letters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        letters.extend(list('1234567890'))

    length=int(request.GET.get('length', 10))
    #Бере значення з Html файла
    thepassword = ''
    for x in range(length):
        thepassword+=random.choice(letters)
    return render(request, 'password.html', {'password':thepassword})

def about(request):
    return render(request, 'about.html')