from django.shortcuts import render

def home_view(request):
    if request.htmx:
        return render(request, 'home/home.html#main')
    return render(request, 'home/home.html')
