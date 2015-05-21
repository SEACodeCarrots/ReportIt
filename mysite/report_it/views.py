from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'report_it/index.html')

def log(request):
    send_mail('Test Subject', 'Test Message', settings.EMAIL_HOST_USER, ['hatamyarg@gmail.com'], fail_silently=False)
    return HttpResponseRedirect('confirmation')

def confirmation(request):
    return render(request, 'report_it/confirmation.html')


