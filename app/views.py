from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import signUpForm


def home(request):
    return render(request,'app/home.html')

def signUp(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user) 
            messages.success(request, "Account created successfully!!")
            return redirect('/') 
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = signUpForm()
    
    return render(request, 'signup.html', {'form': form})
