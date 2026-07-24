from django.shortcuts import render, redirect

def home_view(request):
    if request.htmx:
        return render(request, 'home/home.html#home')
    return render(request, 'home/home.html')

def popup_view(request):
    if request.htmx:
        return render(request, 'home/test.html#popup')
    return redirect('home:home')