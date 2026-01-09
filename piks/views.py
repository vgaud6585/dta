from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Message

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def chat_room(request):
    return render(request, 'chat/room.html')

def send_message(request):
    if request.method == 'POST':
        msg = request.POST.get('message')
        if msg:
            Message.objects.create(user=request.user, content=msg)
        return JsonResponse({'status': 'sent'})

def get_messages(request):
    messages = Message.objects.all().values('user__username', 'content')
    return JsonResponse({'messages': list(messages)})