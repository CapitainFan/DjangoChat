from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm

def frontpage(requests):
    return render(requests, 'core/frontpage.html')

def signup(requests):
    if requests.method == 'POST':
        form = SignUpForm(requests.POST)

        if form.is_valid():
            user = form.save()

            login(requests, user)

            return redirect('frontpage')
    
    else:
        form = SignUpForm()

    return render(requests, 'core/signup.html')
