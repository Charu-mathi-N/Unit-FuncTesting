from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def home(request):
    Form = forms.HashForm()
    return render(request, 'home.html', {'form' : Form})
