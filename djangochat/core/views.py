from django.shortcuts import render

def frontpage(requests):
    return render(requests, 'core/frontpage.html')
