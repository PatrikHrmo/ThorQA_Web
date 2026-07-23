from django.shortcuts import render

def about_view(request):
    if request.htmx:
        return render(request, 'about/about.html#about')
    return render(request, 'about/about.html')