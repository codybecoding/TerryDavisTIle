from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about_index(request):
    return render(request, 'about.html')

def contact_index(request):
    return render(request, 'contact.html')
