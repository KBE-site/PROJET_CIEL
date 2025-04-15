from django.shortcuts import render, redirect
from api.rc import post_rc, get_object

def index(request):
    return render(request, 'main_panel/index.html', {'objects': get_object()})

def room_object(request, room_name):
    # planet = request.POST.get("planet")
    return render(request, 'main_panel/object.html', {'object': room_name})

def move(request):
    top = request.POST.get("b_haut")
    bottom = request.POST.get("b_bas")
    left = request.POST.get("b_gauche")
    right = request.POST.get("b_droite")

    if top != None:
        post_rc("top")
    if bottom != None:
        post_rc("bottom")
    if left != None:
        post_rc("left")
    if right != None:
        post_rc("right")

    return redirect('index')