from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def test(request):
    return render(request,'test.html')

def testimonio(request):
    return render(request,'testimonio.html')

def faq(request):
    return render(request,'faq.html')

def about(request):
    return render(request,'about.html')

def ansiedad(request):
    return render(request,'ansiedad.html')