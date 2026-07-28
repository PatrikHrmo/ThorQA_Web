from django.urls import path
from . views import demo_view

app_name = "demo"

urlpatterns = [
    path("demo/", demo_view, name="demo")
]