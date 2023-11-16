from django.shortcuts import render, HttpResponse
from datetime import datetime
from Data.models import Contact
from Data.models import Newsletter
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        email = request.POST.get('email')
        newsletter = Newsletter(email=email, date=datetime.today())
        newsletter.save()
        messages.success(request, 'You are successfully subscribed!')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
 
def services(request):
    return render(request, 'service.html')

def technology(request):
    return render(request, 'technology.html')

def team(request):
    return render(request, 'team.html')

def clients(request):
    return render(request, 'clients.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, subject=subject,desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your form is submitted!')

    return render(request, 'contact.html')

#def login(request):
    #return render(request, 'login.html')


