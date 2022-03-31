from django.shortcuts import render, redirect

from chat.models import room, Message


def index_view(request):
    return render(request, 'chat/index.html', {'rooms': room.objects.all(), })


def room_view(request, room_name):
    chat_room, created = room.objects.get_or_create(name=room_name)
    msg = Message.objects.filter(room=chat_room)
    return render(request, 'chat/room.html', {'room': chat_room, 'x': msg})
