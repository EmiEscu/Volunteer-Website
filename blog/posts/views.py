from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "posts/new.html",{"form":form})

def about(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "posts/about.html",{"form":form})