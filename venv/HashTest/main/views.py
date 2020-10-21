from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from .forms import HashForm
from .models import Hash
import hashlib
# Create your views here.

def home(request):
    if request.method == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('UTF-8')).hexdigest()
            try:
                Hash.objects.get(hashed = text_hash)
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hashed = text_hash
                hash.save()
            return redirect('hash', hash = text_hash)

    Form = forms.HashForm()
    return render(request, 'home.html', {'form' : Form})

def hash(request, hash):
    hash = Hash.objects.get(hashed = hash)
    return render(request, 'hash.html', {'hash': hash,})

