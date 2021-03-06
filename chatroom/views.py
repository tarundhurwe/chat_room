from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Room, Message
# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request, room):
    try:
        username = request.GET.get('username')
        if username is not None:
            room_details = Room.objects.get(name = room)
            return render(request, 'room.html',{
                'room': room,
                'username': username,
                'room_details': room_details
                })
        else:
            return redirect('/')
    except:
        return redirect('/')

def check(request):
    if request.method == "POST":
        room = request.POST['room_name']
        username = request.POST['username']
        if Room.objects.filter(name = room).exists():
            return redirect('/'+room+'/?username='+username)
        else:
            new_room = Room.objects.create(name = room)
            new_room.save()
            return redirect("/"+room+'/?username='+username)
    else:
        return redirect('/')

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value = message, user = username, room = room_id)
    new_message.save()
    return HttpResponse("message sent successfully")

def fetch_messages(request, room):
    try:
        room_details = Room.objects.get(name = room)

        messages = Message.objects.filter(room = room_details.id)
        return JsonResponse({"messages":list(messages.values())})
    except:
        return redirect('/')

