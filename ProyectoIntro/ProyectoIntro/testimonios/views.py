from django.shortcuts import redirect, render

from .forms import AutoForm
from .models import Formul


# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")
def subirtesti(request):
    if request.method=="POST":
        form= AutoForm(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.save()
            return redirect("dashboard")
    else:
        form=AutoForm()
    return render (request, "subirtesti.html",
     {'form':form})

def vertesti(request):
    formul=Formul.objects.all()
    return render (request, "vertesti.html",
    {'formul': formul})

def revisartesti(request, pk):
    formula= Formul.objects.get(pk=pk)
    return render(request, 'revisartesti.html',
        {'formula': formula})
