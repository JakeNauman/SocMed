from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Post
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse


def home(request):
    data = Post.objects.all()
    if not request.user.is_authenticated:
            user = authenticate(request)
            if user is not None:
                login(request, user)
            else:
                return redirect(reverse('login'))
    return render(request, 'socmed/home.html', {'Posts':data})

def add(request):
    text = request.POST.get('text')

    if text:
        post = Post(user=request.user, text=text)
        post.save()

    return redirect('/home')
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form":form})
