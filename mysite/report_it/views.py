from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponse

def index(request):
    return render(request, 'report_it/index.html')
