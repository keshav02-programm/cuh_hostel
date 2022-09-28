from django.shortcuts import render
from .forms import RegisterationForm
from django.views import View
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

# def login(request):
#  return render(request, 'login.html')


class RegisterationView(View):
    def get(self, request):
        form = RegisterationForm()
        return render(request, 'register.html', {'form':form})

    def post(self, request):
        form = RegisterationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation registerd successfullty')
            form.save()
        return render(request, 'register.html', {'form':form})
