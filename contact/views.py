from django.shortcuts import render

def contact_view(request):
    if request.htmx:
        return render(request, 'contact/contact.html#contact')
    return render(request, 'contact/contact.html')