from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from models import Bot
from forms import UploadFileForm
import os
import subprocess

def write_file_to_disk(uploaded_file, path):
    with open(os.path.join(path,uploaded_file.name), 'wb+') as dest:
        for chunk in uploaded_file.chunks():
            dest.write(chunk)

    if(uploaded_file.name.endswith("gz")):
        subprocess.check_output("tar -xvf {}".format(uploaded_file.name), shell=True, cwd=path)

@login_required
def index(request):
    try:
        bot = Bot.objects.get(user=request.user)
    except:
        bot = None
    return render(request, 'index.html', {"bot":bot, "form" : UploadFileForm()})

@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            bot = Bot.objects.get(user=request.user)
            write_file_to_disk(request.FILES['file'], bot.path)
            return HttpResponseRedirect("/")

