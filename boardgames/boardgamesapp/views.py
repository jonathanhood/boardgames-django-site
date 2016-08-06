from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import Bot

@login_required
def index(request):
    try:
        bot = Bot.objects.get(user=request.user)
    except:
        bot = None
    return render(request, 'index.html', {"bot":bot})

