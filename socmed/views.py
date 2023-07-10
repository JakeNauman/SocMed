from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Post


def home(request):
    data = Post.objects.all()
    return render(request, 'socmed/home.html', {'Posts':data})

def add(request):
    username = request.POST.get('username')
    text = request.POST.get('text')

    if username and text:
        post = Post(username=username, text=text)
        post.save()
    return HttpResponseRedirect('/')