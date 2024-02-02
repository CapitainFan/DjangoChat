from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room

@login_required
def rooms(requests):
    rooms = Room.objects.all()

    return render(requests, 'room/rooms.html', {'rooms': rooms})