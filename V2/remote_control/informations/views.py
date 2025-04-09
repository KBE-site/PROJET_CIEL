from django.shortcuts import render

def index(request):
    return render(request, 'informations/index.html')

def room(request, room_name):
    return render(request, 'informations/room.html', {"room_name": room_name})
