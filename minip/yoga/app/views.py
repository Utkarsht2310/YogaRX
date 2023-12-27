
from . models import Yoga
from django.db.models import Q

from django.shortcuts import render
from . forms import RegistrationForm

from django.contrib import messages
from django.views import View



def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        yogas = Yoga.objects.filter(Q(name__icontains=searched) | Q(dis__icontains=searched))

        return render(request, "app/search.html", {'searched': searched, 'yogas': yogas})
    else:
        return render(request, "app/search.html", {})


class CustomerRegistrationView(View):
    def get(sef,request):
        form = RegistrationForm()
        return render(request, 'app/registration.html',locals())
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User register successfully! ")
        else:
            messages.warning (request,"Invalid Input Data")

        return render(request, 'app/registration.html',locals())