from django.shortcuts import render

def demo_view(requests):
    if requests.htmx:
        return render(requests, "demo/demo.html#demo")
    return render(requests, "demo/demo.html")